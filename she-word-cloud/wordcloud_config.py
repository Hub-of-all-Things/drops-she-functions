#
# DROPS project
#
# Ming-Wei Hsu
# 
import json

def lambda_handler(event, context):

    config = {
        "id": "twitter-word-cloud",
        "info": {
            "version": "1.0.0",
            "versionReleaseDate": "2018-11-27T12:00:00.000Z",
            "name": "Word Cloud",
            "headline": "A word cloud of your tweets",
            "description": {
                "text": "Word Cloud generates a word cloud from your tweets in the past week. "
            },
            "termsUrl": "https://hatdex.org/terms-of-service-hat-owner-agreement",
            "supportContact": "Ming-Wei.Hsu@uwe.ac.uk",
            "graphics": {
                "banner": {
                    "normal": ""
                },
                "logo": {
                    "normal": ""
                },
                "screenshots": [
                    {
                        "normal": ""
                    },
                    {
                        "normal": ""
                    }
                ]
            },
            "dataPreviewEndpoint": "/she/feed/she/twitter/word-cloud"
        },
        "developer": {
            "id": "drops",
            "name": "DROPS project",
            "url": "https://www.hatcommunity.org/about-drops/",
            "country": "United Kingdom"
        },
        "trigger": {
            "triggerType": "individual"
        },
        "dataBundle": {
            "name": "twitter-word-cloud",
            "bundle": {
                "twitter/tweets": {
                    "endpoints": [
                        {
                            "endpoint": "twitter/tweets",
                            "mapping": {
                                "id": "id_str"
                            }
                        }
                    ],
                    "orderBy": "lastUpdated",
                    "ordering": "descending"
                }
            }
        },
        "status": {
            "available": True,
            "enabled": False
        }
    }

    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(config)
    }