from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def lerArquivo():
    #ABRE O ARQUIVO DE TEXTO
    f = open("preferencias.txt", "r")

    #LE AS DUAS LINHAS
    urlDoSite = f.readline().split("--")[1][:-1]
    nomeDeQuemDeveVotar = f.readline().split("--")[1][:-1]
    quantasVezesVotar = int(f.readline().split("--")[1][:-1])

    #FECHA O ARQUIVO
    f.close()

    return [urlDoSite, nomeDeQuemDeveVotar, quantasVezesVotar]


def votar():
    #RECEBE OS DADOS
    urlDoSite, nomeDeQuemDeveVotar, quantasVezesVotar = lerArquivo()

    #OPÇÕES PARA RODA ESCONDIDO
    options = Options()
    options.headless = True

    #ABRE O FIREFOX
    driver = webdriver.Firefox()

    cont = 0
    while(cont < quantasVezesVotar):
        #ACESSA O SITE
        driver.get(urlDoSite)

        #CLICA NO NOME ESCOLHIDO
        ondeClicar = "//label[@class='docssharedWizToggleLabeledContainer freebirdFormviewerViewItemsRadioChoice']//*[text()='" + nomeDeQuemDeveVotar + "']"
        driver.find_element_by_xpath(ondeClicar).click();

        #CLICA EM ENVIAR
        driver.find_element_by_xpath("//div[@class='freebirdFormviewerViewNavigationButtons']//*[text()='Enviar']").click();
        cont += 1

    driver.quit()


votar()