from selenium.webdriver.common.by import By

class LeadFormsLocators:
    EXAMPLE_INPUT = (
        By.XPATH,
        "//input[contains(@class, 'EXAMPLEInput__el')]"
    )
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

    NAME_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Введите фамилию, имя и отчество')]")
