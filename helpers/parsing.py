from bs4 import BeautifulSoup


def get_class_name(soup_obj: BeautifulSoup, course_no):
    """
    'Digital Marketing Analytics in Theory and Practice'
    """
    table = soup_obj.find('div', attrs={'id': 'win0divUC_RSLT_NAV_WRK_GROUPBUTTON${}'.format(course_no)})
    class_name = table.findAll('span', attrs={'id': 'UC_CLSRCH_WRK_UC_CLASS_TITLE${}'.format(course_no)})[0].text
    print(class_name)
    return class_name


def get_course(soup_obj: BeautifulSoup, course_no):
    """
    MSCA 32013/1P01 [27205]
    Open
    In-Person
    """
    table = soup_obj.find('div', attrs={'id': 'win0divUC_RSLT_NAV_WRK_HTMLAREA${}'.format(course_no)})
    modified_text = table.text.replace('\n', '')
    section_condition = modified_text.split(' ')[-1].strip()  # Open or Closed
    section_type = modified_text.split(' ')[-2].strip()  # in-person or online
    section_code = modified_text.split('-')[0].strip()  # the unique course code
    print(section_code)
    print(section_condition)
    print(section_type)

    return section_code, section_condition, section_type


def get_section_capacity(soup_obj: BeautifulSoup, course_no):
    table = soup_obj.find('div', attrs={'id': 'win0divUC_CLSRCH_WRK_DESCR1${}'.format(course_no)})
    section_availability = table.text.replace('\n', '').split(' ')[-1]
    current_capacity = section_availability.split('/')[0]
    total_capacity = section_availability.split('/')[1]
    print("Total Capacity: {}\nCurrent Capacity: {}".format(total_capacity, current_capacity))
    return total_capacity, current_capacity
