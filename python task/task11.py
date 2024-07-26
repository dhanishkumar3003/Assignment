def get_number(product_id):
    ans=0
    for i in product_id:
        if i.isdigit():
            ans=ans*10+int(i)
    return ans
def main(product_ids):
    reduced_ids = list(map(lambda x: get_number(x), product_ids))
    print("Reduced value:", reduced_ids)

if __name__ == "__main__":
    product_ids = ['H1EM-234', 'HEM-123', 'HEM-566']
    main(product_ids)
