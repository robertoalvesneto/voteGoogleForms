import unittest
from googleforms.bot_forms import BotForms


class TestTextField(unittest.TestCase):
    website_url = "https://forms.gle/wtwFScuirGPmkxmK6"
    name_title_field = "normal"
    insert_text = "texto aleatorio a ser inserido"
    path_base_root = "freebirdFormviewerComponentsQuestionBaseRoot"
    bf = None

    def setUp(self):
        self.bf = BotForms()
        self.bf._BotForms__start_driver()
        self.bf._BotForms__open_page(self.website_url)

    def tearDown(self):
        self.bf._BotForms__stop_driver()

    def test_get_element_by_title(self):
        # Testa se pegou o elemento pelo titulo.
        title_component = self.bf._BotForms__text_field_get_by_title(
            self.name_title_field)

        self.assertIn(self.name_title_field, title_component.text)

    def test_get_root_ancestral(self):
        # Testa se pegou o pai principal do componente.
        title_component = self.bf._BotForms__text_field_get_by_title(
            self.name_title_field)

        root_ancestor = self.bf._BotForms__text_field_get_root_ancestral(
            title_component)

        self.assertIn(self.path_base_root,
                      root_ancestor.get_attribute("class"))

    def test_filled_field(self):
        # Testa se inseriu corretamente o texto no campo.
        self.bf._BotForms__text_field(
            self.name_title_field, self.insert_text)

        title_component = self.bf._BotForms__text_field_get_by_title(
            self.name_title_field)
        root_ancestor = self.bf._BotForms__text_field_get_root_ancestral(
            title_component)
        input_field = root_ancestor.find_element_by_tag_name("input")

        self.assertIn(self.insert_text, input_field.get_attribute("value"))


class SuiteTestsTextField():

    def __set_botform_values(self, name_title_field):
        insert_text = "texto aleatorio a ser inserido"
        TestTextField.name_title_field = name_title_field
        TestTextField.insert_text = insert_text

    def __create_suite(self):
        suite = unittest.TestSuite()
        suite.addTest(TestTextField("test_get_element_by_title"))
        suite.addTest(TestTextField("test_get_root_ancestral"))
        suite.addTest(TestTextField("test_filled_field"))

        return suite

    def __builder_suite_test(self, name_title_field):
        self.__set_botform_values(name_title_field)

        return self.__create_suite()

    def test_simple_text_field(self):
        return self.__builder_suite_test("normal")

    def test_required_text_field(self):
        return self.__builder_suite_test("campo obrigatório")

    def test_text_field_with_description(self):
        return self.__builder_suite_test("com descrição")

    def test_text_field_with_validate(self):
        return self.__builder_suite_test("com descrição")

    def test_text_field_with_image(self):
        return self.__builder_suite_test("com imagem")

    def test_text_fields_with_same_name(self):
        return self.__builder_suite_test("teste campo com mesmo nome")

    def test_text_fields_without_name(self):
        return self.__builder_suite_test("")


if __name__ == "__main__":
    # rodar os testes:
    # python3 -m tests.gc_textfield_test
    suite = SuiteTestsTextField()

    runner = unittest.TextTestRunner()
    runner.run(suite.test_simple_text_field())
    runner.run(suite.test_required_text_field())
    runner.run(suite.test_text_field_with_description())
    runner.run(suite.test_text_field_with_validate())
    runner.run(suite.test_text_field_with_image())
    runner.run(suite.test_text_fields_with_same_name())
    runner.run(suite.test_text_fields_without_name())
    # unittest.main()
