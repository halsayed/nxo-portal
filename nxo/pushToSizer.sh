#!/usr/bin/env ash
curl 'https://services.nutanix.com/v1/design/215731/workloads' \
    -H '.nutanix.com' \
    -H 'Accept-Encoding: gzip, deflate, br' \
    -H 'Accept-Language: en-US,en;q=0.8,fr-FR;q=0.6,fr;q=0.4,es;q=0.2' \
    -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36' \
    -H 'Content-Type: application/json' \
    -H 'Accept: application/json' \
    -H 'Referer: https://services.nutanix.com/swagger-ui.html' \
    -H 'Cookie: CID=BgAAANGVtk1DHmGcQ1OnfDzU9b8=; _mkto_trk=id:031-GVQ-112&token:_mch-nutanix.com-1497883604553-44707; NG_TRANSLATE_LANG_KEY=%22en%22; JSESSIONID=1A8CF9D9456551B7CF481E9BE80AE264; AWSELB=0D374F751E67CD3215D1CF685B75AF7C45B28C3ADF32B887E2A21E20EB2502D14E8A6829AFDA06FA0C901059BE700EA1E69A52247C5E96CB4CAE721EAAADCCFD60E0AFAA12D85E7A120A83BB8105AA1574C72CC1D7; isSso=false' \
    -H 'Connection: keep-alive' \
    -H 'DNT: 1' \
    --compressed \
    --data-binary "@/data/payload.json"
