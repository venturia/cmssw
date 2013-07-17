#include "UserCode/TrackerTrackMixing/interface/TrackMixingAssociator.h"
#include "DataFormats/TrackerRecHit2D/interface/SiPixelRecHit.h"
#include "DataFormats/TrackerRecHit2D/interface/SiStripRecHit2D.h"
#include "DataFormats/TrackerRecHit2D/interface/SiStripRecHit1D.h"
#include "DataFormats/TrackerRecHit2D/interface/ProjectedSiStripRecHit2D.h"
#include "DataFormats/TrackerRecHit2D/interface/SiStripMatchedRecHit2D.h"
#include <algorithm>


void 
TrackMixingAssociator::registerTrackEvent(int eid, const reco::TrackCollection &tracks) 
{
    for (reco::TrackCollection::const_iterator it = tracks.begin(), ed = tracks.end(); it != ed; ++it) {
        const reco::Track &tk = *it;
        for (trackingRecHit_iterator ithit = tk.recHitsBegin(), edhit = tk.recHitsEnd(); ithit != edhit; ++ithit) {
            const TrackingRecHit *hit = &**ithit;
            uint32_t detid = hit->geographicalId().rawId();
            allHits_[detid].push_back(HitRecord(eid, hit, &tk));
        }
    }
}

void 
TrackMixingAssociator::registerSeedEvent(int eid, const TrajectorySeedCollection &tracks) 
{
    for (TrajectorySeedCollection::const_iterator it = tracks.begin(), ed = tracks.end(); it != ed; ++it) {
        const TrajectorySeed &tk = *it;
        for (TrajectorySeed::range r = tk.recHits(); r.first != r.second; ++r.first) {
            const TrackingRecHit *hit = &*r.first;
            uint32_t detid = hit->geographicalId().rawId();
            if (typeid(*hit) == typeid(SiStripMatchedRecHit2D)) {
                const SiStripMatchedRecHit2D &mh = static_cast<const SiStripMatchedRecHit2D &>(*hit);
                allSeedHits_[mh.monoHit()->geographicalId().rawId()  ].push_back(SeedRecord(eid, mh.monoHit(),   &tk));
                allSeedHits_[mh.stereoHit()->geographicalId().rawId()].push_back(SeedRecord(eid, mh.stereoHit(), &tk));
            } else if (typeid(*hit) == typeid(ProjectedSiStripRecHit2D)) {
                const ProjectedSiStripRecHit2D &ph = static_cast<const ProjectedSiStripRecHit2D &>(*hit);
                allSeedHits_[ph.originalHit().geographicalId().rawId()].push_back(SeedRecord(eid, &ph.originalHit(), &tk));
            } else {
                allSeedHits_[detid].push_back(SeedRecord(eid, hit, &tk));
            }
        }
    }
}


void 
TrackMixingAssociator::registerClusterEvent(int id, const SiPixelClusterCollection &allPixels, const SiStripClusterCollection &allStrips) 
{
   registerClusters(id, allStrips); 
   registerClusters(id, allPixels); 
}


template<typename T>
void
TrackMixingAssociator::associateHitToRec(const TrackingRecHit *hit, std::vector<RecAssociation<T> > &out, boost::unordered_map<uint32_t, std::vector<RecRecord<T> > > &record) {
    const std::vector<RecRecord<T> > & hitRecords = record[ hit->geographicalId().rawId() ];
    for (typename std::vector<RecRecord<T> >::const_iterator itr = hitRecords.begin(), edr = hitRecords.end(); itr != edr; ++itr) {
        if (matchesRecord(*hit, *itr)) {
            typename std::vector<RecAssociation<T> >::iterator as = std::find(out.begin(), out.end(), itr->track);
            if (as == out.end()) { out.push_back(RecAssociation<T>(itr->eventId, itr->track)); as = out.end() - 1; }
            as->addSharedHit(*hit);
        }
    }
}

template<typename T>
void
TrackMixingAssociator::associateToRec(const reco::Track &tk, std::vector<RecAssociation<T> > &out, boost::unordered_map<uint32_t, std::vector<RecRecord<T> > > &record) 
{
    out.clear();
    for (trackingRecHit_iterator ithit = tk.recHitsBegin(), edhit = tk.recHitsEnd(); ithit != edhit; ++ithit) {
        const TrackingRecHit *hit = &**ithit;
        associateHitToRec<T>(hit,out,record);
        
    }
    std::sort(out.begin(), out.end());
}

template<typename T>
void
TrackMixingAssociator::associateToRec(const TrajectorySeed &tk, std::vector<RecAssociation<T> > &out, boost::unordered_map<uint32_t, std::vector<RecRecord<T> > > &record) 
{
    out.clear();
    for (TrajectorySeed::range r = tk.recHits(); r.first != r.second; ++r.first) {
        const TrackingRecHit *hit = &*r.first;
        if (typeid(*hit) == typeid(SiStripMatchedRecHit2D)) {
            const SiStripMatchedRecHit2D &mh = static_cast<const SiStripMatchedRecHit2D &>(*hit);
            associateHitToRec<T>(mh.monoHit(),out,record);
            associateHitToRec<T>(mh.stereoHit(),out,record);
        } else if (typeid(*hit) == typeid(ProjectedSiStripRecHit2D)) {
            const ProjectedSiStripRecHit2D &ph = static_cast<const ProjectedSiStripRecHit2D &>(*hit);
            associateHitToRec<T>(&ph.originalHit(),out,record);
        } else {
            associateHitToRec<T>(hit,out,record);
        }
    }
    std::sort(out.begin(), out.end());
}


void
TrackMixingAssociator::associateToTracks(const reco::Track &tk, std::vector<TrackAssociation> &out) {
    return associateToRec<reco::Track>(tk,out,allHits_); 
}

void
TrackMixingAssociator::associateToTracks(const TrajectorySeed &tk, std::vector<TrackAssociation> &out) { 
    return associateToRec<reco::Track>(tk,out,allHits_);
}

void
TrackMixingAssociator::associateToSeed(const reco::Track &tk, std::vector<SeedAssociation> &out) { 
    return associateToRec<TrajectorySeed>(tk,out,allSeedHits_); 
}

void
TrackMixingAssociator::associateToSeed(const TrajectorySeed &tk, std::vector<SeedAssociation> &out) { 
    return associateToRec<TrajectorySeed>(tk,out,allSeedHits_); 
} 


void 
TrackMixingAssociator::associateHitToClusters(const TrackingRecHit *hit, std::vector<TrackClusterAssociation> &out) 
{
    const std::vector<ClusterRecord> & clusterRecords = allClusters_[ hit->geographicalId().rawId() ];
    std::vector<int> eventIds;
    int nmatches = 0;
    for (std::vector<ClusterRecord>::const_iterator itr = clusterRecords.begin(), edr = clusterRecords.end(); itr != edr; ++itr) {
        if (matches(*hit, *itr)) { nmatches++; eventIds.push_back(itr->eventId); }
    }
    for (std::vector<int>::const_iterator iti = eventIds.begin(), edi = eventIds.end(); iti != edi; ++iti) {
        std::vector<TrackClusterAssociation>::iterator as = std::find(out.begin(), out.end(), *iti);
        if (as == out.end()) { out.push_back(TrackClusterAssociation(*iti)); as = out.end() - 1; }
        as->addHit(*hit, nmatches == 1);
    }
}

void 
TrackMixingAssociator::associateToClusters(const reco::Track &tk, std::vector<TrackClusterAssociation> &out) 
{
    out.clear();
    for (trackingRecHit_iterator ithit = tk.recHitsBegin(), edhit = tk.recHitsEnd(); ithit != edhit; ++ithit) {
        const TrackingRecHit *hit = &**ithit;
        associateHitToClusters(hit,out);
    }
    std::sort(out.begin(), out.end());
}


void 
TrackMixingAssociator::associateToClusters(const TrajectorySeed &tk, std::vector<TrackClusterAssociation> &out) 
{
    out.clear();
    for (TrajectorySeed::range r = tk.recHits(); r.first != r.second; ++r.first) {
        const TrackingRecHit *hit = &*r.first;
        if (typeid(*hit) == typeid(SiStripMatchedRecHit2D)) {
            const SiStripMatchedRecHit2D &mh = static_cast<const SiStripMatchedRecHit2D &>(*hit);
            associateHitToClusters(mh.monoHit(),out);
            associateHitToClusters(mh.stereoHit(),out);
        } else if (typeid(*hit) == typeid(ProjectedSiStripRecHit2D)) {
            const ProjectedSiStripRecHit2D &ph = static_cast<const ProjectedSiStripRecHit2D &>(*hit);
            associateHitToClusters(&ph.originalHit(),out);
        } else {
            associateHitToClusters(hit,out);
        }
    }
    std::sort(out.begin(), out.end());
}


bool
TrackMixingAssociator::matches(const SiStripCluster &c1, const SiStripCluster &c2) 
{
    // either: 
    //   - c1 begins after c2 begins but before c2 ends
    //   - c2 begins after c1 begins but before c1 ends
    // the rightmost beginning must be on the left of the leftmost ending
    return std::max(c1.firstStrip(),c2.firstStrip()) <= std::min(c1.firstStrip()+c1.amplitudes().size(),c2.firstStrip()+c2.amplitudes().size());
}

bool
TrackMixingAssociator::matches(const SiPixelCluster &c1, const SiPixelCluster &c2)
{
    return ( std::max(c1.minPixelRow(), c2.minPixelRow()) <= std::min(c1.maxPixelRow(), c2.maxPixelRow()) ) && 
           ( std::max(c1.minPixelCol(), c2.minPixelCol()) <= std::min(c1.maxPixelCol(), c2.maxPixelCol()) ) ;
}

template<typename T, typename Record>
bool TrackMixingAssociator::matchesRecordSpecific(const TrackingRecHit &hit, const Record &record) 
{
    if (typeid(hit) == typeid(T) && typeid(T) == typeid(*record.hit)) {
        return matches(*(static_cast<const T &>(hit)).cluster(),
                       *(static_cast<const T &>(*record.hit)).cluster());
    }
    return false;
}

template<typename Record>
bool 
TrackMixingAssociator::matchesRecord(const TrackingRecHit &hit, const Record &record) 
{
    return matchesRecordSpecific<SiStripRecHit2D,Record>(hit,record) ||
           matchesRecordSpecific<SiStripRecHit1D,Record>(hit,record) ||
           matchesRecordSpecific<SiPixelRecHit  ,Record>(hit,record);
}

bool
TrackMixingAssociator::matches(const TrackingRecHit &hit, const ClusterRecord &record) 
{
    if (record.stripCluster != 0 && typeid(hit) == typeid(SiStripRecHit2D)) {
         return matches( *(static_cast<const SiStripRecHit2D &>(hit)).cluster(), *record.stripCluster);
    } else if (record.stripCluster != 0 && typeid(hit) == typeid(SiStripRecHit1D)) {
         return matches( *(static_cast<const SiStripRecHit1D &>(hit)).cluster(), *record.stripCluster);
    } else if (record.pixelCluster != 0 && typeid(hit) == typeid(SiPixelRecHit)) {
         return matches( *(static_cast<const SiPixelRecHit &>(hit)).cluster(), *record.pixelCluster);
    }
    return false;
}

template<typename T>
void TrackMixingAssociator::registerClusters(int eventId, const edmNew::DetSetVector<T> &clusters)
{
    for (typename edmNew::DetSetVector<T>::const_iterator itds = clusters.begin(), edds = clusters.end(); itds != edds; ++itds) {
        typename edmNew::DetSet<T> ds = *itds;
        std::vector<ClusterRecord> & theseClusters = allClusters_[ds.detId()];
        for (typename edmNew::DetSet<T>::const_iterator it = ds.begin(), ed = ds.end(); it != ed; ++it) {
            theseClusters.push_back(ClusterRecord(eventId, *it));
        }
    }
}
