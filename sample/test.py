import json

res = {
        "payload":{
            "Items":[
              {
                  "Identifiers":{
                    "MarketplaceASIN":{
                        "MarketplaceId":"A1VC38T7YXB528",
                        "ASIN":"B079T6CHPV"
                    }
                  },
                  "AttributeSets":[
                    {
                        "Platform":[
                          "Nintendo Switch"
                        ],
                        "Binding":"Video Game",
                        "Brand":"任天堂",
                        "Genre":"ゲーム",
                        "ItemDimensions":{
                          "Height":{
                              "value":13.779527545,
                              "Units":"inches"
                          },
                          "Length":{
                              "value":19.291338563,
                              "Units":"inches"
                          },
                          "Width":{
                              "value":2.755905509,
                              "Units":"inches"
                          },
                          "Weight":{
                              "value":5.2470018356,
                              "Units":"pounds"
                          }
                        },
                        "IsAdultProduct":False,
                        "Label":"任天堂",
                        "ListPrice":{
                          "Amount":7678.0,
                          "CurrencyCode":"JPY"
                        },
                        "Manufacturer":"任天堂",
                        "Model":"HAC-R-ADFUA",
                        "PackageDimensions":{
                          "Height":{
                              "value":2.5199999974296,
                              "Units":"inches"
                          },
                          "Length":{
                              "value":17.8699999817726,
                              "Units":"inches"
                          },
                          "Width":{
                              "value":13.5799999861484,
                              "Units":"inches"
                          },
                          "Weight":{
                              "value":5.31093589158,
                              "Units":"pounds"
                          }
                        },
                        "PackageQuantity":1,
                        "PartNumber":"HAC-R-ADFUA",
                        "PegiRating":"ages_3_and_over",
                        "ProductGroup":"Video Games",
                        "ProductTypeName":"PHYSICAL_VIDEO_GAME_SOFTWARE",
                        "Publisher":"任天堂",
                        "ReleaseDate":"2018-04-20",
                        "Size":"1) Amazon.co.jp限定無し",
                        "SmallImage":{
                          "URL":"https://m.media-amazon.com/images/I/51l2xg5wiDL._SL75_.jpg",
                          "Height":{
                              "Units":"pixels",
                              "value":75
                          },
                          "Width":{
                              "Units":"pixels",
                              "value":75
                          }
                        },
                        "Studio":"任天堂",
                        "Title":"Nintendo Labo (ニンテンドー ラボ) Toy-Con 01: Variety Kit - Switch"
                    }
                  ],
                  "Relationships":[
                    
                  ],
                  "SalesRankings":[
                    {
                        "ProductCategoryId":"video_games_display_on_website",
                        "Rank":834
                    },
                    {
                        "ProductCategoryId":"4731378051",
                        "Rank":209
                    }
                  ]
              }
            ]
        }
      }
def SP_API_FORMATTING(res):
  temp = {
            "Id":{
                "value":""
            },
            "IdType":{
                "value":""
            },
            "status":{
                "value":"Success"
            },
            "Products":{
                "Product":{
                  "Identifiers":{
                      "MarketplaceASIN":{
                        "MarketplaceId":{
                            "value":""
                        },
                        "ASIN":{
                            "value":""
                        }
                      }
                  },
                  "AttributeSets":{
                      "ItemAttributes":{
                        "lang":{
                            "value":"ja-JP"
                        },
                        "Binding":{
                            "value":""
                        },
                        "Brand":{
                            "value":"任天堂"
                        },
                        "CEROAgeRating":{
                            "value":"全年齢対象"
                        },
                        "ESRBAgeRating":{
                            "value":"Everyone"
                        },
                        "Genre":{
                            "value":"ゲーム"
                        },
                        "ItemDimensions":{
                            "Height":{
                              "value":"",
                              "Units":{
                                  "value":""
                              }
                            },
                            "Length":{
                              "value":"19.291338563",
                              "Units":{
                                  "value":"inches"
                              }
                            },
                            "Width":{
                              "value":"2.755905509",
                              "Units":{
                                  "value":"inches"
                              }
                            },
                            "Weight":{
                              "value":"5.2470018356000",
                              "Units":{
                                  "value":"pounds"
                              }
                            }
                        },
                        "IsAdultProduct":{
                            "value":"false"
                        },
                        "Label":{
                            "value":"任天堂"
                        },
                        "ListPrice":{
                            "Amount":{
                              "value":""
                            },
                            "CurrencyCode":{
                              "value":""
                            }
                        },
                        "Manufacturer":{
                            "value":""
                        },
                        "Model":{
                            "value":""
                        },
                        "PackageDimensions":{
                            "Height":{
                              "value":"",
                              "Units":{
                                  "value":""
                              }
                            },
                            "Length":{
                              "value":"",
                              "Units":{
                                  "value":""
                              }
                            },
                            "Width":{
                              "value":"",
                              "Units":{
                                  "value":""
                              }
                            },
                            "Weight":{
                              "value":"",
                              "Units":{
                                  "value":""
                              }
                            }
                        },
                        "PackageQuantity":{
                            "value":"1"
                        },
                        "PartNumber":{
                            "value":""
                        },
                        "PegiRating":{
                            "value":""
                        },
                        "Platform":{
                            "value":""
                        },
                        "ProductGroup":{
                            "value":""
                        },
                        "ProductTypeName":{
                            "value":""
                        },
                        "Publisher":{
                            "value":""
                        },
                        "ReleaseDate":{
                            "value":""
                        },
                        "Size":{
                            "value":""
                        },
                        "SmallImage":{
                            "URL":{
                              "value":"https://m.media-amazon.com/images/I/51l2xg5wiDL._SL75_.jpg"
                            },
                            "Height":{
                              "value":"75",
                              "Units":{
                                  "value":"pixels"
                              }
                            },
                            "Width":{
                              "value":"75",
                              "Units":{
                                  "value":"pixels"
                              }
                            }
                        },
                        "Studio":{
                            "value":""
                        },
                        "Title":{
                            "value":""
                        }
                      }
                  },
                  "Relationships":{
                      
                  },
                  "SalesRankings":{
                      "SalesRank":[
                        {
                            "ProductCategoryId":{
                              "value":""
                            },
                            "Rank":{
                              "value":"1495"
                            }
                        },
                        {
                            "ProductCategoryId":{
                              "value":""
                            },
                            "Rank":{
                              "value":""
                            }
                        }
                      ]
                  }
                }
            }
          }

  #---------Identifiers start
  MarketplaceId = res["payload"]["Items"][0]["Identifiers"]["MarketplaceASIN"]["MarketplaceId"]
  temp["Products"]["Product"]["Identifiers"]["MarketplaceASIN"]["MarketplaceId"]["value"] = MarketplaceId
  ASIN = res["payload"]["Items"][0]["Identifiers"]["MarketplaceASIN"]["ASIN"]
  temp["Products"]["Product"]["Identifiers"]["MarketplaceASIN"]["ASIN"]["value"] = ASIN
  #---------Identifiers end

  #---------AttributeSets start
  Binding = res["payload"]["Items"][0]["AttributeSets"][0]["Binding"]
  temp["Products"]["Product"]["AttributeSets"]["ItemAttributes"]["Binding"]["value"] = Binding
  Brand = res["payload"]["Items"][0]["AttributeSets"][0]["Brand"]
  temp["Products"]["Product"]["AttributeSets"]["ItemAttributes"]["Brand"]["value"] = Brand
  Brand = res["payload"]["Items"][0]["AttributeSets"][0]["Brand"]
  temp["Products"]["Product"]["AttributeSets"]["ItemAttributes"]["Brand"]["value"] = Brand

    #---------ItemDimensions start
  Height = res["payload"]["Items"][0]["AttributeSets"][0]["ItemDimensions"]['Height']['value']
  temp["Products"]["Product"]["AttributeSets"]["ItemAttributes"]["ItemDimensions"]["Height"]["value"] = Height
  Units = res["payload"]["Items"][0]["AttributeSets"][0]["ItemDimensions"]['Height']['Units']
  temp["Products"]["Product"]["AttributeSets"]["ItemAttributes"]["ItemDimensions"]["Height"]["Units"]["value"] = Units

  Length = res["payload"]["Items"][0]["AttributeSets"][0]["ItemDimensions"]['Length']['value']
  temp["Products"]["Product"]["AttributeSets"]["ItemAttributes"]["ItemDimensions"]["Length"]["value"] = Length
  Units = res["payload"]["Items"][0]["AttributeSets"][0]["ItemDimensions"]['Length']['Units']
  temp["Products"]["Product"]["AttributeSets"]["ItemAttributes"]["ItemDimensions"]["Length"]["Units"]["value"] = Units

  Width = res["payload"]["Items"][0]["AttributeSets"][0]["ItemDimensions"]['Width']['value']
  temp["Products"]["Product"]["AttributeSets"]["ItemAttributes"]["ItemDimensions"]["Width"]["value"] = Width
  Units = res["payload"]["Items"][0]["AttributeSets"][0]["ItemDimensions"]['Width']['Units']
  temp["Products"]["Product"]["AttributeSets"]["ItemAttributes"]["ItemDimensions"]["Width"]["Units"]["value"] = Units

  Weight = res["payload"]["Items"][0]["AttributeSets"][0]["ItemDimensions"]['Weight']['value']
  temp["Products"]["Product"]["AttributeSets"]["ItemAttributes"]["ItemDimensions"]["Weight"]["value"] = Weight
  Units = res["payload"]["Items"][0]["AttributeSets"][0]["ItemDimensions"]['Weight']['Units']
  temp["Products"]["Product"]["AttributeSets"]["ItemAttributes"]["ItemDimensions"]["Weight"]["Units"]["value"] = Units
    #---------ItemDimensions end

  Label = res["payload"]["Items"][0]["AttributeSets"][0]["Label"]
  temp["Products"]["Product"]["AttributeSets"]["ItemAttributes"]["Label"]["value"] = Label

  ListPriceAmount = res["payload"]["Items"][0]["AttributeSets"][0]["ListPrice"]["Amount"]
  temp["Products"]["Product"]["AttributeSets"]["ItemAttributes"]["ListPrice"]["Amount"]["value"] = ListPriceAmount
  ListPriceCurrencyCode = res["payload"]["Items"][0]["AttributeSets"][0]["ListPrice"]["CurrencyCode"]
  temp["Products"]["Product"]["AttributeSets"]["ItemAttributes"]["ListPrice"]["CurrencyCode"]["value"] = ListPriceCurrencyCode

  Manufacturer = res["payload"]["Items"][0]["AttributeSets"][0]["Manufacturer"]
  temp["Products"]["Product"]["AttributeSets"]["ItemAttributes"]["Manufacturer"]["value"] = Manufacturer

  Model = res["payload"]["Items"][0]["AttributeSets"][0]["Model"]
  temp["Products"]["Product"]["AttributeSets"]["ItemAttributes"]["Model"]["value"] = Model

    #------------PackageDimensions start
  Height = res["payload"]["Items"][0]["AttributeSets"][0]["PackageDimensions"]['Height']['value']
  temp["Products"]["Product"]["AttributeSets"]["ItemAttributes"]["PackageDimensions"]["Height"]["value"] = Height
  Units = res["payload"]["Items"][0]["AttributeSets"][0]["PackageDimensions"]['Height']['Units']
  temp["Products"]["Product"]["AttributeSets"]["ItemAttributes"]["PackageDimensions"]["Height"]["Units"]["value"] = Units

  Length = res["payload"]["Items"][0]["AttributeSets"][0]["PackageDimensions"]['Length']['value']
  temp["Products"]["Product"]["AttributeSets"]["ItemAttributes"]["PackageDimensions"]["Length"]["value"] = Length
  Units = res["payload"]["Items"][0]["AttributeSets"][0]["PackageDimensions"]['Length']['Units']
  temp["Products"]["Product"]["AttributeSets"]["ItemAttributes"]["PackageDimensions"]["Length"]["Units"]["value"] = Units

  Width = res["payload"]["Items"][0]["AttributeSets"][0]["PackageDimensions"]['Width']['value']
  temp["Products"]["Product"]["AttributeSets"]["ItemAttributes"]["PackageDimensions"]["Width"]["value"] = Width
  Units = res["payload"]["Items"][0]["AttributeSets"][0]["PackageDimensions"]['Width']['Units']
  temp["Products"]["Product"]["AttributeSets"]["ItemAttributes"]["PackageDimensions"]["Width"]["Units"]["value"] = Units

  Weight = res["payload"]["Items"][0]["AttributeSets"][0]["PackageDimensions"]['Weight']['value']
  temp["Products"]["Product"]["AttributeSets"]["ItemAttributes"]["PackageDimensions"]["Weight"]["value"] = Weight
  Units = res["payload"]["Items"][0]["AttributeSets"][0]["PackageDimensions"]['Weight']['Units']
  temp["Products"]["Product"]["AttributeSets"]["ItemAttributes"]["PackageDimensions"]["Weight"]["Units"]["value"] = Units
    #------------PackageDimensions end

  PackageQuantity = res["payload"]["Items"][0]["AttributeSets"][0]["PackageQuantity"]
  temp["Products"]["Product"]["AttributeSets"]["ItemAttributes"]["PackageQuantity"]["value"] = PackageQuantity

  PartNumber = res["payload"]["Items"][0]["AttributeSets"][0]["PartNumber"]
  temp["Products"]["Product"]["AttributeSets"]["ItemAttributes"]["PartNumber"]["value"] = PartNumber

  PegiRating = res["payload"]["Items"][0]["AttributeSets"][0]["PegiRating"]
  temp["Products"]["Product"]["AttributeSets"]["ItemAttributes"]["PegiRating"]["value"] = PegiRating

  Platform = res["payload"]["Items"][0]["AttributeSets"][0]["Platform"]
  temp["Products"]["Product"]["AttributeSets"]["ItemAttributes"]["Platform"]["value"] = Platform

  ProductGroup = res["payload"]["Items"][0]["AttributeSets"][0]["ProductGroup"]
  temp["Products"]["Product"]["AttributeSets"]["ItemAttributes"]["ProductGroup"]["value"] = ProductGroup

  ProductTypeName = res["payload"]["Items"][0]["AttributeSets"][0]["ProductTypeName"]
  temp["Products"]["Product"]["AttributeSets"]["ItemAttributes"]["ProductTypeName"]["value"] = ProductTypeName

  Publisher = res["payload"]["Items"][0]["AttributeSets"][0]["Publisher"]
  temp["Products"]["Product"]["AttributeSets"]["ItemAttributes"]["Publisher"]["value"] = Publisher

  Size = res["payload"]["Items"][0]["AttributeSets"][0]["Size"]
  temp["Products"]["Product"]["AttributeSets"]["ItemAttributes"]["Size"]["value"] = Size

  Studio = res["payload"]["Items"][0]["AttributeSets"][0]["Studio"]
  temp["Products"]["Product"]["AttributeSets"]["ItemAttributes"]["Studio"]["value"] = Studio

  Title = res["payload"]["Items"][0]["AttributeSets"][0]["Title"]
  temp["Products"]["Product"]["AttributeSets"]["ItemAttributes"]["Title"]["value"] = Title

  #----------SalesRankings
  productcategoryId1 = res["payload"]["Items"][0]["SalesRankings"][0]["ProductCategoryId"]
  temp["Products"]["Product"]["SalesRankings"]["SalesRank"][0]["ProductCategoryId"]["value"] = productcategoryId1
  Rank1 = res["payload"]["Items"][0]["SalesRankings"][0]["Rank"]
  temp["Products"]["Product"]["SalesRankings"]["SalesRank"][0]["Rank"]["value"] = Rank1

  productcategoryId1 = res["payload"]["Items"][0]["SalesRankings"][1]["ProductCategoryId"]
  temp["Products"]["Product"]["SalesRankings"]["SalesRank"][1]["ProductCategoryId"]["value"] = productcategoryId1
  Rank1 = res["payload"]["Items"][0]["SalesRankings"][1]["Rank"]
  temp["Products"]["Product"]["SalesRankings"]["SalesRank"][1]["Rank"]["value"] = Rank1

  return temp


