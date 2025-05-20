
from selenium.webdriver.common.by import By

class CampaignPageLocators:
    CREATE_BUTTON = (
        By.XPATH,
        "//*[@data-testid='create-button']",
    )

    NAME_SIGN = (By.XPATH, "//*[contains(@class, 'EditableTitle_container__')]")
    NAME_EDIT = (By.XPATH, "//*[contains(@class, 'EditableTitle_container__')]//textarea")
    SUBMIT_NAME = (By.XPATH, "//*[contains(@class, 'EditableTitle_container__')]//svg")

    @staticmethod
    def NAME_CONTENT(name):
        return (By.XPATH, f"//*[contains(@class, 'EditableTitle_container__')]//*[text()='{name}]")

    TARGET_TABS = (By.XPATH, "//*[contains(@class, 'ObjectiveTabs_tabItemContent__') and text()='Целевые действия']")

    RECOGNITION_TABS = (
        By.XPATH, "//*[contains(@class, 'ObjectiveTabs_tabItemContent__') and text()='Узнаваемость и охват']")

    TARGET_TABS_SIGN = (By.XPATH, "//*[contains(@class, 'FormItem_topText__') and text()='Что будете рекламировать?']")

    RECOGNITION_TABS_SIGN = (
        By.XPATH, "//*[contains(@class, 'FormItem_topText__') and text()='Какой формат будете использовать?']")

    @staticmethod
    def CATEGORY_CELL(sign):
        return (By.XPATH, f"//*[text()='{sign}']")

    SITE_NAME_INPUT = (
        By.XPATH,
        "//*[contains(@class, 'vkuiFormItem') and .//*[contains(@class, 'FormItem_topText__') and text()='Рекламируемый сайт']]//input",
    )

    @staticmethod
    def ERROR_SITE_NAME(error):
        return (By.XPATH, f"//*[contains(@class, 'vkuiFormItem')]//*[text()='{error}']")

    BANNER = (By.XPATH, "//*[contains(@class, 'formBanner_container__')]//*[text()='Пиксель не установлен']")
    POKAZ = (By.XPATH, f"//*[text()='Показы рекламы']")
    TARGET_ACTION_SELECT = (By.XPATH, "//*[@data-testid='priced-goal']")

    @staticmethod
    def DROPDOWN_OPTIONS(content):
        return (By.XPATH, f"//*[text()='{content}']")

    SWITCH = (By.XPATH, "//*[contains(@class, 'BudgetOptimization_switch__')]")

    STRATEGY_ACTION_SELECT = (By.XPATH, "//*[contains(@data-testid, 'autobidding-mode')]")

    BUDGET_INPUT = (By.XPATH, "//*[@data-testid='targeting-not-set']")

    BUDGET_PERIOD_SELECT = (By.XPATH, "//*[@data-testid='budget']")

    START_DATE = (By.XPATH, "//*[@data-testid='start-date']")

    END_DATE = (By.XPATH, "//*[@data-testid='end-date']")

    CREATE_FOOTER = (By.XPATH, "//*[contains(@class, 'CreateFooter_footer__')]")
    CREATE_FOOTER_CONTINUE = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text() = 'Продолжить']")
    CREATE_FOOTER_PUBLISH = (By.XPATH,
                             "//*[contains(@class, 'CreateFooter_footer__')]//*[contains(@class, 'vkuiButton__content') and text() = 'Опубликовать']")

    @staticmethod
    def SECTION(name):
        return (By.XPATH, f"//*[contains(@class, 'GroupForm_groupHeader__')]//*[text()='{name}']")

    @staticmethod
    def REGION_BUTTON(region):
        return (By.XPATH, f"//*[contains(@class, 'vkuiButton__content') and text()='{region}']")

    @staticmethod
    def AGE_SELECT_CHECK(age):
        return (By.XPATH, f"//*[contains(@class, 'vkuiFormField')]//*[text()='{age}']")

    @staticmethod
    def AGE_SELECT_INPUT(age):
        return (By.XPATH, f"//*[contains(@class, 'vkuiFormField') and .//*[text()='{age}']]//input")

    PEGI_AGE_SELECT = (By.XPATH, "//*[contains(@class, 'vkuiTypography') and text()='0+']")

    INTEREST_SUBSECTION = (By.XPATH, "//*[contains(@class, 'InterestsSubSection_headerText__')]")
    INTEREST_SELECT = (By.XPATH, "//*[@data-name='interests']//input")

    STOP_INTEREST_OPENER = (By.XPATH, "//*[contains(@class, 'Interests_negativeOpener__')]")

    STOP_INTEREST_SELECT = (By.XPATH,
                            "//*[contains(@class, 'vkuiFormItem') and .//*[contains(@class, 'vkuiTypography') and text()='Исключая интересы']]//input")

    CLOSE_DROPDOWN_BUTTON = (By.XPATH, "//*[@data-name='interests']//*[contains(@class, 'vkuiChipsSelect__dropdown')]")

    DESKTOP_CHECKBOX = (By.XPATH, "//*[contains(@class, 'vkuiTypography') and text()='Десктопные']")
    MOBILE_CHECKBOX = (By.XPATH, "//*[contains(@class, 'vkuiTypography') and text()='Мобильные']")

    UPLOAD_AVATAR = (By.XPATH, "//*[contains(@class, 'UploadMediaButton_buttonLogoIcon__')]")

    TITLE_LABEL = (By.XPATH, "//span[contains(@class, 'FormItem_topText__') and text()='Заголовок']")
    TITLE_INPUT = (By.XPATH,
                   "//span[contains(@class, 'vkuiFormField--sizeY-compact')]//div//div[contains(@data-testid, 'заголовок, макс. 40 символов')]")
    SHORT_DESCRIPTION = (
        By.XPATH, "//*[contains(@class, 'FormItem_topText__') and text()='Короткое описание']")
    SHORT_DESCRIPTION_INPUT = (By.XPATH,
                               "//span[contains(@class, 'vkuiFormField--sizeY-compact')]//div//div[contains(@data-testid, 'описание, макс. 90 символов')]")
    SHORT_DESCRIPTION_TEXT = (By.XPATH,
                              "//span[contains(@class, 'vkuiFormField--sizeY-compact')]//div//div[contains(@data-testid, 'описание, макс. 90 символов')]//p")
    LONG_DESCRIPTION = (By.XPATH, "//*[contains(@class, 'FormItem_topText__') and text()='Длинное описание']")
    LONG_DESCRIPTION_INPUT = (By.XPATH,
                              "//span[contains(@class, 'vkuiFormField--sizeY-compact')]//div//div[contains(@data-testid, 'Длинный текст для использования в лентах соцсетей (2000 знаков)')]")
    LONG_DESCRIPTION_TEXT = (By.XPATH,
                             "//span[contains(@class, 'vkuiFormField--sizeY-compact')]//div//div[contains(@data-testid, 'Длинный текст для использования в лентах соцсетей (2000 знаков)')]//p")

    BUTTON_TEXT = (
        By.XPATH, "//*[contains(@class, 'FormItem_topText__') and text()='Текст рядом с кнопкой']")
    BUTTON_TEXT_INPUT = (By.XPATH,
                         "//span[contains(@class, 'vkuiFormField--sizeY-compact')]//div//div[contains(@data-testid, 'Доп. заголовок 30 знаков')]")
    ADVERTISER_DESCRIPTION = (
        By.XPATH, "//*[contains(@class, 'FormItem_topText__') and text()='О рекламодателе']")
    ADVERTISER_DESCRIPTION_INPUT = (By.XPATH,
                                    "//span[contains(@class, 'vkuiFormField--sizeY-compact')]//div//div[contains(@data-testid, 'юридическая информация, макс. 115 символов')]")
    ADVERTISER_DESCRIPTION_TEXT = (By.XPATH,
                                   "//span[contains(@class, 'vkuiFormField--sizeY-compact')]//div//div[contains(@data-testid, 'юридическая информация, макс. 115 символов')]//p")
    MEDIATEC = (By.XPATH, "//*[text()='Медиатека']")
    CORARI = (By.XPATH, "//*[contains(@class, 'AdMediaPreview_autogenIcon__')]")
    IMAGE_ITEM = (By.XPATH, "//*[contains(@class, 'ImageItem_imageItem__')]")
    PREVIEW_IMAGE = (By.XPATH, "//*[contains(@class, 'AdMediaPreview_preview__')]")
    SUBMIT_BUTTON = (By.XPATH, "//*[@data-testid='submit']")
    CANCEL_BUTTON = (By.XPATH, "//button[@data-testid='cancel']")
    CONFIRM_CANCEL_BUTTON = (
        By.XPATH, "//div[contains(@class, 'ModalConfirm_buttons__')]//button[@data-testid='cancel']")

    MEDIA_CONTENT_LIST = (By.XPATH, "//*[contains(@class, 'MediaContentList_flexContainer__')]")

    CHECKBOX_ALL = (By.XPATH, "//*[contains(@class, 'BaseTable__header')]//*[contains(@class, 'vkuiCheckbox')]")

    @staticmethod
    def ADS_PAGE_TABS(name):
        return (By.XPATH, f"//*[@data-testid='tab-items']//*[text()='{name}']")

    ACTION_SELECT = (By.XPATH, "//*[@data-testid='select-options']")

    EDIT_TAPPABLE = (By.XPATH, "//*[contains(@class, 'vkuiTypography') and text()='Редактировать']")

    @staticmethod
    def BUDGET_CELL(amount):
        return (By.XPATH, f"//*[contains(@class, 'budget_editable__')]//div[contains(text(), '{amount}')]")

    @staticmethod
    def ACTION_CELL(action):
        return (By.XPATH, f"//*[contains(@class, 'objectiveCell_title__') and text()='{action}']")

    EDIT_CELL_TAPABLE = (By.XPATH, "//*[@data-testid='edit']")

    @staticmethod
    def ENTITY_NAME_TITLE(name):
        return (By.XPATH, f"//*[contains(@class, 'EditableTitle_container__')]//*[text()='{name}']")

    @staticmethod
    def ENTITY_NAME_CELL(name):
        return (By.XPATH, f"//button[contains(@class, 'nameCellContent_link__') and text()='{name}']")

    PEGI_16_AGE_SELECT = (By.XPATH, "//*[contains(@class, 'vkuiTypography') and text()='16+']")

    @staticmethod
    def CHECKBOX_NAME_IS_CHECKED_OR_NOT(checkbox, state):
        return (
            By.XPATH,
            f"//*[contains(@class, 'vkuiCheckbox') and .//* [contains(@class, 'vkuiTypography') and text()='{checkbox}']]//*[contains(@class, 'vkuiCheckbox__icon--{state}')]",
        )

    AVATAR_IMAGE = (By.XPATH, "//*[contains(@class, 'AdMediaPreview_img__')]")

    MODAL_SEND_BUTTON = (By.XPATH,
                         "//*[contains(@class, 'vkuiModalCard')]//*[contains(@class, 'vkuiButton__content') and text()='Отправить']")
    MODAL_CANCEL_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'vkuiModalCard')]//*[contains(@class, 'vkuiButton__content') and text()='Отмена']")

    @staticmethod
    def SIDEBAR_SITE_NAME_INPUT(url):
        return (
            By.XPATH,
            f"//*[contains(@class, 'vkuiFormItem') and .//*[contains(@class, 'FormItem_topText__') and text()='Рекламируемый сайт']]//*[text()='{url}']",
        )

    @staticmethod
    def SIDEBAR_ACTION_SELECT(action):
        return (
            By.XPATH,
            f"//*[contains(@class, 'vkuiFormItem') and .//*[contains(@class, 'FormItem_topText__') and text()='Целевое действие']]//*[text()='{action}']",
        )

    @staticmethod
    def SIDEBAR_STRATEGY_SELECT(strategy):
        return (
            By.XPATH,
            f"//*[contains(@class, 'vkuiFormItem') and .//*[contains(@class, 'FormItem_topText__') and text()='Стратегия ставок']]//*[text()='{strategy}']",
        )

    @staticmethod
    def SIDEBAR_BUDGET_SELECT(value):
        return (
            By.XPATH,
            f"//*[contains(@class, 'vkuiFormItem') and .//*[contains(@class, 'FormItem_topText__') and text()='Бюджет']]//*[text()='{value}']",
        )

    @staticmethod
    def SIDEBAR_BUDGET_INPUT(value):
        return (
            By.XPATH,
            f"//*[contains(@class, 'vkuiFormItem') and .//*[contains(@class, 'FormItem_topText__') and text()='Бюджет']]//input[@value='{value}']",
        )

    @staticmethod
    def SELECTED_REGION(region):
        return (By.XPATH, f"//*[contains(@class, 'RegionsList_wrapper__')]//*[text()='{region}']")

    @staticmethod
    def INTEREST_CHIP(interest):
        return (By.XPATH, f"//*[@data-name='interests']//*[text()='{interest}']")

    @staticmethod
    def STOP_INTEREST_CHIP(interest):
        return (By.XPATH,
                f"//*[contains(@class, 'vkuiFormItem') and .//*[contains(@class, 'vkuiTypography') and text()='Исключая интересы']]//*[text()='{interest}']")

    @staticmethod
    def SIDEBAR_AD_INPUT(input, value):
        return (By.XPATH,
                f"//*[contains(@class, 'vkuiFormItem') and .//*[contains(@class, 'FormItem_topText__') and text()='{input}']]//*[text()='{value}']")