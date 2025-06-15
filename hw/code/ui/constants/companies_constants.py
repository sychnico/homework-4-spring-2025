class CampaignConstants:
    URL = 'https://ads.vk.com/hq/dashboard/ad_plans'
    SITE_URL = 'https://education.vk.company/'
    URL_TEXT = 'education.vk.company'
    TITLE = 'Заголовок'
    class Tabs:
        TARGET = ['Сайт', 'Каталог товаров', 'Мобильное приложение', 'Сообщество и профиль',
                 'Группа и профиль ОК', 'Дзен', 'Лид-формы и опросы', 'VK Mini Apps и игры', 'Музыка',
                 'Видео и трансляции']
        
        RECOGNITION = ['Баннерная реклама', 'Видеореклама', 'Реклама в Дзене', 'HTML5 баннер',
                      'Премиальное размещение']
        
        CAMPAIGN = ['Кампании', 'Группы', 'Объявления']

    class Sections:
        NAMES = ['Регионы показа', 'Демография', 'Интересы и поведение', 'Устройства', 'Аудитории',
                'Параметры URL', 'Места размещения']
        REGIONS = ['Россия', 'Москва', 'Санкт-Петербург']

    class Demography:
        MIN_AGE = '16'
        MAX_AGE = '68'
        PEGI = '16+'

    class Targeting:
        SELECTED_REGION = 'Россия'
        INTEREST = 'Автобарахолка'
        STOP_INTEREST = 'Авто премиум класс'
        ACTION = 'Показы рекламы'
        STRATEGY = 'Минимальная цена' 