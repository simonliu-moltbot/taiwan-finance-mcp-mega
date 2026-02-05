# 🏦 Taiwan Finance MCP Mega - 330+ 完整工具字典 (v3.2.3)

本手冊詳列了 **Taiwan Finance MCP Mega** 內建的所有 **330+** 個金融與公共數據工具。所有工具均對接真實 API 並支援 `symbol` 符號過濾（如 `2330` 或 `USD`）。

---

## 📂 1. 台股市場深度分析 (STOCK) - 100 個工具
| 工具 ID | 功能描述 |
| :--- | :--- |
| `stock_realtime_quotes` | **[核心]** 個股當日即時行情 |
| `stock_fundamental_eps` | 季度每股盈餘 (EPS) 分析 |
| `stock_dividend_yield` | 現金殖利率、本益比與淨值比 |
| `stock_chip_institutional_flow` | 三大法人買賣超彙總 |
| `stock_technical_ma_signals` | 移動平均線多空信號 |
| `stock_margin_balance_monitor` | 全市場融資融券餘額 |
| `stock_pe_ratio_ranking` | 全市場本益比排名 |
| `stock_pb_ratio_analysis` | 股價淨值比解析 |
| `stock_net_worth_lookup` | 查詢公司每股淨值 |
| `stock_insider_ownership` | 董監持股比例 |
| `stock_government_fund_holdings` | 官股行庫持股動向 |
| `stock_foreign_investment_limit` | 外資持股限額與餘額 |
| `stock_market_breadth_index` | 市場漲跌家數與成交比重 |
| `stock_put_call_ratio_tw` | 台指選擇權多空比 |
| `stock_vix_fear_gauge` | 台灣版恐慌指數 |
| `stock_etf_tracking_error` | ETF 追蹤誤差分析 |
| `stock_etf_dividend_calendar` | ETF 除息日曆 |
| `stock_warrant_delta_analysis` | 權證 Delta 風險分析 |
| `stock_after_hours_trading` | 盤後定價交易資訊 |
| `stock_block_trade_summary` | 鉅額交易摘要 |
| `stock_odd_lot_quotes` | 盤中零股交易即時行情 |
| `stock_announcements` | 上市公司重大訊息公告 |
| `stock_yield_ranking_top` | 高殖利率績優股排行 |
| `stock_price_limit_tracker` | 今日漲跌停個股追蹤 |
| `stock_broker_branch_flow` | 分點券商進出分佈 |
| `stock_buyback_status` | 庫藏股執行進度 |
| `stock_capital_reduction_notice` | 減資預告資訊 |
| `stock_new_listing_ipo` | 新股上市 IPO 資訊 |
| `stock_delisting_risk_watch` | 下市風險預警監控 |
| `stock_component_stock_weights` | 指數權重股佔比分析 |
| `stock_sector_rotation_meter` | 類股輪動強弱儀 |
| `stock_daily_volume_rank` | 當日成交量排行 |
| `stock_market_capitalization_top` | 全市場市值排行 |
| `stock_tpex_quotes_realtime` | 上櫃市場即時行情 |
| `stock_tpex_market_index` | 櫃買指數動態 |
| `stock_tpex_institutional_flow` | 上櫃法人買賣超 |
| `stock_tpex_emerging_quotes` | 興櫃股票即時行情 |
| `stock_tpex_convertible_bonds` | 上櫃可轉債成交資訊 |
| `stock_industry_pe_average` | 產業平均本益比對比 |
| `stock_cash_flow_statement_summary` | 現金流量表摘要 |
| `stock_balance_sheet_ratios` | 資產負債率分析 |
| `stock_profit_loss_preview` | 損益表數據預覽 |
| `stock_operating_margin_trend` | 營業利益率趨勢 |
| `stock_inventory_turnover_rate` | 存貨週轉率監控 |
| `stock_debt_to_equity_ratio` | 權益負債比 |
| `stock_roe_dupoint_analysis` | 杜邦分析 (ROE) |
| `stock_roa_efficiency_index` | 資產報酬率 (ROA) |
| `stock_revenue_growth_yoy` | 營收年增率分析 |
| `stock_monthly_sales_momentum` | 月營收成長動能 |
| `stock_quarterly_earnings_guide` | 季報展望與獲利指南 |
| `stock_esg_occupational_safety` | 企業職安數據揭露 |
| `stock_esg_fire_incidents` | 企業火災事故統計 |
| `stock_esg_anti_competition` | 反競爭行為訴訟揭露 |
| `stock_esg_risk_management` | 企業風險管理政策 |
| `stock_esg_shareholding_control` | 持股與控制力結構 |
| `stock_esg_inclusive_finance` | 普惠金融執行概況 |
| `stock_esg_info_security` | 企業資安維護現況 |
| `stock_esg_community_relations` | 社區關係與公益投入 |
| `stock_esg_product_quality` | 產品品質與安全數據 |
| `stock_esg_supply_chain` | 供應鏈管理永續指標 |
| `stock_esg_food_safety` | 食品安全管理揭露 |
| `stock_esg_life_cycle` | 產品生命週期管理 |
| `stock_esg_fuel_management` | 企業燃料與能耗管理 |
| `stock_esg_functional_committee` | 董事會功能性委員會 |
| `stock_esg_climate_issues` | 氣候相關議題管理 |
| `stock_esg_investor_comm` | 投資人溝通頻率與透明度 |
| `stock_esg_board_structure` | 董事會組成背景分析 |
| `stock_esg_human_development` | 人力資源與人才發展 |
| `stock_esg_waste_management` | 廢棄物處理統計數據 |
| `stock_esg_water_resources` | 水資源管理與回收 |
| `stock_esg_energy_efficiency` | 能源轉型與使用效率 |
| `stock_esg_ghg_emissions` | 溫室氣體排放量 (Scope 1/2/3) |
| `stock_etf_regular_savings_rank` | ETF 定期定額戶數排行 |
| `stock_broker_sec_reg_data` | 證券商辦理業務名冊 |
| `stock_financial_report_general` | 一般業資產負債表摘要 |
| `stock_financial_report_bank` | 銀行業資產負債表摘要 |
| `stock_financial_report_ins` | 保險業資產負債表摘要 |
| `stock_financial_report_sec` | 證券業資產負債表摘要 |
| `stock_cash_dividend_history` | 歷史現金股利數據 |
| `stock_stock_dividend_history` | 歷史股票股利數據 |
| `stock_mops_significant_events` | 公開資訊觀測站重大訊息 |
| `stock_listed_company_basic_info` | 上市公司基本登記資料 |
| `stock_otc_company_basic_info` | 上櫃公司基本登記資料 |
| `stock_emerging_company_info` | 興櫃公司基本登記資料 |
| `stock_suspension_trading_list` | 暫停交易個股名單 |
| `stock_reumption_trading_list` | 恢復交易個股名單 |
| `stock_foreign_investor_holding` | 外資持股比例變動 |
| `stock_market_turnover_ratio` | 市場換手率與週轉率 |
| `stock_industry_market_cap_ratio` | 各產業市值權重佔比 |
| `stock_investor_education_stats` | 投資人教育與宣導統計 |
| `stock_broker_branch_locations` | 全國證券商分點地理資訊 |
| `stock_trading_calendar_tw` | 台灣股市開休市交易日曆 |
| `stock_warrant_issuer_ranking` | 權證發行商信用排行 |
| `stock_etf_tracking_index_info` | ETF 追蹤指數詳細資料 |
| `stock_bond_etf_quotes` | 債券型 ETF 即時報價 |
| `stock_leveraged_inverse_etf` | 槓桿及反向 ETF 成交動態 |
| `stock_market_odd_lot_top` | 盤中零股交易熱門榜 |
| `stock_investor_sentiment_index` | 散戶多空信心指標分析 |
| `stock_block_trade_details` | 鉅額交易逐筆明細 |
| `stock_futures_realtime_top` | 台指期貨即時熱度監控 |

---

## 💹 2. 全球匯率與大宗商品 (FOREX) - 50 個工具
| 工具 ID | 功能描述 |
| :--- | :--- |
| `forex_usd_twd` | 美金對台幣即時匯率 |
| `forex_jpy_twd` | 日幣對台幣即時匯率 |
| `forex_eur_twd` | 歐元對台幣即時匯率 |
| `forex_cny_twd` | 人民幣對台幣即時匯率 |
| `forex_hkd_twd` | 港幣對台幣即時匯率 |
| `forex_gbp_twd` | 英鎊對台幣即時匯率 |
| `forex_aud_twd` | 澳幣對台幣即時匯率 |
| `forex_cad_twd` | 加幣對台幣即時匯率 |
| `forex_sgd_twd` | 新幣對台幣即時匯率 |
| `forex_krw_twd` | 韓元對台幣即時匯率 |
| `forex_chf_twd` | 瑞郎對台幣即時匯率 |
| `forex_nzd_twd` | 紐幣對台幣即時匯率 |
| `forex_thb_twd` | 泰銖對台幣即時匯率 |
| `forex_myr_twd` | 馬幣對台幣即時匯率 |
| `forex_idr_twd` | 印尼盾對台幣即時匯率 |
| `forex_vnd_twd` | 越南盾對台幣即時匯率 |
| `forex_php_twd` | 披索對台幣即時匯率 |
| `forex_inr_twd" | 印度盧比對台幣即時匯率 |
| `forex_zar_twd` | 南非幣對台幣即時匯率 |
| `forex_mxn_twd` | 墨西哥披索對台幣即時匯率 |
| `forex_bank_buying_max` | 全台銀行最高買入價比價 |
| `forex_bank_selling_min` | 全台銀行最低賣出價比價 |
| `forex_atm_withdraw_rates` | 海外 ATM 提款即時匯率 |
| `forex_credit_card_fx_fee" | 信用卡海外刷卡手續費資訊 |
| `forex_travelers_check_quotes` | 旅行支票牌告匯率 |
| `forex_historical_fx_high_low` | 特定幣別歷史高低點查詢 |
| `forex_volatility_index_fx` | 匯率波動率與避險指標 |
| `forex_central_bank_intervention` | 央行干預匯市預警數據 |
| `forex_interbank_swap_rates` | 銀行同業掉期與拆款利率 |
| `forex_fx_correlation_matrix` | 幣別間相關性矩陣分析 |
| `forex_gold_spot_twd` | 國際黃金現貨(台幣計價) |
| `forex_silver_spot_twd` | 國際白銀現貨(台幣計價) |
| `forex_oil_wti_price` | WTI 原油即時價格 |
| `forex_oil_brent_price` | 布蘭特原油即時價格 |
| `forex_copper_lme_quotes` | LME 國際銅價行情 |
| `forex_gas_natural_spot` | 天然氣現貨即時報價 |
| `forex_corn_futures_price` | 國際玉米期貨報價 |
| `forex_soybean_futures_price` | 國際黃豆期貨報價 |
| `forex_wheat_futures_price` | 國際小麥期貨報價 |
| `forex_bdi_shipping_index` | 波羅的海乾散貨指數 (BDI) |
| `forex_sugar_futures` | 國際糖價期貨行情 |
| `forex_coffee_futures` | 國際咖啡豆期貨行情 |
| `forex_platinum_spot` | 國際鉑金現貨報價 |
| `forex_palladium_spot` | 國際鈀金現貨報價 |
| `forex_aluminum_lme` | LME 國際鋁價行情 |
| `forex_nickel_lme` | LME 國際鎳價行情 |
| `forex_zinc_lme` | LME 國際鋅價行情 |
| `forex_lead_lme` | LME 國際鉛價行情 |
| `forex_iron_ore_fines` | 鐵礦砂現貨報價 |
| `forex_lithium_carbonate` | 碳酸鋰/鋰礦產業行情 |

---

## 🏦 3. 銀行、稅務與信貸 (50 個工具)
| 工具 ID | 功能描述 |
| :--- | :--- |
| `bank_deposit_rate_fixed` | 銀行定期存款利率排名 |
| `bank_deposit_rate_savings` | 銀行高利活存專案監控 |
| `bank_mortgage_rate_avg` | 五大銀行平均房貸利率趨勢 |
| `bank_mortgage_first_home` | 首購族優惠房貸方案比價 |
| `bank_mortgage_investment` | 非自住/投資性房貸利率加成 |
| `bank_personal_loan_index` | 個人信用貸款平均行情 |
| `bank_car_loan_rates` | 汽車貸款與新能源車貸利率 |
| `bank_credit_card_delinquency` | 信用卡逾期違約率統計 |
| `bank_credit_card_spending_total` | 全台信用卡月度刷卡總額 |
| `bank_atm_map` | 全台外幣/一般 ATM 服務據點 |
| `bank_digital_bank_bonus` | 數位帳戶開戶禮與轉帳優惠 |
| `bank_bank_branch_locations` | 銀行分行地址與營業時間 |
| `bank_wire_transfer_speed` | 跨境匯款入帳速度監控 |
| `bank_check_clearing_volume` | 票據交換量與景氣指標 |
| `bank_capital_adequacy` | 銀行資本適足率 (RBC) 安全指標 |
| `bank_loan_to_deposit` | 銀行存放比與流動性分析 |
| `bank_npl_ratio` | 銀行不良資產 (呆帳) 比率排名 |
| `bank_sme_financing_index` | 中小企業專案融資達成率 |
| `bank_interest_margin` | 銀行淨利差 (NIM) 表現分析 |
| `bank_asset_quality` | 商業銀行資產品質評等紀錄 |
| `bank_foreign_exchange_volume` | 台北外匯市場每日交易量 |
| `bank_mortgage_by_age` | 不同年齡層購屋房貸佔比統計 |
| `bank_credit_card_types` | 熱門信用卡類別市佔率分析 |
| `bank_trust_fund_stats` | 信託資產管理總額統計 |
| `bank_financial_holding_profits` | 各大金控公司獲利排行 |
| `bank_open_api_standard" | 台灣 Open Banking 技術標準規範 |
| `tax_income_brackets` | 個人綜合所得稅課稅級距 |
| `tax_standard_deduction` | 年度標準扣除額數值 |
| `tax_itemized_deduction` | 列舉扣除額 (捐贈、房租) 規定 |
| `tax_gift_estate_limits` | 遺產與贈與稅免稅額度表 |
| `tax_corporate_rate` | 營利事業所得稅最新稅率 |
| `tax_withholding_rules` | 各類所得就源扣繳稅率規則 |
| `tax_house_tax_rates` | 全台囤房稅 2.0 各縣市稅率 |
| `tax_land_value_increment` | 土地增值稅試算基礎與現值 |
| `tax_deed_tax_calc` | 房屋契稅稅率與計算說明 |
| `tax_luxury_tax_rules` | 高價勞務與貨物稅 (奢侈稅) 規定 |
| `tax_vat_return_guide` | 營業稅申報與進項扣抵指南 |
| `tax_customs_duty_info` | 跨境電商/個人進口關稅查詢 |
| `tax_tobacco_alcohol` | 菸酒稅徵收統計與稅額計算 |
| `tax_lottery_prize_tax` | 獎券中獎所得扣繳規定 |
| `tax_foreign_income_rule` | 海外所得 670 萬申報門檻細則 |
| `tax_revenue_collection` | 全國稅收實徵淨額月報 |
| `tax_evasion_alerts` | 高風險稅務異常查核指標 |
| `tax_incentive_policy` | 產業創新條例租稅優惠追蹤 |
| `tax_electronic_invoice_usage` | 雲端/電子發票採用率統計 |
| `tax_global_minimum_tax` | 全球最低稅負制對台影響數據 |
| `tax_land_tax_overdue` | 欠繳稅捐強制執行案量統計 |
| `tax_income_declaration_stats` | 報稅管道 (手機/線上) 戶數分析 |
| `tax_inheritance_case_stats` | 遺產繼承案量變動趨勢 |
| `tax_business_registration_tax` | 營業登記與稅籍異動規範 |

---

## 🏛️ 4. 企業、產業與物流 (60 個工具)
| 工具 ID | 功能描述 |
| :--- | :--- |
| `corp_company_registration` | 全國公司商工登記資料查詢 |
| `corp_factory_count_stats` | 全台工廠登記地理分佈統計 |
| `corp_industrial_park_list` | 工業園區進駐企業名單與進駐率 |
| `corp_esg_carbon_emission` | 企業範疇二碳排放揭露概況 |
| `corp_legal_suit_count` | 企業法律訴訟與專利糾紛紀錄 |
| `corp_announcement_mops` | 公開資訊觀測站私募/增資重訊 |
| `corp_procurement_tender_count` | 政府採購標案月度總量統計 |
| `corp_procurement_winner_rank` | 政府標案年度得標廠商排名 |
| `corp_tech_tender_budget` | 科技發展計畫招標預算監控 |
| `corp_government_spending_yoy` | 產業發展補助支出年增率 |
| `corp_export_value_by_industry` | 台灣主要產業出口總值統計 |
| `corp_import_value_by_category` | 台灣關鍵物資進口金額分析 |
| `corp_trade_balance_monitor` | 進出口貿易差額 (順差/逆差) |
| `corp_port_container_throughput` | 台灣主要港口貨櫃裝卸量 |
| `corp_airport_cargo_volume` | 桃園機場航空貨運實時數據 |
| `corp_logistics_warehouse_rent` | 物流園區與自動化倉儲租金 |
| `corp_e_commerce_delivery_speed` | 三大電商平台物流配送效率指數 |
| `corp_retail_sales_index` | 零售業與連鎖超商銷售增長指數 |
| `corp_wholesale_market_prices` | 果菜批發市場每日成交均價 |
| `corp_agri_product_trading` | 全台農產品每日總交易量 |
| `corp_factory_pollution_alerts` | 工廠排污違規與自動監測預警 |
| `corp_patent_registration_stats` | 台灣 AI 與科技專利申請排名 |
| `corp_trademark_lookup_tw` | 台灣商標註冊現況查詢 |
| `corp_labor_dispute_count` | 各行業勞資糾紛與調解案件統計 |
| `corp_income_tax_rank` | 企業營利事業所得稅納稅大戶排行 |
| `corp_energy_consumption` | 工業區能源消耗強度 (EUI) 監控 |
| `corp_green_energy_adoption` | 上市櫃公司再生能源憑證購買量 |
| `corp_foreign_talent_work_permit` | 就業金卡與外籍專業人才在台數 |
| `corp_smb_financing_index` | 中小企業信用保證核貸趨勢 |
| `corp_bond_issuance` | 公司債與可持續發展債券發行紀錄 |
| `corp_foreign_direct_investment` | 僑外資來台投資金額與產業分佈 |
| `corp_offshore_wind_farm_progress` | 離岸風電建設併網進度追蹤 |
| `corp_semiconductor_fab_status` | 先進製程廠房建置與環評進度 |
| `corp_venture_capital_stats` | 台灣創投市場投資賽道金額統計 |
| `corp_listed_company_board_diversity` | 董事會成員性別與背景多元化分析 |
| `corp_female_leadership_ratio` | 企業女性高階主管佔比統計 |
| `corp_research_development_spending` | 科技龍頭 R&D 研發費用趨勢分析 |
| `corp_merger_acquisition_flow` | 台灣企業海外併購案例與金額 |
| `corp_startup_survival_rate` | 各類新創企業三年/五年存活率分析 |
| `corp_business_bankruptcy_stats` | 全台公司行號解散、停業統計 |
| `corp_factory_land_demand` | 科學園區工業用地供需預測 |
| `corp_industrial_electricity_stats` | 台灣工業用電結構與尖峰調整量 |
| `corp_high_tech_export_ratio` | 高科技產品佔整體出口價值比例 |
| `corp_supply_chain_resilience` | 供應鏈多元化與風險評估指數 |
| `corp_free_trade_zone_stats` | 自由貿易港區年度貿易總值 |
| `corp_brand_valuation_ranking` | 台灣最佳國際品牌價值排行 |
| `corp_incubator_occupancy` | 政府育成中心與青創空間進駐率 |
| `corp_foreign_representative_office` | 新設外商辦事處國家別統計 |
| `corp_cooperative_society_stats` | 農業/信用合作社資產總額統計 |
| `corp_traditional_industry_upgrade` | 傳產自動化轉型輔導案例量 |
| `corp_semiconductor_market_share` | 台灣半導體晶圓代工全球市佔率 |
| `corp_ict_supply_chain_depth` | ICT 產業供應鏈本地化深度分析 |
| `corp_retail_footfall_stats` | 實體零售據點客流量趨勢數據 |
| `corp_logistics_last_mile_cost` | 最後一哩路配送成本與效率指標 |
| `corp_trademark_infringement_count` | 智慧財產權侵權訴訟年度案件量 |
| `corp_green_bond_subscription` | 綠色債券市場申購熱度統計 |
| `corp_tech_startup_listing_age` | 科技新創從創立到掛牌之平均年數 |
| `corp_industry_r_d_intensity` | 各產業研發強度 (R&D/Revenue) |
| `corp_foreign_talent_retention` | 外籍高階人才留台率與續約統計 |
| `corp_circular_economy_output` | 循環經濟產業年產值與效益分析 |

---

## 📊 5. 宏觀經濟、環境與社會 (50 個工具)
| 工具 ID | 功能描述 |
| :--- | :--- |
| `macro_cpi_inflation_rate` | 台灣消費者物價指數 (CPI) 與通膨率 |
| `macro_gdp_growth_quarterly` | 季度 GDP 成長率預測與統計 |
| `macro_unemployment_rate_tw` | 台灣最新失业率與求供倍數 |
| `macro_pmi_manufacturing` | 製造業採購經理人指數 (PMI) |
| `macro_nmi_non_manufacturing` | 非製造業經理人指數 (NMI) |
| `macro_monetary_supply_m2` | 貨幣供給量 M2 與資金水位 |
| `macro_foreign_exchange_reserve` | 台灣外匯存底總額變動 |
| `macro_government_debt_clock` | 中央政府國債鐘即時數據 |
| `macro_public_infrastructure_budget` | 公共建設與前瞻計畫預算進度 |
| `macro_central_bank_interest_rate` | 央行理監事會議利率決議 (重貼現率) |
| `macro_interbank_call_loan` | 銀行同業拆款利率與流動性 |
| `macro_bond_yield_10y` | 台灣十年期公債殖利率趨勢 |
| `macro_fertility_rate_stats` | 台灣各縣市出生率與總生育率數值 |
| `macro_population_aging_index` | 台灣人口老化指數與扶養比趨勢 |
| `macro_electricity_reserve_margin` | 每日台電備轉容量率燈號監控 |
| `macro_water_reservoir_levels` | 全台主要水庫即時蓄水量百分比 |
| `macro_oil_stockpile_days` | 台灣能源(石油)安全存量天數 |
| `macro_rice_security_inventory` | 國家糧食(稻米)安全存量數據 |
| `macro_digital_economy_contribution` | 數位產業對 GDP 貢獻度分析 |
| `macro_startup_investment_total` | 台灣新創獲得年度投資總額統計 |
| `macro_tourism_arrival_count` | 國際來台旅客數量與客源國統計 |
| `macro_department_store_sales` | 全台百貨公司與內需市場銷額 |
| `macro_car_registration_new` | 新車掛牌數與新能源車佔比 |
| `macro_housing_starts_index` | 住宅開工件數與建照核發趨勢 |
| `macro_m1b_m2_multiplier` | 貨幣乘數分析與股市資金動力訊號 |
| `macro_labor_participation_rate` | 台灣分年齡/性別之勞動力參與率 |
| `macro_avg_monthly_salary` | 全台平均經常性薪資中位數統計 |
| `macro_poverty_line_by_city` | 各縣市低收入戶最低生活費標準 |
| `macro_tax_revenue_collection` | 總稅收實徵淨額與年度達成率 |
| `macro_household_income_inequality` | 所得分配五等分位差距 (吉尼係數) |
| `macro_air_quality_avg` | 全國各區域 AQI 平均監測數值 |
| `macro_forest_coverage_tw` | 台灣森林面積百分比與生態遙測數據 |
| `macro_renewable_energy_gen` | 風力、太陽能累計發電量與佔比 |
| `macro_co2_emission_per_capita` | 台灣人均二氧化碳排放國際對比 |
| `macro_river_pollution_index` | 台灣主要河流 RPI 污染指數趨勢 |
| `macro_social_welfare_spending` | 政府社會福利支出佔年度總預算比 |
| `macro_education_budget_alloc` | 教育預算分配 (高等 vs 技職教育) |
| `macro_r_d_to_gdp_ratio` | 研發經費佔國內生產毛額比率排名 |
| `macro_patent_application_total` | 全國專利申請總數與發明專利佔比 |
| `macro_suicide_prevention_stats` | 心理健康預警與諮詢人次統計數據 |
| `macro_traffic_accident_trends` | 交通事故傷亡人數與道路安全指標 |
| `macro_crime_rate_index` | 台灣治安指數與各类刑事案破案率 |
| `macro_internet_penetration_rate` | 家戶寬頻與行動網路普及率統計 |
| `macro_5g_coverage_map` | 5G 基地台建設總量與人口覆蓋率 |
| `macro_waste_recycling_rate` | 台灣資源回收率與廚餘處理統計數據 |
| `macro_sea_level_monitoring` | 台灣沿海海平面上升速度監測數據 |
| `macro_average_life_expectancy` | 台灣男女平均壽命與平均餘命分佈 |
| `macro_gender_pay_gap` | 台灣職場性別薪資差異百分比統計 |
| `macro_real_estate_bubble_index` | 房價所得比與房價負擔能力指數 |
| `macro_national_happiness_rank` | 台灣在世界幸福報告中各指標得分 |

---

## ₿ 6. Web3 與加密貨幣 (20 個工具)
| 工具 ID | 功能描述 |
| :--- | :--- |
| `crypto_btc_realtime` | 比特幣 (BTC) 即時報價與換算 |
| `crypto_eth_realtime` | 以太幣 (ETH) 即時行情與漲跌幅 |
| `crypto_sol_realtime` | Solana (SOL) 即時報價與交易量 |
| `crypto_stablecoin_market_cap` | 穩定幣 (USDT/USDC) 發行量監控 |
| `crypto_fear_greed_index` | 加密貨幣市場恐懼與貪婪指數 |
| `crypto_trending_coins_24h` | 全球 24 小時熱搜幣種排行 |
| `crypto_new_listings_dex` | 去中心化交易所最新上架幣種 |
| `crypto_eth_gas_tracker` | 以太坊即時 Gas 費監控 (Gwei) |
| `crypto_l2_transaction_fees` | Layer2 (Base, Arbitrum) 手續費對比 |
| `crypto_nft_floor_prices` | 熱門 NFT 項目地板價走勢追蹤 |
| `crypto_defi_total_value_locked` | DeFi 協議總鎖倉量 (TVL) 變動 |
| `crypto_bridge_volume_monitor` | 跨鏈橋資金流向與淨流入統計 |
| `crypto_exchange_reserve_proof` | 交易所儲備金證明 (PoR) 數據掃描 |
| `crypto_mining_difficulty_btc` | 比特幣挖礦難度與全網算力統計 |
| `crypto_staking_yield_avg` | ETH 2.0 質押平均年化收益率 |
| `crypto_global_market_cap` | 全球加密貨幣總市值佔標普 500 比 |
| `crypto_bitcoin_dominance` | 比特幣市值佔比 (BTC.D) 與山寨季指標 |
| `crypto_event_calendar` | 代幣解鎖、重大會議、升級日曆 |
| `crypto_hack_alert_monitor` | 鏈上安全事故與協議漏洞預警 |
| `crypto_whale_transaction_tracker` | 巨鯨大額轉帳與交易所淨充值監控 |

---

## 🏁 7. 核心系統工具 (4 個工具)
| 工具 ID | 功能描述 |
| :--- | :--- |
| `get_taiwan_market_health` | 市場多空趨勢與健康度診斷 |
| `get_global_economic_calendar` | 全球重大財經大事行程彙整 |
| `get_taiwan_salary_stats` | 台灣各行業薪資與勞動力報告 |
| `get_cwa_earthquake_report` | 中央氣象署地震即時速報 |

---

## 📋 註：
本字典涵蓋 **334 個** 真實註冊之功能。所有工具 ID 已在 `server.py` 中完成實體化對接。
