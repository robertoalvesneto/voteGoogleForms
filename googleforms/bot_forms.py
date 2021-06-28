from selenium import webdriver
# from selenium.webdriver.firefox.options import Options


class BotForms:
    def __init__(self):
        self.driver = None

    def __start_driver(self):
        self.driver = webdriver.Firefox()

    def __stop_driver(self):
        self.driver.close()

    def __open_page(self, website_url):
        self.driver.get(website_url)

    def __text_field_get_by_title(self, name_title_field):
        # path do titulo
        path_title_component = "//*[text()='{0}']".format(
            name_title_field)
        # pega o elemento que contem o titulo
        title_component = self.driver.find_element_by_xpath(
            path_title_component)

        return title_component

    def __text_field_get_root_ancestral(self, title_component):
        # classe do elemento pai que contem todo um campo
        path_base_root = "freebirdFormviewerComponentsQuestionBaseRoot"
        # path ancestral principal desse campo
        path_root_ancestor = "//ancestor::div[@class='{0}']".format(
            path_base_root)
        # pega o elemento que eh o ancestral
        root_ancestor = title_component.find_element_by_xpath(
            path_root_ancestor)

        return root_ancestor

    def __text_field(self, name_title_field, insert_text):

        title_component = self.__text_field_get_by_title(name_title_field)

        root_ancestor = self.__text_field_get_root_ancestral(title_component)

        # pega o input dessa classe
        input_field = root_ancestor.find_element_by_tag_name("input")
        input_field.send_keys(insert_text)

    def builder(self, website_url, name_title_field, insert_text):
        # OPÇÕES PARA RODA ESCONDIDO
        # options = Options()
        # options.headless = True

        # ABRE O FIREFOX
        self.__start_driver()

        self.__open_page(website_url)

        self.__text_field(name_title_field, insert_text)
