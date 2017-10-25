#!/usr/bin/env ash
curl 'https://services.nutanix.com/v1/design/215731/workloads' \
    -H '.nutanix.com' \
    -H 'Accept-Encoding: gzip, deflate, br' \
    -H 'Accept-Language: en-US,en;q=0.8,fr-FR;q=0.6,fr;q=0.4,es;q=0.2' \
    -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36' \
    -H 'Content-Type: application/json' \
    -H 'Accept: application/json' \
    -H 'Referer: https://services.nutanix.com/swagger-ui.html' \
    -H 'Cookie: CID=BgAAANGVtk1DHmGcQ1OnfDzU9b8=; _mkto_trk=id:031-GVQ-112&token:_mch-nutanix.com-1497883604553-44707; NG_TRANSLATE_LANG_KEY=%22en%22; JSESSIONID=0A216053C9BDB91CFD8A78B4D9100FD3; AWSELB=0D374F751E67CD3215D1CF685B75AF7C45B28C3ADF1F8915BB4B07CD8A6A2695A7D5FC42B52D30A6469760D2557AC7CBDD8A94E4E26CDCFCCBA34AA0758F383EB0D953B5D6B0CA6946AF0A38D579434BA06A400FFA; isSso=false' \
    -H 'Connection: keep-alive' \
    -H 'DNT: 1' \
    --data-binary $'{\n    "data" :\n    {\n        "RAM" : 0.954,\n        "mhz" : 466,\n        "type" : "serverVirtualization",\n        "nPlus" : 1,\n        "dedupe" : 0,\n        "cluster" : null,\n        "hotData" : 0.632,\n        "coldData" : 5.684,\n        "corePerVm" : 1,\n        "sizeByMHz" : false,\n        "editWLMode" : "ADD_WL_FLOW",\n        "compression" :\n        {\n            "enabledForAF" : true,\n            "preCompressed" : false,\n            "enabledForHybrid" : true,\n            "containerCompression" : 50\n        },\n        "containerRF" : 2,\n        "numberOfVMs" : 5,\n        "enabledForAF" : false,\n        "vCPUsPerCore" : 6,\n        "workloadName" : "Small CPU Small RAM 3",\n        "erasureCoding" : false,\n        "preCompressed" : null,\n        "remoteCluster" : null,\n        "targetCluster" : "No",\n        "totalCapacity" : 6.315,\n        "blockAwareness" : "0",\n        "enabledForHybrid" : false,\n        "encryptedStorage" : "0",\n        "remoteReplication" : null,\n        "serverProfileType" : "Small",\n        "targetClusterName" : "",\n        "availabilityDomain" : "1",\n        "containerCompression" : null,\n        "dedicatedClusterNewName" : null\n    }\n}' \
    --compressed
