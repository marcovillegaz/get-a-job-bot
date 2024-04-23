from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

service = Service(executable_path=r"Browser\geckodriver.exe")
driver = webdriver.Firefox(service=service)


## GOOGLe
# Open webpage
driver.get("https://www.google.com/")
# Search an element by its class in HTML
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.send_keys("Colo Colo Libertadores" + Keys.ENTER)

""" ## AIRBNB
# Open webpage
driver.get("https://www.airbnb.cl/")
# Search an element by its class in HTML
search_button = driver.find_element(
    By.CLASS_NAME,
    "ihcg2em atm_9j_tlke0l atm_9s_1ulexfb atm_2a_1u8qnfj atm_3f_okh77k atm_5j_1vi7ecw atm_am_qk3dho atm_jb_idpfg4 atm_l8_2zoau0 atm_6h_1s2714j_vmtskl atm_66_nqa18y_vmtskl atm_4b_1egtlkw_vmtskl atm_5e_idpfg4_vmtskl atm_92_1yyfdc7_vmtskl atm_9s_glywfm_vmtskl atm_e2_1vi7ecw_vmtskl atm_h3_4h84z3_vmtskl atm_mk_stnw88_vmtskl atm_n3_idpfg4_vmtskl atm_tk_1ssbidh_vmtskl atm_wq_idpfg4_vmtskl atm_2a_1u8qnfj_9in345 atm_3f_okh77k_9in345 atm_5j_1vi7ecw_9in345 atm_6i_idpfg4_9in345 atm_92_1yyfdc7_9in345 atm_fq_idpfg4_9in345 atm_mk_stnw88_9in345 atm_n3_idpfg4_9in345 atm_tk_idpfg4_9in345 atm_wq_idpfg4_9in345 i1w7syu0 atm_9s_1ulexfb_1rqz0hn atm_h0_yh40bf_9bj8xt atm_2d_um1unu_9bj8xt atm_9s_1ulexfb_1jy6zas atm_2d_1p8m8iw_1joo1sn atm_4b_1p8m8iw_1joo1sn atm_70_d987b7_1joo1sn atm_fq_idpfg4_1joo1sn atm_n3_idpfg4_1joo1sn atm_h0_yh40bf_1joo1sn dir dir-ltr",
)
search_button.click()

search_box = driver.find_element(By.ID, "bigsearch-query-location-input")
search_box.send_keys("Pichilemu") """


time.sleep(10)
driver.quit()
