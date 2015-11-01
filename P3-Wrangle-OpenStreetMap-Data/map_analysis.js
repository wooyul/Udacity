//Number of entries
db.sfmap.find().count()

//Number of unique users.
db.sfmap.distinct("created.user")

//Number of unique type
db.sfmap.distinct("type")

//Number of unique 
db.sfmap.aggregate(
[
    {$match : {"created.user" : {"$exists" : true}}},
    {$group: {"_id" : "$created.user" ,"count" : {"$sum":1}}},
    {$sort : {"count" : -1}}
]
)
//Number of nodes with amenity
db.sfmap.find({"amenity" : {"$exists" : true}})

//Group by amenity
db.sfmap.aggregate(
[
    {$match : {"amenity" : {"$exists" : true}}},
    {$project: {"amenity" : "$amenity"}},
    {$group: {"_id" : "$amenity" ,"count" : {"$sum":1}}},
    {$sort : {"count" : -1}}
]
)
    
