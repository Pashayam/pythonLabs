

def сondition():
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
        return options[option]


def start():
    print(
       'Это симулятор утки-маляра\n'
       'Вы хотите погулять. Пойдете ли вы гулять?')
    if сondition():
        return walk()
    return home()


def umbrella():
    print('Вы взяли зонтик и пошли гулять. На улице начался дождь.'
          'Вы раскрыли зонтик и пошли дальше. На вашем пути встретилась кофейня. Зайти в кофейню?')
    if сondition():
        return coffee_house()
    return no_coffee_house()


def no_umbrella():
    print('Вы пошли гулять без зонтика и на улице начался дождь.'
          'Кажется надо идти домой. Перед вами стоит выбор побежать или спокойно пойти домой. Вы хотите побежать?')
    if сondition():
        return run()
    return no_run()


def coffee_house():
    print('Вы взяли кофе и переждали дождь в кофейне.'
          'Теперь встал выбор пойти гулять дальше или пойти домой. Идем дальше гулять?')
    if сondition():
        return go_walk()
    return no_coffee_house()


def no_coffee_house():
    print('Вы вернулись домй и довольны прогулкой. Конец.')


def go_walk():
    print('Гуляя вы увидели деньги лежащие на дороге. Подобрать деньги?')
    if сondition():
        return take_money()
    return no_take_money()


def take_money():
    print('Вы подобрали деньги и пошли домой. Придя домой вы поняли, что это были фальшивые деньги. Конец.')
    return


def no_take_money():
    print('Вы решили не подбирать деньги и пошли домой. '
          'Вы уставший после такой долгой прогули сразу легли спать. Конец.')
    return


def run():
    print('Вы побежали домой. Вы случайно подскользнулись на ступеньке, упали и потеряли сознание.'
          ' Ваше бессознательное тело отвезли в больницу. Конец. ')
    return


def no_run():
    print('Придя домой вы поняли, что замерли и решили сделать себе горячий чай. Конец.')
    return


def home():
    print('Вы решили никуда не идти и остаться дома. Конец.')
    return


def walk():
    print(
        'Вы готовитесь к выходу. Возьмете ли вы зонтик?'
    )
    if сondition():
        return umbrella()
    return no_umbrella()


if __name__ == "__main__":
    start()