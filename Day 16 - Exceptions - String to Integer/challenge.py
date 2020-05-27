if __name__ == '__main__':
    S = input().strip()

    try:
        numeric_value = int(S)
        print(numeric_value)
    except:
        print('Bad String')
