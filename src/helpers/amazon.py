from bs4 import BeautifulSoup

def find_product_table_data(html):
    soup = BeautifulSoup(html, "html.parser")
    product_data = soup.find('div', id='prodDetails')
    if product_data is None:
        return []
    table = product_data.find('table')
    columns = [f"{x.text}".strip() for x in table.find_all('th')]
    table_data=[]
    for i, row in enumerate(table.find_all('tr')):  # [1:] to skip the header row
        # Get all cells in the row
        cells = row.find_all('td')
        # Create a dictionary for the current row, mapping header to cell data
        row_data = {columns[i]: f'{cell.text}'.strip() for cell in cells}
        # Add the dictionary to your list
        table_data.append(row_data)
    return table_data


def find_product_rating(html):
    soup = BeautifulSoup(html, "html.parser")
    average_rating = soup.find(id='averageCustomerReviews').find_all("span", class_='a-size-base')[0].text.strip()
    average_rating = "".join([x for x in f"{average_rating}".strip() if x.isdigit() or x == '.'])
    average_rating = float(average_rating)
    rating_data = soup.find(id='acrCustomerReviewText').text
    rating_count = int(''.join([x for x in rating_data if x.isdigit()]))
    rating_count
    return {
        'average': average_rating,
        'count': rating_count,
    }

def extract_amazon_product_data(html):
    soup = BeautifulSoup(html, "html.parser")
    productTitle = soup.find('span', id='productTitle')
    productTitleText = f"{productTitle.text}".strip()
    productPrice = soup.find_all('span', class_='a-price-whole')[0]
    productPrice = f"{productPrice.text}".strip()
    productPriceText = "".join([x for x in productPrice if x.isdigit() or x == '.'])
    productPriceNum = float(productPriceText)
    try:
        productDescription = soup.find('div', id='productDescription').text
    except:
        productDescription = ''
    featureBullets = soup.find('div', id='feature-bullets').text
    asin = ''
    metadata_items = find_product_table_data(html)
    for data in metadata_items:
        if data.get("ASIN") is None:
            continue
        else:
            asin = data.get("ASIN")
            break
    return {
        'asin': asin,
        'title': productTitleText,
        'price_raw': productPrice,
        'price_text': productPriceText,
        'price': productPriceNum,
        'metadata': metadata_items,
        'description': productDescription,
        'feature_bullets': featureBullets,
        'rating': find_product_rating(html)
    }