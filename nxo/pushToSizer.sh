#!/usr/bin/env ash
curl 'https://services.nutanix.com/v1/design/215731/workloads' \
    -H '.nutanix.com' \
    -H 'Accept-Encoding: gzip, deflate, br' \
    -H 'Accept-Language: en-US,en;q=0.8,fr-FR;q=0.6,fr;q=0.4,es;q=0.2' \
    -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36' \
    -H 'Content-Type: application/json' \
    -H 'Accept: application/json' \
    -H 'Referer: https://services.nutanix.com/swagger-ui.html' \
    -H 'Cookie: _ga=GA1.2.1516369824.1481734003; __insp_wid=1064621746; __insp_slim=1481734006273; __insp_nv=true; __insp_targlpu=https%3A%2F%2Fwww.nutanix.com%2Fpartners%2Fbecome-partner-oem%2F; __insp_targlpt=Become%20a%20Partner%20OEM%20-%20Nutanix; _mkto_trk=id:031-GVQ-112&token:_mch-nutanix.com-1481734006382-30359; __insp_norec_sess=true; _ga=GA1.3.111948247.1481732649; _gid=GA1.3.1170185597.1508968642; NG_TRANSLATE_LANG_KEY=%22en%22; _bizo_bzid=dc74111c-cfd8-46f2-acd5-218d5c083267; _bizo_cksm=B614E2370026F7B6; _bizo_np_stats=155%3D329%2C; JSESSIONID=BE1335F7D4D6103BAE95C8C83F9302D7; AWSELB=0D374F751E67CD3215D1CF685B75AF7C45B28C3ADFACD7ED7879A97368D45B127E4AFAD8234A8CA99B4514AA46839CD79307F0D3685E96CB4CAE721EAAADCCFD60E0AFAA129CE759B74ADBBF19035B8F5A7823B8F9; isSso=false' \
    -H 'Connection: keep-alive' \
    -H 'DNT: 1' \
    --compressed \
    --data-binary "@/data/payload.json"
