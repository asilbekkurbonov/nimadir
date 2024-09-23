def ortacha_ball(baholar):
    ortacha_baho = {}
    for talaba, ballar in baholar.items():
        ortacha = sum(ballar) / len(ballar)
        ortacha_baho[talaba] = ortacha
    return ortacha_baho

baholar = {
    'Ali': [85, 90, 78],
    'Vali': [88, 92, 85],
    'Sami': [75, 80, 72],
    'Husan': [95, 85, 90]
}

yangi_dict = ortacha_ball(baholar)
print(yangi_dict)