import requests
from bs4 import BeautifulSoup


PRODUCT_URL = 'https://www.amazon.co.uk/Sony-WF-C500-Wireless-Headphones-Built-Black/dp/B09FKGJ1CB/ref' \
              '=d_bmx_dp_cdjieemo_sccl_1_3/262-3215502-2054313?pd_rd_w=FKNxO&content-id=amzn1.sym.89757917-7d86-4c30' \
              '-a82b-c76fe5b7d5a8&pf_rd_p=89757917-7d86-4c30-a82b-c76fe5b7d5a8&pf_rd_r=TARPZPHAE320QRPATHHF&pd_rd_wg' \
              '=IfoOi&pd_rd_r=803fa2a6-3285-459c-8eb4-842b3262332c&pd_rd_i=B09FKGJ1CB&th=1'

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 ' \
             'Safari/537.36 Edg/110.0.1587.41'

if __name__ == '__main__':

    headers = {'user-agent': USER_AGENT}

    response = requests.get(PRODUCT_URL, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    main_price = float(soup.find(
        name='div', id='corePriceDisplay_desktop_feature_div'
    ).select('.a-offscreen')[0].getText().removeprefix('£'))
    print(main_price)

