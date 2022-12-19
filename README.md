![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2&height=200&section=header&text=Добро%20пожаловать!%20&fontAlignY=35&fontSize=60&desc=%20Selenium%20SignalGSM%20&descAlignY=60&descSize=50&animation=twinkling&fontColor=E9E9E9F3&descAlign=60&fontAlign=35)



<p align="center">
  <img title="by Gorelov Alexandr" src="https://readme-typing-svg.herokuapp.com?color=2986cc&font=Knewave&size=35&center=true&vCenter=true&lines=Gorelov+Alexandr;QA+engineer">
    <img title="Signal GSM" src="images/signal.png">
</p>


# Проект по автоматизации тестирования
## [Документация](http://confluence.bolid.ru/pages/viewpage.action?pageId=60820024)

### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:heavy_check_mark: [вход в Систему](http://192.168.22.159/)

## :rocket: Технологии и инструменты

<p  align="center"

<code><img width="5%" title="Pycharm" src="images/Pycharm.svg"></code>
<code><img width="5%" title="Selenium" src="images/Selenium.svg"></code>
<code><img width="5%" title="Redmine" src="images/Redmine.svg"></code>
<code><img width="5%" title="Python" src="images/Python.svg"></code>
<code><img width="5%" title="Allure Report" src="images/allure-Report-logo.svg"></code>
<code><img width="5%" title="Pytest" src="images/Pytest.svg"></code>
<code><img width="5%" title="GitLab" src="images/GitLab.svg"></code>
<code><img width="5%" title="TeamCity" src="images/TC.svg"></code>
</p>

> *В данном проекте автотесты написаны на <code><strong>*Python*</strong></code> с использованием фреймворка <code><strong>*PyTest*</strong></code> для UI-тестов и <code><strong>*requests*</strong></code> для API-тестов.*
>
>*Запуск тестов выполняется из <code><strong>*TeamCity*</strong></code>.*
>
>*<code><strong>*Allure Report*</strong></code> используются для визуализации результатов тестирования.*

## Реализованы проверки

### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; UI

> - [x] *Тесты на валидацию полей ввода*
> - [x] *Тесты на проверку Ui элементов*
> - [x] *Тесты на проверку сохранения*



### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; API

> - [x] *Тесты на проверку ответов от сервера*




## :computer: Запуск тестов из терминала


&nbsp;*Установка зависимостей:*

```bash
pip install --proxy http://<username>:<password>@proxy.bolid.ru:3128 -r requirements.txt
```

&nbsp;*Запуск всех тестов:*

```bash
python -m pytest tests/
```

&nbsp;*Запуск тестов с отчетом Allure:*

```bash
python -m pytest --browser=chrome --alluredir=allure_reports/  tests/<нужный тест>

```

где:
>- [x] *--browser - браузер, в котором будут выполняться тесты (по умолчанию chrome)*
>- [x] *--alluredir - папка в которую будут складываться отчеты*
>- [x] *tests/<нужный тест> - указывается нужный тест для запуска, либо указывается просто "tests/" для прогона всех тестов*


&nbsp;*Сформировать allure отчет:*

```bash
allure serve allure_reports/
```

## <img width="4%" title="Jenkins" src="images/TC.svg"> Запуск тестов в [TeamCity](http://192.168.22.130:8112/)


*Для запуска сборки необходимо выбрать интересующий build и нажать кнопку <code><strong>*RUN*</strong></code>.*

<p align="center">
  <img src="images/job_param.png" alt="job" width="800">
</p>

*После выполнения сборки, в блоке <code><strong>*Статус сборки*</strong></code> появится выпадающий список с полем Allure
<img width="2%" title="Allure Report" src="images/allure-Report-logo.svg"><code><strong>*Allure
Report*</strong></code>, кликнув по которому, откроется страница с сформированным html-отчетом.*

<p align="center">
  <img src="images/Allure_history.png" alt="job" width="1000">
</p>

## <img width="4%" title="Allure Report" src="images/allure-Report-logo.svg"> Отчет о результатах тестирования в [Allure Report](http://192.168.22.130:8112/viewLog.html?buildId=3207&buildTypeId=Signal_SeleniumTests&tab=report_project8_ALLURE)

### :pushpin: Общая информация

*Главная страница Allure-отчета содержит следующие информационные блоки:*

> - [x] <code><strong>*ALLURE REPORT*</strong></code> - отображает дату и время прохождения теста, общее количество прогнанных кейсов, а также диаграмму с указанием процента и количества успешных, упавших и сломавшихся в процессе выполнения тестов
>- [x] <code><strong>*TREND*</strong></code> - отображает тренд прохождения тестов от сборки к сборке
>- [x] <code><strong>*SUITES*</strong></code> - отображает распределение результатов тестов по тестовым наборам
>- [x] <code><strong>*ENVIRONMENT*</strong></code> - отображает тестовое окружение, на котором запускались тесты (в данном случае информация не задана)
>- [x] <code><strong>*CATEGORIES*</strong></code> - отображает распределение неуспешно прошедших тестов по видам дефектов
>- [x] <code><strong>*FEATURES BY STORIES*</strong></code> - отображает распределение тестов по функционалу, который они проверяют
>- [x] <code><strong>*EXECUTORS*</strong></code> - отображает исполнителя текущей сборки (ссылка на сборку в Jenkins)

<p align="center">
  <img src="images/job.jpg" alt="Allure Report" width="900">
</p>

### :pushpin: Список тестов c описанием шагов и визуализацией результатов

*На данной странице представляется стандартное распределение выполнявшихся тестов по тестовым наборам или классам, в
которых находятся тестовые методы.*

<p align="center">
  <img src="images/allure_step.jpg" alt="Allure Report" width="900">
</p>

[//]: # ()
[//]: # (## <img width="4%" title="Selenoid" src="images/daramirra_selenoid-logo.svg"> Пример запуска теста в Selenoid)

[//]: # ()
[//]: # (<p align="center">)

[//]: # (  <img src="images/daramirra_video.gif" alt="video" width="1000">)

[//]: # (</p>)

[//]: # ()
[//]: # (## <img width="4%" title="Telegram" src="images/daramirra_Telegram.svg"> Уведомления в Telegram)

[//]: # ()
[//]: # (<p align="center">)

[//]: # (  <img src="images/daramirra_tlgrm.png" alt="Telegram" width="440">)

[//]: # (  <img src="images/daramirra_tlgrm_.png" alt="Telegram" width="390">)

[//]: # (</p>)


<hr>
<p align="center">
  <img title="|Customized by Gorelov Alexandr|" src="images/github-contribution-grid-snake.svg" alt="snake">
</p>
