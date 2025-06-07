from selenium.webdriver.common.by import By

class LeadFormsLocators:
    SAVE_MODAL = (By.XPATH, "//*[contains(@class, 'ModalRoot_overlay__')]")
    CREATE_LEADFORM_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton') and text()='Создать лид-форму']")
    MODAL_FORM_LEAD = (By.XPATH, "//form[contains(@class, 'ModalSidebarPage_container__')]")
    SUBMIT_BUTTON = (By.XPATH, "//button[@data-testid='submit']")
    CANCEL_LEADFORM_BUTTON = (By.XPATH, "//button[@data-testid='cancel']")
    CONFIRM_DELETE_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__') and text()='Удалить']")
    CONTINUE_BUTTON = (By.XPATH, "//button[contains(@data-testid, 'submit')]")
    EDIT_IMAGES_BUTTON = (By.XPATH, "//button[contains(@aria-label, 'Edit')]")
    SELECT_ALL_IMAGES_BUTTON = (By.XPATH, "//*[contains(@class, 'EditControl_selection__')]//*[text()='Выбрать все']")
    DELETE_IMAGES_BUTTON = (By.XPATH, "//button[contains(@data-testid, 'delete')]")
    UPLOADED_IMAGE_ITEM = (By.XPATH, "//*[contains(@class, 'ItemList_item__')]")
    UPLOADED_IMAGE_NAME = (By.XPATH, "//*[contains(@class, 'ImageItem_name__')]")
    SAVE_IMAGE_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__') and text()='Сохранить']")

    LOAD_IMAGE_BUTTON = (By.XPATH, "//*[contains(@data-testid, 'set-global-image')]")
    LOAD_IMAGE_INPUT = (By.XPATH, "//input[@type='file']")

    FORM_NAME_INPUT = (By.XPATH, "//input[@placeholder='Название лид-формы']")
    COMPANY_NAME_INPUT = (By.XPATH, "//input[@placeholder='Название компании']")
    FORM_HEADER_INPUT = (By.XPATH, "//input[@placeholder='Текст заголовка']")
    DESCRIPTION_INPUT = (By.XPATH, "//input[@placeholder='Введите описание']")

    ADRESS_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Введите адрес')]")

    NAME_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Введите фамилию, имя и отчество')]")

    LOAD_LOGO_BUTTON = (By.XPATH, "//span[text()='Загрузить логотип']")

    CREATE_QUESTIONS_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton') and text()='Создать опрос']")
    ClOSE_QUESTIONS_BUTTON = (By.XPATH, "//button[contains(@aria-label, 'Close')]")
    SURVEYS_TAB = (By.XPATH, "//div[@data-testid='tabs-item' and @aria-controls='surveys']")
    YCLIENTS_TAB = (By.XPATH, "//div[@data-testid='tabs-item' and @aria-controls='yclients']")
    YCLIENTS_BUTTON = (By.XPATH, "//span[contains(@class, 'vkuiButton__content') and text()='Перейти в YCLIENTS']")
    LEAD_TAB = (By.XPATH, "//div[@data-testid='tabs-item' and @aria-controls='leadforms']")
    ADD_QUESTION_BUTTON = (By.XPATH, "//span[contains(@class, 'vkuiButton__content') and text()='Добавить вопрос']")
    ADD_SITE_BUTTON = (By.XPATH, "//span[text()='Добавить сайт']")
    ACTIVE_STATUS_CELL = (By.XPATH, "//div[@role='gridcell' and text()='Активен']")

    COMPANY_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Введите название')]")
    NAME_TITLE_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Введите название компании')]")
    TITLE_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Введите заголовок')]")
    DESCRIPTION_QUE_INPUT = (By.XPATH, "//textarea[@placeholder='Введите описание опроса']")

    QUESTION_INPUT = (By.XPATH, "//textarea[@placeholder='Текст вопроса']")
    ANSWER_1_INPUT = (By.XPATH, "(//input[@placeholder='Введите ответ'])[1]")
    ANSWER_2_INPUT = (By.XPATH, "(//input[@placeholder='Введите ответ'])[2]")
    SAVE_QUE_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__') and text()='Запустить опрос']")

    ARCHIVE_LINK = (By.XPATH, "//span[contains(@class, 'Nav_text__mcKDd') and text()='Архивировать']")
    ARCHIVE_BUTTON = (By.XPATH, "//span[contains(@class, 'vkuiButton__content') and text()='Архивировать']")

    HOVER_BUTTON = (By.XPATH, "//*[contains(@class, 'BaseTable__row')]")

    TEST_LEADFORM_NAME = (By.XPATH, "//span[text()='test']")