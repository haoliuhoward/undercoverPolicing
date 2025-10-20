rm(list=ls(all=TRUE))
cat("\014")

library(tidyverse)
library(fixest)
library(glmmTMB)
library(texreg)


# Load data -----------------------------------------
load("data/panel_dat.rda") 

# model 1
model_vio_feols <- feols(policeUC_arrest_bin 
                         ~ cl_quart_sw + cl_quarter + policeUC_count_bin + policeUni_car_count_bin + pArrest_count_sw + violence_escalation 
                         | CACODE,
                         data=panel_dat, panel.id = ~ CACODE) 

# model 2
model_vio_feols.t <- feols(policeUC_arrest_bin
                           ~ cl_quart_sw + cl_quarter + policeUC_count_bin + policeUni_car_count_bin + pArrest_count_sw + violence_escalation  + time +time2 + time3 
                           | CACODE, 
                           data=panel_dat, panel.id = ~ CACODE) 

# model 3
model_vio_feols_iv <- feols(policeUC_arrest_bin 
                            ~ policeUC_count_bin + policeUni_car_count_bin + pArrest_count_sw + violence_escalation 
                            | CACODE | cl_quart_sw + cl_quarter ~ weekend + day,
                            data=panel_dat, panel.id = ~ CACODE)

# model 4
model_vio_feols_iv.t <- feols(policeUC_arrest_bin ~ policeUC_count_bin + policeUni_car_count_bin + pArrest_count_sw + violence_escalation + time +time2 + time3 
                              | CACODE | cl_quart_sw + cl_quarter ~ weekend + day ,
                              data=panel_dat, panel.id = ~ CACODE)

# model 5
re_vio.mod <- glmmTMB(policeUC_arrest_bin ~ cl_quart_sw + cl_quarter + policeUC_count_bin + policeUni_car_count_bin + pArrest_count_sw + violence_escalation + indoorSp_protests + legCo  + (1 | CACODE), data = panel_dat, family="gaussian") 

# model 6
re_vio.mod.t <- glmmTMB(policeUC_arrest_bin ~ cl_quart_sw + cl_quarter + policeUC_count_bin + policeUni_car_count_bin + pArrest_count_sw + violence_escalation + indoorSp_protests + legCo + time +time2 + time3 + (1 | CACODE), data = panel_dat, family="gaussian")


# main result (Table 1)--------------------------------
idvs = c("Closeness to protest zone",  "Protest zone", 
         "Undercover Police", "Uniformed Police", "Arrests nearby", "Protest violence",
          "time", "time2", "time3",
         "Predicted closeness to protest zone","Predicted protest zone", 
          "Intercept", 
          "Indoor spaces", "LegCo"
)

screenreg(list(model_vio_feols, model_vio_feols.t,
               model_vio_feols_iv,model_vio_feols_iv.t,
               re_vio.mod, re_vio.mod.t),
          include.variance=F, include.intercept = F,
          include.rsquared = F, include.loglik = F,
          include.aic = F, include.adjr = F,
          digits = 4,
          stars = c(0.01, 0.05, 0.10),
          custom.model.names = c(
            "OLS", "OLS",
            "2SLS","2SLS",
            "OLS", "OLS"),
          custom.coef.names = idvs,
          custom.gof.rows = list(Model = c("FE", "FE", "FE", "FE", "RE", "RE"), TimePoly = c("N", "Y", "N", "Y","N", "Y")),
          omit.coef = "(time|time2|time3|(Intercept))"
          ) 

