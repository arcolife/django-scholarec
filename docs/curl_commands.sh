#!/bin/sh

# curl -XGET 'http://localhost:9200/_all/_search?pretty' -d '{
#   "facets": {
#     "terms": {
#       "terms": {
#         "field": "_type",
#         "size": 100,
#         "order": "count",
#         "exclude": []
#       },
#       "facet_filter": {
#         "fquery": {
#           "query": {
#             "filtered": {
#               "query": {
#                 "bool": {
#                   "should": [
#                     {
#                       "query_string": {
#                         "query": "*"
#                       }
#                     }
#                   ]
#                 }
#               },
#               "filter": {
#                 "bool": {
#                   "must": [
#                     {
#                       "match_all": {}
#                     }
#                   ]
#                 }
#               }
#             }
#           }
#         }
#       }
#     }
#   },
#   "size": 0
# }'


curl -XGET 'http://localhost:9200/_all/_search?pretty' -d '{
  "facets": {
    "terms": {
      "terms": {
        "field": "published",
        "size": 50,
        "order": "count",
        "exclude": []
      },
      "facet_filter": {
        "fquery": {
          "query": {
            "filtered": {
              "query": {
                "bool": {
                  "should": [
                    {
                      "query_string": {
                        "query": "*"
                      }
                    }
                  ]
                }
              },
              "filter": {
                "bool": {
                  "must": [
                    {
                      "match_all": {}
                    }
                  ]
                }
              }
            }
          }
        }
      }
    }
  },
  "size": 0
}'
