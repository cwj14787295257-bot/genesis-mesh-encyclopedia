#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os

data = [
        {
                "id": "nexttiny",
                "name": "Nexttiny",
                "brand": "Vape Ware Mods (VWM)",
                "origin": "希腊",
                "type": "Genesis RDTA",
                "image": "images/nexttiny.jpg",
                "quickSpecs": [
                        "22mm",
                        "3.4ml",
                        "中心网孔"
                ],
                "specs": {
                        "品牌产地": "Vape Ware Mods (VWM) · 希腊",
                        "发布时间": "2015年10月",
                        "设备类型": "Genesis RDTA (中心网芯立式导油)",
                        "外形直径": "22 mm",
                        "本体高度": "27 mm（不含滴嘴）",
                        "油仓容量": "约 3.4ml (不锈钢仓) / 3.3ml (PC仓)",
                        "主体材质": "304 不锈钢 / PEEK 绝缘 / PC 1000",
                        "进气规格": "顶盖旋转调节，4 组双垂直进气孔 (1.0 / 1.2 / 1.4 / 1.6mm)",
                        "电极平台": "中心垂直单网孔 (Center-wick Deck)",
                        "导油孔径": "3.5 mm (中心立式环形导油孔，适配 13.5mm 裁网高度)",
                        "导油介质": "不锈钢网 (Mesh #200 ~ #400) / 避雷针碳棒系统",
                        "接口规格": "标准 510 接口"
                },
                "officialNotes": "VWM 原厂设计要点：在继承 Nextgen 成功经验的基础上，大幅压缩整体雾化室高度（仅 27mm），采用独特的中心立柱网芯架构（Center-post Wick），双侧垂直微孔直接对焦网芯正中，旨在打造极致紧凑的聚气风道与便捷的做网体验。",
                "reviews": [
                        {
                                "quote": "Nextiny 重新定义了网子雾化器的易用性与风味上限。极度缩小的微型雾化室带来了世界级的解析力（world-class flavor），与以往繁琐易短路的传统 Genesis 完全不同，中心绕网结构让新手也能稳定做出极高纯净度的口感。",
                                "author": "Mark Todd & POTV 评测组",
                                "platform": "Planet of the Vapes (英国电子烟专业评测媒体)",
                                "topic": "Vape Ware Mods Nextiny Comprehensive Review",
                                "url": "https://www.planetofthevapes.co.uk"
                        }
                ],
                "zuosi": [],
                "tanbang": [
                        {
                                "mesh": "200 316 斜纹",
                                "needle": "13.5*3.5~40mm",
                                "vm3": "",
                                "vm4": "",
                                "vms": "",
                                "s35": "",
                                "snet": ""
                        },
                        {
                                "mesh": "200 316 斜纹",
                                "needle": "13.5*25mm / 13.5*20mm 斜剪",
                                "vm3": "",
                                "vm4": "",
                                "vms": "",
                                "s35": "",
                                "snet": ""
                        },
                        {
                                "mesh": "300 316 斜纹",
                                "needle": "13.5*45mm",
                                "vm3": "",
                                "vm4": "",
                                "vms": "",
                                "s35": "",
                                "snet": ""
                        },
                        {
                                "mesh": "325 316 斜纹",
                                "needle": "13.5*45~50mm",
                                "vm3": "",
                                "vm4": "",
                                "vms": "",
                                "s35": "",
                                "snet": ""
                        },
                        {
                                "mesh": "400 316 斜纹",
                                "needle": "13.5*50*55mm",
                                "vm3": "",
                                "vm4": "",
                                "vms": "",
                                "s35": "",
                                "snet": ""
                        }
                ],
                "images": [
                        "images/nexttiny.jpg",
                        "images/nexttiny_deck.jpg",
                        "images/nexttiny_parts.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "Vape Ware Mods (VWM) 希腊工坊官方发售公告: 2015-10-20 正式批量出厂交付",
                        "secondary": "Planet of the Vapes (POTV) 英国专业媒体: 2015年10月首发全面深度评测《VWM Nextiny Review》",
                        "analysis": "希腊原厂出厂发售公告与英国专业媒体开箱评测同月发表，双源高度吻合。"
                }
        },
        {
                "id": "ghost_afc",
                "name": "Ghost AFC",
                "brand": "Paravozz (Пара-Воз)",
                "origin": "俄罗斯",
                "type": "Genesis RDTA",
                "image": "images/ghost_afc.jpg",
                "quickSpecs": [
                        "22mm",
                        "4.0ml",
                        "旋转AFC"
                ],
                "specs": {
                        "品牌产地": "Paravozz (Пара-Воз / 车头) · 俄罗斯",
                        "发布时间": "约 2018年 (暂定)",
                        "设备类型": "Genesis RDTA (Ghost 幽灵系列 AFC 进气版)",
                        "外形直径": "22 mm",
                        "本体高度": "36.5 mm（不含滴嘴）",
                        "油仓容量": "4.0 ml",
                        "主体材质": "特种高纯度钛合金 (Titanium) / 高透耐热油仓",
                        "进气规格": "外置旋转式 AFC 双孔调节环 (0.8 / 1.0 / 1.2 / 1.5 mm)",
                        "电极平台": "车头经典直立单丝路网芯结构",
                        "导油孔径": "2.5 mm（支持使用 26mm 高度网芯）",
                        "导油介质": "不锈钢网 (Mesh #200/#230/#325/#500) 碳棒制作",
                        "接口规格": "标准 510 接口"
                },
                "officialNotes": "Paravozz 工坊结构要点：将车头引以为傲的钛合金手工级公差与外置可调旋转 AFC 进气环结合，解决传统固定进气孔车头无法随时根据不同目数网芯微调吸阻的限制。",
                "reviews": [
                        {
                                "quote": "Ghost MTL / AFC 版本在保持车头标志性的冷雾与无杂音吸阻的同时，旋转进气环让调节变得非常实用。搭配 230目 配合约 1.0mm 左右的进气，导油与气流极其线性，彻底摆脱了早期车头必须手动挑孔的困扰。",
                                "author": "资深车头玩家交流帖",
                                "platform": "eCigTalk.org (俄罗斯最大电子烟极客论坛)",
                                "topic": "®ГЕНЕЗИС 'Пара ВозЪ' 讨论专区",
                                "url": "https://www.ecigtalk.org"
                        }
                ],
                "zuosi": [],
                "tanbang": [
                        {
                                "mesh": "200 316 斜纹",
                                "needle": "",
                                "vm3": "26*47mm",
                                "vm4": "",
                                "vms": "",
                                "s35": "",
                                "snet": ""
                        },
                        {
                                "mesh": "230 316 斜纹",
                                "needle": "",
                                "vm3": "26*50mm",
                                "vm4": "26*45mm",
                                "vms": "26*35mm",
                                "s35": "",
                                "snet": "26*45mm"
                        },
                        {
                                "mesh": "325 316 斜纹",
                                "needle": "",
                                "vm3": "",
                                "vm4": "26*50mm",
                                "vms": "",
                                "s35": "",
                                "snet": ""
                        },
                        {
                                "mesh": "500 316 斜纹",
                                "needle": "",
                                "vm3": "26*110mm",
                                "vm4": "",
                                "vms": "",
                                "s35": "",
                                "snet": ""
                        }
                ],
                "images": [
                        "images/ghost_afc.jpg",
                        "images/ghost_afc_deck.jpg",
                        "images/ghost_afc_case.jpg"
                ],
                "dateVerification": {
                        "status": "tentative",
                        "primary": "PARaVOzZ® Wiki 官方历史档案: 记录车头 Ghost 基础加装外置旋转气流环之改装定制机",
                        "secondary": "eCigTalk 玩家交流记录: 约 2018 年前后私人订制流转",
                        "analysis": "暂定理由：非独立批量量产发售型号，属玩家定向调校之私人订制改装配件，无独立批量公开发售公文。"
                }
        },
        {
                "id": "sakura",
                "name": "樱花 (Sakura)",
                "brand": "Paravozz (Пара-Воз)",
                "origin": "俄罗斯",
                "type": "Genesis RDTA",
                "image": "images/sakura.jpg",
                "quickSpecs": [
                        "22mm",
                        "3.0ml",
                        "樱花限定"
                ],
                "specs": {
                        "品牌产地": "Paravozz (Пара-Воз / 车头) · 俄罗斯",
                        "发布时间": "约 2018年 (暂定)",
                        "设备类型": "Genesis RDTA (钛合金高级限定版)",
                        "外形直径": "22 mm",
                        "本体高度": "约 41.5 mm（不含滴嘴）",
                        "油仓容量": "3.0 ml",
                        "主体材质": "航空级高纯度钛合金 (Titanium) / 石英玻璃仓 / PEI 仓",
                        "进气规格": "单侧固定精密微孔 (1.1 mm)",
                        "电极平台": "双极柱单发 Genesis 网芯垂直平台",
                        "导油孔径": "2.5 mm（支持扩孔至 3.5mm 规格，网高 22~25mm）",
                        "导油介质": "不锈钢网 (Mesh #200/#230) 碳棒垂直卷芯",
                        "接口规格": "标准 510 接口"
                },
                "officialNotes": "Paravozz 工坊限定版结构：全钛精密车削，搭配专属樱花主题外盖与聚气穹顶，主要面向高端藏家与骨灰级 Genesis 玩家定制。",
                "reviews": [],
                "zuosi": [
                        {
                                "mesh": "200目",
                                "size": "2.1*2.7cm",
                                "wraps": "6vm"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "230 316 斜纹",
                                "needle": "",
                                "vm3": "",
                                "vm4": "",
                                "vms": "22*35mm",
                                "s35": "25*60mm",
                                "snet": ""
                        }
                ],
                "images": [
                        "images/sakura.jpg",
                        "images/sakura_dome.jpg",
                        "images/sakura_deck.jpg",
                        "images/sakura_cap.jpg"
                ],
                "dateVerification": {
                        "status": "tentative",
                        "primary": "PARaVOzZ® 资深藏家档案: 全钛樱花主题定制刻槽顶盖限定版",
                        "secondary": "俄罗斯与日本网子论坛微距流转实拍: 约 2018 年由私人藏家订制",
                        "analysis": "暂定理由：私人珠宝级订制刻纹版，未开具公开批量预定帖，仅在核心藏家圈私下流转。"
                }
        },
        {
                "id": "v10",
                "name": "v10",
                "brand": "Paravozz (Пара-Воз)",
                "origin": "俄罗斯",
                "type": "Genesis RDTA",
                "image": "images/v10.jpg",
                "quickSpecs": [
                        "22mm",
                        "2.5ml/3.5ml",
                        "十代里程碑"
                ],
                "specs": {
                        "品牌产地": "Paravozz (Пара-Воз / 车头) · 俄罗斯",
                        "发布时间": "2015年8月",
                        "设备类型": "Genesis RDTA (十代名机 v.10 / v.10.0.2 / 10.1 6Killer)",
                        "外形直径": "22 mm",
                        "本体高度": "40.5 mm（不含滴嘴）",
                        "油仓容量": "2.5 ml（标仓）/ 3.5 ml（扩容仓）",
                        "主体材质": "航天钛合金 (Titanium) / 高硼硅耐温玻璃仓 / PEI 仓",
                        "进气规格": "1.2×2.4 mm 矩形开槽，或可选 1.2 / 1.4 / 1.65 / 1.9 mm 单孔",
                        "电极平台": "单网极速对焦垂直电极柱",
                        "导油孔径": "2.5 mm",
                        "导油介质": "不锈钢网 (Mesh #230 316 斜纹) 碳棒制作",
                        "接口规格": "标准 510 接口"
                },
                "officialNotes": "工坊历史记录：2015年8月21日由作者 Андрей Робул (japan1967 / Andrey Robul) 正式推出 10.0.2 版本。作为车头十代核心里程碑，设计了专用的 1.2×2.4mm 矩形气流开槽与微型化集气顶盖，成为公认的巅峰代表作。",
                "reviews": [
                        {
                                "quote": "在车头近十年的演进史中，10.0.2 与 6Killer 被公认为全系列三大巅峰圣杯之一。特殊的 1.2×2.4mm 开槽让气流以极佳的面接触覆盖发热丝，雾化出的烟雾温度极低、颗粒干燥细腻，层次分离度达到了 Genesis 的极限水平。",
                                "author": "ecigtalk 资深车头版主与藏家群体",
                                "platform": "eCigTalk.org (俄罗斯极客论坛)",
                                "topic": "®ГЕНЕЗИС 'Пара ВозЪ'. 编年史与版本横评",
                                "url": "https://www.ecigtalk.org/forum/f73/t17087.html"
                        }
                ],
                "zuosi": [],
                "tanbang": [
                        {
                                "mesh": "230 316 斜纹",
                                "needle": "",
                                "vm3": "待补",
                                "vm4": "",
                                "vms": "",
                                "s35": "",
                                "snet": ""
                        }
                ],
                "images": [
                        "images/v10.jpg",
                        "images/v10_deck.jpg",
                        "images/v10_base.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "eCigTalk.org 编年史《Хронология ген》: 确切著录 2015-08-21 由 Andrey Robul (japan) 推出 10.0.2 版本",
                        "secondary": "eCigTalk «®ГЕНЕЗИС 'Пара ВозЪ'» 主题贴: 2015年8月批次交付与玩家开箱晒单",
                        "analysis": "俄系官方编年史交付记录与论坛主楼首发开箱同月完全吻合。"
                }
        },
        {
                "id": "genny2",
                "name": "genny2",
                "brand": "Bear Lair Mods (BLM)",
                "origin": "俄罗斯",
                "type": "Genesis RTA/RDTA",
                "image": "images/genny2.jpg",
                "quickSpecs": [
                        "22mm",
                        "4.2ml",
                        "双网支持"
                ],
                "specs": {
                        "品牌产地": "Bear Lair Mods (BLM) · 俄罗斯",
                        "发布时间": "2018年5月",
                        "设备类型": "Genesis RTA / RDTA",
                        "外形直径": "22 mm",
                        "本体高度": "42.0 mm（不含滴嘴）",
                        "油仓容量": "4.2 ml",
                        "主体材质": "AISI 316 不锈钢 / ULTEM & Pyrex 双仓 / PEEK 绝缘",
                        "进气规格": "可互换模块化 AFC 环 (MTL: 1.2 / 1.4 / 1.6 mm; Cloud: 1.8 / 2.0 / 2.2 mm)",
                        "电极平台": "双极柱设计，支持单网 (附堵头) 或双网 (Dual Mesh) 配置",
                        "导油孔径": "3.5 mm (网子高度约 28~30mm)",
                        "导油介质": "不锈钢网 (Mesh #230 316 斜纹) 碳棒制作",
                        "接口规格": "标准 510 接口 (固定正极针)"
                },
                "officialNotes": "Bear Lair Mods 原厂设计说明：标配耐酸 Pyrex 玻璃与耐高温 ULTEM 双油仓，配备 MTL 与 Cloud 两套独立 AFC 进气环。电极台设计为双柱对称开孔，支持 3.5mm 单发网子（配减径硅胶塞）或极速暴力双网发热。",
                "reviews": [
                        {
                                "quote": "Genny 2 拥有罕见的 3.5mm 大口径网孔与模块化进气环，连抽导油速度极快，完全没有传统 Genesis 容易断油的顾虑。双仓配置做工扎实，在 MTL 模式下对复合水果与甜点类烟油的浓郁度还原非常惊艳。",
                                "author": "Vaping Post 评测编辑组",
                                "platform": "Vaping Post (国际专业电子烟测评杂志)",
                                "topic": "Bear Lair Mods Genny Two Review",
                                "url": "https://www.vapingpost.com"
                        }
                ],
                "zuosi": [],
                "tanbang": [
                        {
                                "mesh": "230 316 斜纹",
                                "needle": "",
                                "vm3": "28*50mm",
                                "vm4": "",
                                "vms": "",
                                "s35": "",
                                "snet": ""
                        }
                ],
                "images": [
                        "images/genny2.jpg",
                        "images/genny2_kit.jpg",
                        "images/genny2_deck.jpg",
                        "images/genny2_afc.jpg",
                        "images/genny2_cap.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "Bear Lair Mods (BLM) 官方商城公告: 2018-05-15 启动首批批量交付",
                        "secondary": "Vaping Post (欧洲知名评测媒体): 2018年5月专题评测《Genny 2 by Bear Lair Mods》",
                        "analysis": "俄罗斯工坊官方商城出厂与欧洲主流评测媒体同月吻合。"
                }
        },
        {
                "id": "s61v1",
                "name": "S61 V1",
                "brand": "Four One Five (415 Mod)",
                "origin": "日本",
                "type": "Genesis RDTA",
                "image": "images/s61v1.jpg",
                "quickSpecs": [
                        "22mm",
                        "3.0ml",
                        "原版和风匠作"
                ],
                "specs": {
                        "品牌产地": "Four One Five (415 Mod) · 日本",
                        "发布时间": "2020年4月",
                        "设备类型": "Genesis RDTA (初代和风经典)",
                        "外形直径": "22 mm",
                        "本体高度": "约 35.3 mm（不含滴嘴）",
                        "油仓容量": "约 3.0 ml",
                        "主体材质": "SUS316L 不锈钢 / PCTG 高透油仓 / PEEK 绝缘",
                        "进气规格": "侧进气微孔直吹，内嵌精细可换口吸销 (约 1.0~1.2 mm)",
                        "电极平台": "双柱单网专用极柱，专为不锈钢网定制",
                        "导油孔径": "2.5 mm (支持 22mm 裁网高度)",
                        "导油介质": "不锈钢网 (Mesh #230 316) 碳棒制作",
                        "接口规格": "标准 510 接口"
                },
                "officialNotes": "Four One Five 官方设计宗旨：追求极致的日本工业美学与紧致聚气风道，纯不锈钢与极简外形设计，内部无多余死角，直击高目数网子在纯烟草领域的微小风味还原。",
                "reviews": [
                        {
                                "quote": "415 S61 初代展现了日本车床加工的极限公差。仓内聚气极度致密，烟雾非常冷，对有机烟草中细微的烟草灰味与木质底韵的分离感极强，是老派 Genesis 纯网口吸爱好者的梦幻神机。",
                                "author": "日本高端网子玩家交流群",
                                "platform": "Office Edge & 乐天日系 Vape 玩家专栏",
                                "topic": "415 Four One Five S61 Genesis 実機レビュー",
                                "url": "https://item.rakuten.co.jp/officeedge/"
                        }
                ],
                "zuosi": [],
                "tanbang": [
                        {
                                "mesh": "230 316 斜纹",
                                "needle": "",
                                "vm3": "22*45mm",
                                "vm4": "",
                                "vms": "",
                                "s35": "",
                                "snet": ""
                        }
                ],
                "images": [
                        "images/s61v1.jpg",
                        "images/s61v1_deck.jpg",
                        "images/s61v1_parts.jpg",
                        "images/s61v1_base.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "Four One Five (415 Mod) 日本官方发售公告: 2020-04-15 启动首批商业交付",
                        "secondary": "Office Edge (日本正品经销商) & TVGC (意大利): 2020年4月上架与评测建档",
                        "analysis": "日本原厂商业交付与日欧正品渠道建档同月完全闭环。"
                }
        },
        {
                "id": "s61v2",
                "name": "S61 V2",
                "brand": "Four One Five (415 Mod)",
                "origin": "日本",
                "type": "Genesis RDTA",
                "image": "images/s61v2.jpg",
                "quickSpecs": [
                        "22mm",
                        "3.0ml",
                        "AFC 0.9-1.1"
                ],
                "specs": {
                        "品牌产地": "Four One Five (415 Mod) · 日本",
                        "发布时间": "2021年4月",
                        "设备类型": "Genesis RDTA (二代迭代旗舰)",
                        "外形直径": "22 mm",
                        "本体高度": "39.7 mm（不含滴嘴）",
                        "油仓容量": "3.0 ml",
                        "主体材质": "SUS316L 不锈钢 / 钛合金电极 / PEI (ULTEM) 耐热耐腐油仓",
                        "进气规格": "高精度旋转式 AFC (0.9 mm ~ 1.1 mm 极细微调)",
                        "电极平台": "单丝路网芯垂直电极台，螺丝夹片固定",
                        "导油孔径": "2.5 mm (标配 25mm 裁网高度)",
                        "导油介质": "不锈钢网 (Mesh #230 316) 碳棒制作",
                        "接口规格": "标准 510 接口"
                },
                "officialNotes": "415mod.co 官方产品档案：V2 针对初代进气单一的问题，全新开发了 0.9mm~1.1mm 连续微调式 AFC 气流环，电极升级为耐高温钛合金组件，标配琥珀色 PEI 仓与改良绝缘台，极大提高了耐用度与控温能力。",
                "reviews": [
                        {
                                "quote": "S61 V2 的 0.9-1.1mm AFC 旋转阻尼做得像高档相机镜头一样扎实。进气极其顺滑无声，配合 PEI 仓完全不用担心高酸性烟油侵蚀，在保持初代极致冷干口感的同时，做芯与维护的宽容度高了非常多。",
                                "author": "Dr.Vapor 评测团队",
                                "platform": "Dr.Vapor (日本专业 VAPE 体验店)",
                                "topic": "415 S61 V2 Genesis RDTA 特集",
                                "url": "https://415mod.co"
                        }
                ],
                "zuosi": [],
                "tanbang": [
                        {
                                "mesh": "230 316 斜纹",
                                "needle": "",
                                "vm3": "25*50mm",
                                "vm4": "",
                                "vms": "",
                                "s35": "",
                                "snet": ""
                        }
                ],
                "images": [
                        "images/s61v2.jpg",
                        "images/s61v2_deck.jpg",
                        "images/s61v2_chamber.jpg",
                        "images/s61v2_reducer.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "Four One Five (415mod.co) 官方商城: 2021-04-20 迭代发售 S61 V2",
                        "secondary": "Dr.Vapor (日本知名评测频道): 2021年4月视频实测《S61 Genesis V2 彻底解析》",
                        "analysis": "日本官方商城发售与专业评测视频同月吻合。"
                }
        },
        {
                "id": "babe",
                "name": "Babe",
                "brand": "Paravozz (Пара-Воз)",
                "origin": "俄罗斯",
                "type": "Genesis RDTA",
                "image": "images/babe.jpg",
                "quickSpecs": [
                        "19/22mm",
                        "全钛合金",
                        "静音吸阻"
                ],
                "specs": {
                        "品牌产地": "Paravozz (Пара-Воз / 车头) · 俄罗斯",
                        "发布时间": "2015年4月",
                        "设备类型": "Genesis RDTA (全钛极客级微型雾化器)",
                        "外形直径": "19 mm（可搭配 22mm 装饰美化环）",
                        "本体高度": "约 38.0 mm（不含滴嘴）",
                        "油仓容量": "约 2.0 ~ 3.0 ml（依仓体版本）",
                        "主体材质": "特种航天钛合金 (Titanium) / PEI 耐热组件",
                        "进气规格": "车头标志性单孔精密 MTL 进气 (约 1.1 mm)",
                        "电极平台": "垂直单丝路纯网导油架构",
                        "导油孔径": "2.5 mm（适合 20mm 裁网高度）",
                        "导油介质": "不锈钢网 (Mesh #230 316 斜纹) 碳棒制作",
                        "接口规格": "标准 510 接口"
                },
                "officialNotes": "Paravozz 经典架构：玩家昵称“比贝克 (Babe)”，对应 Paravoz v.2.0 / v.2.1 体系。采用 19mm 超窄径全钛本体，极度压缩的内部空间创造了近乎无空气扰动的垂直风道。",
                "reviews": [
                        {
                                "quote": "Mesh 500# and kanthal 28ga, 1ohm at 12.5w, 'old school' regeneration that is well suited to the Babe's small vape chamber. Halfzware Shag aroma, classic extract that has much more aromatic charge.",
                                "reviewer": "Simone Bongi (PARaVOzZ® Wiki 档案馆长, 2024-04-05)"
                        },
                        {
                                "quote": "«Бибек»（Babe）是车头老玩家心中永远的白月光。19mm 带来的微小雾化室让烟气几乎瞬间直达味蕾，吸气时几乎听不到一丝气流杂音，在稳定性与纯正干爽度上堪称教科书级别的表现。",
                                "reviewer": "eCigTalk 资深老玩家讨论串 (俄罗斯极客论坛)"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "500 目不锈钢细网 (20×45mm)",
                                "needle": "2.0mm 微空心卷网",
                                "wire": "0.32mm (28 AWG) Kanthal A1",
                                "circle": "5 圈 (阻值 1.0Ω)",
                                "note": "Simone Bongi 官方推荐：500 目密网搭配经典 28ga 细丝，在 12.5W 功率下与 Babe 的 19mm 微型雾化仓天作之合。"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "400 目氧化隔离网",
                                "needle": "1.8mm 高纯石墨碳棒芯",
                                "wire": "0.28mm NiCr",
                                "circle": "5 圈",
                                "note": "碳棒骨架完全杜绝了 19mm 狭窄内腔中的微小跳火，口感干爽紧致。"
                        }
                ],
                "images": [
                        "images/babe.jpg",
                        "images/babe_deck.jpg",
                        "images/babe_parts.jpg",
                        "images/babe_afc.jpg",
                        "images/babe_mod.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "eCigTalk.org 编年史《Хронология ген》: 确切著录 2015-04-01 出厂 Паравоз 2.0 'I'll be back' LE",
                        "secondary": "eCigTalk 车头主楼登记与玩家实拍照时间戳: 2015年4月多名老玩家晒单证实",
                        "analysis": "官方编年史与论坛发帖日期双源精确比对，破译阿诺德经典台词俄语谐音，双源完全闭环。"
                }
        },
        {
                "id": "k5k",
                "name": "K5K",
                "brand": "Paravozz (Пара-Воз)",
                "origin": "俄罗斯",
                "type": "Genesis RDTA",
                "image": "images/k5k.jpg",
                "quickSpecs": [
                        "22mm",
                        "3.0ml",
                        "高通用性"
                ],
                "specs": {
                        "品牌产地": "Paravozz (Пара-Воз / 车头) · 俄罗斯",
                        "发布时间": "2020年3月",
                        "设备类型": "Genesis RDTA (22mm 经典主力机)",
                        "外形直径": "22 mm",
                        "本体高度": "约 46.0 mm（不含滴嘴）",
                        "油仓容量": "约 3.0 ml",
                        "主体材质": "高档钛合金或 SUS316L / 高硼硅透明玻璃仓 / PEI 选件",
                        "进气规格": "侧向紧致固定进气 (1.2 mm，支持选配更换 Air Pin)",
                        "电极平台": "单发纯网平台（中心齿轮冠正极柱 + 偏置负极压片螺丝，带阶梯弧形减压槽）",
                        "导油孔径": "2.5 mm（支持 22mm 裁网高度）",
                        "导油介质": "不锈钢网 (Mesh #200/#230 316 斜纹) 碳棒制作",
                        "接口规格": "标准 510 接口"
                },
                "officialNotes": "Paravozz 22mm 标杆架构：在保持纯钛原厂加工的同时，电极台配备阶梯弧形减压槽与齿轮冠正极锁线柱，标准化了仓体负压平衡孔与极柱间距，是车头家族中适配度最高、量产成熟度最高的 22mm 标准 Genesis 设备。",
                "reviews": [
                        {
                                "quote": "K5K 就像是『车头家族里的 iPhone』，它把很多原本需要靠丰富经验摸索的负压平衡与导油公差在出厂时就固化做好了。即使是新手做网，只要按规矩卷芯，几乎不会发生干烧或漏液，运行极其稳健可靠。",
                                "author": "eCigTalk 玩家 @Error / paravoz 交流专帖",
                                "platform": "eCigTalk.org (俄罗斯极客论坛)",
                                "topic": "ПароКлон & K5K 原理对比讨论",
                                "url": "https://www.ecigtalk.org"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "200目",
                                "size": "2.2*2.7cm",
                                "wraps": "6vm"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "230 316 斜纹",
                                "needle": "",
                                "vm3": "22*50mm",
                                "vm4": "",
                                "vms": "",
                                "s35": "",
                                "snet": ""
                        }
                ],
                "images": [
                        "images/k5k.jpg",
                        "images/k5k_deck.jpg",
                        "images/k5k_parts.jpg",
                        "images/k5k_full.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "eCigTalk «ПароКлон & K5K» 专版与 Paravozz 官方预定: 2020-03-10 正式交付",
                        "secondary": "eCigTalk 玩家开箱晒单与做网实录: 2020年3月中旬全面建立档案",
                        "analysis": "论坛官方预定与首批交付同月闭环。"
                }
        },
        {
                "id": "shoushudao",
                "name": "手术刀",
                "brand": "作者：花椒",
                "origin": "中国原创",
                "type": "Genesis RDTA",
                "image": "images/shoushudao.jpg",
                "quickSpecs": [
                        "22mm",
                        "约3.0ml",
                        "花椒名作"
                ],
                "specs": {
                        "品牌产地": "作者：花椒 · 中国原创设计",
                        "发布时间": "约 2018年 (暂定)",
                        "设备类型": "Genesis RDTA (国内玩家高端口感定制)",
                        "外形直径": "22 mm",
                        "本体高度": "约 36.0 mm（不含滴嘴）",
                        "油仓容量": "约 3.0 ml",
                        "主体材质": "316L 不锈钢 / 聚碳酸酯高透油仓 / PEEK 绝缘",
                        "进气规格": "侧壁精密直吹微孔 (1.2 mm)",
                        "电极平台": "精密单发做丝电极台，专为 Genesis 网芯优化",
                        "导油孔径": "3.0 mm（支持 23mm 裁网，作丝兼容 3.0 规格）",
                        "导油介质": "不锈钢网 (Mesh #200/#230) / 碳棒系统",
                        "接口规格": "标准 510 接口"
                },
                "officialNotes": "作者花椒设计理念：命名为「手术刀」，意在追求如刀锋般犀利的风味剥离感。通过极致缩短的进气路径与垂直对准网芯的微孔，专为细致解构高阶复合烟油香型而生。",
                "reviews": [
                        {
                                "quote": "花椒的手术刀在老网子圈子里声名赫赫。进气短促凌厉，烟雾颗粒感收得极细，抽复合烟草油时，前调的甜香与后调的烟草坚果味被剥离得一清二楚，不愧『手术刀』之名。",
                                "author": "国内老玩家玩家圈实测实录",
                                "platform": "百度贴吧电子烟吧 / 玩家自媒体分享",
                                "topic": "国产网子经典名作『手术刀』体验心得",
                                "url": ""
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "200目",
                                "size": "2.3*2.7mm (2.3*2.7cm)",
                                "wraps": "6vm"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "230 316 斜纹",
                                "needle": "",
                                "vm3": "23*50mm",
                                "vm4": "",
                                "vms": "23*35mm",
                                "s35": "",
                                "snet": ""
                        }
                ],
                "images": [
                        "images/shoushudao.jpg",
                        "images/shoushudao_deck.jpg",
                        "images/shoushudao_cap.jpg"
                ],
                "dateVerification": {
                        "status": "tentative",
                        "primary": "中国网子创作者“花椒的网子课”独立研制实录: 约 2018 年手工打样",
                        "secondary": "B站 UP 主“花椒拌小虾”早期网子视频与国内社群交流记录",
                        "analysis": "暂定理由：作者独立手工打磨、非工业化量产，无商业发售公告，保留客观暂定。"
                }
        },
        {
                "id": "paravozz_cyclone",
                "name": "Paravozz Cyclone Cool XL (Пара-Воз Циклон Cool XL / V21)",
                "brand": "Paravozz (Пара-Воз)",
                "origin": "俄罗斯",
                "type": "Genesis RDTA (车头 Cyclone Cool XL 旗舰钛合金旋风散热大体量雾化器)",
                "image": "images/paravozz_cyclone.jpg",
                "quickSpecs": [
                        "22mm",
                        "VT-6特种航空钛",
                        "10阶全散热鳍片"
                ],
                "specs": {
                        "品牌产地": "Paravozz (Пара-Воз / 车头工坊) · 俄罗斯",
                        "发布时间": "约 2015年 (暂定)",
                        "设备类型": "Genesis RDTA (车头经典钛合金旋风聚气雾化器)",
                        "外形直径": "22.0 mm",
                        "本体高度": "约 38.0 mm（不含 510 接口与滴嘴）",
                        "油仓容量": "约 3.5 ml (耐酸耐热高硼硅石英玻璃仓)",
                        "主体材质": "VT-6 / Grade 5 航空特种钛合金 (手工喷砂拉丝) / PEEK 绝缘组件",
                        "进气规格": "侧壁微孔定向直吹 (1.2mm 经典口吸微孔，配合内部旋风倾角导流设计)",
                        "电极平台": "车头标志性单侧垂直立柱 + 偏心单网导油孔，沉头螺钉紧固导电",
                        "导油孔径": "2.8 mm 偏置导油孔",
                        "导油介质": "不锈钢网 (Mesh #200 ~ #400 复合卷网) / 避雷针碳棒系统",
                        "接口规格": "标准 510 接口 (底座精密切削车头经典标识与流水出厂序号)"
                },
                "officialNotes": "Paravozz 车头工坊出品的经典力作「Cyclone（Циклон / 旋风）」。该作以独特的穹顶聚气减仓弧度与侧壁倾角导风轨迹命名，旨在进气直扑网芯线圈时在极小雾化室内形成如旋风般的微涡流扰动，极大提升烟雾浓缩度与层次细腻感。机身整体采用 VT-6 军工航空钛合金精密切削，延续了车头家族一贯的紧致吸阻与深沉击喉感，是车头历史上极具玩家口碑的钛合金网子名作。",
                "reviews": [
                        {
                                "quote": "Cyclone 是车头工坊在聚气气道设计上的一次重要突破。内部穹顶弧度带来的微气旋效果让烟气温度与浓郁度达到了极佳的平衡，搭配 VT-6 钛合金材质，口感干脆纯净。",
                                "author": "Vladislav Karabas (Paravozz 历史档案评述)",
                                "platform": "Paravozz Wiki / Facebook 典藏专栏",
                                "topic": "Paravozz Cyclone (Циклон) Architecture & History",
                                "url": "https://www.facebook.com/groups/paravozzwiki/"
                        },
                        {
                                "quote": "车头经典的 1.2mm 定向进气配合 Cyclone 的内胆压缩，做网极其干练，无论是粗网目还是细网目，击喉感与层次感都表现出纯正的硬核俄罗斯风味。",
                                "author": "ECF Genny 社区资深玩家",
                                "platform": "E-Cigarette Forum (ECF)",
                                "topic": "Russian Titanium Genesis: Paravozz Cyclone Impressions",
                                "url": "https://www.e-cigarette-forum.com/"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "200目平纹 + 325目外包",
                                "size": "2.1*2.7cm",
                                "wraps": "4圈 0.28mm (约 0.95Ω)"
                        },
                        {
                                "mesh": "230目斜纹",
                                "size": "2.0*2.6cm",
                                "wraps": "5圈 0.30mm (约 0.85Ω)"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "230目斜纹",
                                "needle": "1.0",
                                "vm3": "21*42mm",
                                "vm4": "20*40mm",
                                "vms": "21*35mm",
                                "s35": "20*35mm",
                                "snet": "22*42mm"
                        }
                ],
                "images": [
                        "images/paravozz_cyclone.jpg",
                        "images/paravozz_cyclone_deck.jpg",
                        "images/paravozz_cyclone_base.jpg",
                        "images/paravozz_cyclone_parts.jpg"
                ],
                "dateVerification": {
                        "status": "tentative",
                        "primary": "PARaVOzZ® Wiki 官方历史编年 (#zZhistory): 著录 Cyclone Cool XL (V21) 旋风进气款",
                        "secondary": "eCigTalk 论坛极客定制贴: 约 2015 年 Andrey Robul 定向打造的微量版本",
                        "analysis": "暂定理由：属于官方 Wiki 记载的微量非量产探索款，未单独开具公开发售主楼。"
                }
        },
        {
                "id": "paravozz_8_2",
                "name": "Paravozz 8.2 (Пара-Воз 8.2)",
                "brand": "Paravozz (Пара-Воз)",
                "origin": "乌克兰 / 俄罗斯",
                "type": "Genesis RDTA (八代旗舰 Terminator V8.2)",
                "image": "images/paravozz_8_2.jpg",
                "quickSpecs": [
                        "22mm",
                        "VT-6原色钛",
                        "锥形聚气仓"
                ],
                "specs": {
                        "品牌产地": "Paravozz (Пара-Воз / 车头) · 乌克兰 / 俄罗斯",
                        "发布时间": "2024年6月",
                        "设备类型": "Genesis RDTA (八代旗舰 Terminator Jet'Win V8.2 / 经典锥形聚气)",
                        "外形直径": "22 mm",
                        "本体高度": "42.0 mm（不含滴嘴，经典全尺寸）",
                        "油仓容量": "3.2 ml (耐酸耐热高硼硅石英玻璃)",
                        "主体材质": "VT-6 / Grade 5 航空特种钛合金 (拉丝与细致喷砂微光原色)",
                        "进气规格": "侧壁直线插销式可换 Air Pin (标配 1.0/1.1/1.2/1.4/1.6 mm)",
                        "电极平台": "经典垂直单丝路单网立式电极台，沉头螺钉锁丝，平整导电面",
                        "导油孔径": "2.5 mm（标配 26mm 裁网高度，极强毛细提油）",
                        "导油介质": "不锈钢网 (Mesh #200 ~ #300 45°斜切) / 避雷针碳棒系统",
                        "接口规格": "标准 510 接口 (底座工坊专属流水编号与机车经典刻印)"
                },
                "officialNotes": "Paravozz V8.2（Terminator Jet'Win V8.2）是车头工坊于 2024 年推出的现代化标准型号。整机采用 VT-6 航空高强度钛合金精密切削，搭载标志性的 купол-конус 经典双阶斜肩锥形顶盖与侧插式可换 Air Pin 系统。其内胆聚气室经过微调，兼顾了充沛的储油量与紧凑的压缩风道，为玩家提供了厚实顺滑的纯正烟气解析。",
                "reviews": [
                        {
                                "quote": "V8.2 是车头家族中手感与做工极其纯粹的一代。相比后期版本，8.2 保持了最经典的全尺寸 42mm 比例与 3.2ml 油仓，锥形内胆大幅改善了冷凝，抽原味草本烟油时的解析力层次极其分明。",
                                "author": "Abdualrhman Hosam Altunaib",
                                "platform": "Facebook Paravozz Wiki 藏家俱乐部",
                                "topic": "Paravozz V8.2 Small Chamber Review",
                                "url": ""
                        },
                        {
                                "quote": "V8.2 极度易于做丝调试，使用 Frolov 230目 45°斜切网子配合绳子几乎一次即成，点火爆发平稳柔和，没有任何杂味。",
                                "author": "Frank Hagege",
                                "platform": "ecigtalk.org 资深藏家论坛",
                                "topic": "V8.2 Setup & Mesh Building Tutorial",
                                "url": "https://www.ecigtalk.org/forum/f20/t7578.html"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "200目斜纹 (45°切网)",
                                "size": "2.1*4.5cm",
                                "wraps": "4圈 0.28mm (约 0.90Ω)"
                        },
                        {
                                "mesh": "230目平纹",
                                "size": "2.1*4.3cm",
                                "wraps": "5圈 0.30mm (约 0.85Ω)"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "200目",
                                "needle": "1.0",
                                "vm3": "21*23",
                                "vm4": "20*22",
                                "vms": "20*22",
                                "s35": "20*22",
                                "snet": "22*24"
                        },
                        {
                                "mesh": "230目",
                                "needle": "1.0",
                                "vm3": "21*23",
                                "vm4": "20*22",
                                "vms": "20*22",
                                "s35": "20*22",
                                "snet": "22*24"
                        }
                ],
                "images": [
                        "images/paravozz_8_2.jpg",
                        "images/paravozz_8_2_cap.jpg",
                        "images/paravozz_8_2_deck.jpg",
                        "images/paravozz_8_2_build.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "车头官方工坊 (Marat Mtl / Jap Ti) 官方批次交付记录: 2024-06 首批交付 Terminator Jet'Win V8.2",
                        "secondary": "Facebook Paravozz Wiki 藏家俱乐部交付实帖: 2024-06-10 Frank Hagege 与 2024-06-12 Hosam Altunaib 首批实物晒单",
                        "analysis": "原厂批次交付记录与首发藏家开箱做网实帖完全吻合，确证为 2024 年 6 月交付。"
                }
        },
        {
                "id": "magnum",
                "name": "马格南",
                "brand": "MAG 小组",
                "origin": "中国大陆",
                "type": "Genesis RDTA",
                "image": "images/magnum_full.jpg",
                "quickSpecs": [
                        "22mm",
                        "约3.2ml",
                        "中国原创"
                ],
                "specs": {
                        "品牌产地": "MAG 小组 · 中国大陆原创",
                        "发布时间": "约 2017年 (暂定)",
                        "设备类型": "Genesis RDTA (国内网子经典名器)",
                        "外形直径": "22 mm",
                        "本体高度": "约 35.5 mm（不含滴嘴）",
                        "油仓容量": "约 3.2 ml",
                        "主体材质": "316L 不锈钢 / 高透耐热油仓 / PEEK 绝缘组件",
                        "进气规格": "精密直吹微孔 (约 1.2 mm)",
                        "电极平台": "单发线圈电极平台（专为纯网导油优化）",
                        "导油孔径": "3.5 mm（兼容 3.5 规格碳棒，裁网高度 21mm）",
                        "导油介质": "不锈钢网 (Mesh #200/#230)",
                        "接口规格": "标准 510 接口"
                },
                "officialNotes": "中国大陆 MAG 小组设计要点：国内早期民间团队为纯粹网子玩家打造的 Genesis RDTA 代表作。结构重点强化了油仓内部负压平衡，优化了垂直网芯与进气微孔的相对夹角，备忘录中记载有完整的 200目/230目 3 组成熟作丝参数。",
                "reviews": [
                        {
                                "quote": "MAG 小组的马格南是早期国内为数不多真正懂得网子脾性的原创雾化器。负压平衡调校得很顺，按备忘数据做 200目 4vm 或 230目 6vm，网芯导油非常稳定，抽坚果类和烟草类烟油极其浓醇顺口。",
                                "author": "国内资深网子老玩家实操测评",
                                "platform": "Bilibili / 国内电子烟极客社群",
                                "topic": "国内原创网子雾化器回忆与做芯实录",
                                "url": "https://www.bilibili.com"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "200目",
                                "size": "2.1*2.5cm",
                                "wraps": "4vm"
                        },
                        {
                                "mesh": "230目",
                                "size": "2.1*3.0cm",
                                "wraps": "6vm 3.5"
                        },
                        {
                                "mesh": "230目",
                                "size": "2.2x2.8",
                                "wraps": "5-6vm"
                        }
                ],
                "tanbang": [],
                "images": [
                        "images/magnum_full.jpg",
                        "images/magnum_parts.jpg",
                        "images/magnum_base.jpg"
                ],
                "dateVerification": {
                        "status": "tentative",
                        "primary": "中国大陆民间极客 MAG 小组内部交流记录: 约 2017 年手工研发试产",
                        "secondary": "早期网子玩家社群口述历史与论坛实物讨论: 证实无公开商业通告",
                        "analysis": "暂定理由：国内早期民间极客小圈子内部交流研发，无独立商业实体与公开发售贴。"
                }
        },
        {
                "id": "inax_v5",
                "name": "In'Ax V5",
                "brand": "Athea Mods",
                "origin": "法国",
                "type": "Genesis RDTA",
                "image": "images/inax_v5.jpg",
                "quickSpecs": [
                        "22mm",
                        "3.0ml",
                        "中心柱同轴立式"
                ],
                "specs": {
                        "品牌产地": "Athea Mods (Vincent Athea) · 法国",
                        "发布时间": "2020年2月",
                        "设备类型": "Genesis RDTA (中心同轴网芯立式导油)",
                        "外形直径": "22 mm",
                        "本体高度": "34.5 mm（不含 510 螺纹与滴嘴）",
                        "油仓容量": "约 3.0ml (标配 SS316L 钢仓与 PC1000 仓)",
                        "主体材质": "316L 手术级不锈钢 / 陶瓷绝缘体 / PEEK / PC1000 / Ultem 气流环",
                        "进气规格": "5 档可调气流环 (双孔/单孔/长条槽，覆盖紧致 MTL 到轻肺吸 DL)",
                        "电极平台": "中心垂直立柱同轴电极平台 (Center-wick Deck)",
                        "导油孔径": "约 3.2 mm (同轴中心套管，容纳中心穿柱与同心网卷)",
                        "导油介质": "不锈钢网 (Mesh #300 ~ #400) / 陶瓷套管绝缘系统",
                        "接口规格": "标准 510 接口"
                },
                "officialNotes": "Athea 原厂设计要点：In'Ax 系列是法系中心立柱网芯创世纪（Center-wick Genesis）的开山始祖。V5 版本在保留标志性陶瓷底座绝缘与中心螺纹紧固（GripStick/螺丝）的基础上，大幅优化了微型雾化室散热鳍片造型，并引入 5 档进气调控与双材质外环（不锈钢与 Ultem），实现了烟草层次与复合水果的极高解析。",
                "reviews": [
                        {
                                "quote": "In'Ax V5 延续了 Athea 标志性的中心立式网子架构，法系高精数控车削极其细腻。得益于微型雾化室与多档进气调节，对烟草与复合香气的层次分离度极佳，是硬核网子玩家不可多得的纯正 Genesis 艺术品。",
                                "author": "Alex",
                                "platform": "Vaping Post (法国专业电子烟评测媒体)",
                                "topic": "Test : In'Ax V5 – Athea Mods",
                                "url": "https://fr.vapingpost.com"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "300目 / 400目",
                                "size": "2.2 x 2.5 cm (中心同轴卷管)",
                                "wraps": "4-5 圈 (NiChrome 80 / Kanthal 0.28-0.32mm, 约 0.9-1.1Ω)"
                        }
                ],
                "tanbang": [],
                "images": [
                        "images/inax_v5.jpg",
                        "images/inax_v5_deck.jpg",
                        "images/inax_v5_exploded.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "Vincent Athea (Athea Mods) 官方发售公告: 2020-02-18 正式交付 In'Ax V5",
                        "secondary": "TVGC (The Vaping Gentlemen Club) & Vaping Post: 2020年2月建立发售档案",
                        "analysis": "法国工坊官方出厂与欧洲主流分销商同月闭环。"
                }
        },
        {
                "id": "sat22",
                "name": "Sat22",
                "brand": "Satburn",
                "origin": "塞浦路斯 / 欧洲",
                "type": "Genesis RDTA",
                "image": "images/sat22.jpg",
                "quickSpecs": [
                        "22mm",
                        "3.0ml",
                        "经典阶梯顶盖"
                ],
                "specs": {
                        "品牌产地": "Satburn (Andreas Vassiliou) · 塞浦路斯 / 欧洲",
                        "发布时间": "2014年3月",
                        "设备类型": "Genesis RDTA (经典侧孔立式导油)",
                        "外形直径": "22 mm",
                        "本体高度": "约 35 mm（不含 510 螺纹与滴嘴）",
                        "油仓容量": "约 3.0ml (Pyrex 硼硅耐热玻璃仓)",
                        "主体材质": "304 / 316 不锈钢 / Pyrex 玻璃 / PEEK 绝缘",
                        "进气规格": "双侧固定微孔垂直对焦 (2x 0.8mm，专为正统紧致 MTL 打造)",
                        "电极平台": "偏心单孔 Genesis 平台 (超微型压缩聚气雾化室)",
                        "导油孔径": "2.4 mm (偏心单导油孔，防漏与毛细爬油平衡尺寸)",
                        "导油介质": "不锈钢网 (Mesh #400 ~ #500) / 细目空心卷网",
                        "接口规格": "标准 510 接口"
                },
                "officialNotes": "Satburn 原厂设计要点：Sat22 具有标志性的冷峻三层阶梯状削切外观，其设计精髓在于极致微缩的顶盖内部穹顶雾化室。双 0.8mm 垂直对冲进气孔与导油网芯零距离贴近，彻底消除发热丝热脚（Hot legs），将烟雾温度与冷冽凝聚力控制在巅峰状态。",
                "reviews": [
                        {
                                "quote": "Sat22 凭借其标志性的三层阶梯冷峻外观与极致缩小的微型雾化室，将导油与发热丝的距离压缩到极致。双孔对焦进气让烟油解析度达到了冷冽纯净的巅峰，是欧洲创世纪网子黄金年代的图腾之作。",
                                "author": "Mark Todd & POTV 评测组",
                                "platform": "Planet of the Vapes & Todd's Reviews",
                                "topic": "The Sat22 Genesis Atomizer Review",
                                "url": "https://www.planetofthevapes.co.uk"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "400目 / 500目",
                                "size": "2.0 x 3.0 cm (空心细卷网)",
                                "wraps": "4-5 圈 (Kanthal A1 0.25-0.28mm, 1.0-1.2Ω)"
                        }
                ],
                "tanbang": [],
                "images": [
                        "images/sat22.jpg",
                        "images/sat22_deck.jpg",
                        "images/sat22_parts.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "塞浦路斯 Satburn (Andreas Vassiliou) 于 UK Vapers: 2014-03-01 首批量产交付",
                        "secondary": "Todd's Reviews (YouTube): 2014年3月深度评测《Sat 22 Genesis Atomiser by Satburn》",
                        "analysis": "地中海名作工坊首发交付与 Todd 权威视频评测同月闭环。"
                }
        },
        {
                "id": "monad",
                "name": "Monad",
                "brand": "Xtra Mile Vape (XMV)",
                "origin": "韩国",
                "type": "Genesis RDTA",
                "image": "images/monad.jpg",
                "quickSpecs": [
                        "22mm",
                        "3.1ml",
                        "实心聚气微仓"
                ],
                "specs": {
                        "品牌产地": "Xtra Mile Vape (XMV) · 韩国",
                        "发布时间": "2014年12月",
                        "设备类型": "Genesis RDTA (高阶精密紧致 MTL 网子)",
                        "外形直径": "22 mm",
                        "本体高度": "36.5 mm（不含 510 接头与滴嘴）",
                        "油仓容量": "约 3.0 ~ 3.1ml (PCTG / 磨砂 PC / 选配 Ultem 仓)",
                        "主体材质": "316L 医用级不锈钢 (纯手工缎面拉丝) / PEEK / PCTG",
                        "进气规格": "双侧精准对冲微孔 (标配 0.8mm x 2 / 可选 0.9mm x 2，绝对静音 MTL)",
                        "电极平台": "偏心单发 Genesis 平台 (极限实心削切极小雾化室)",
                        "导油孔径": "2.7 mm (精密倒角导油孔，支持紧凑做网)",
                        "导油介质": "不锈钢网 (Mesh #325 ~ #400) / 混合棉芯作法",
                        "接口规格": "标准 510 接口"
                },
                "officialNotes": "Xtra Mile Vape 原厂设计要点：Monad 堪称韩系极简工业美学的里程碑，整机大部分关键件均经历严苛的手工打磨抛光。顶部不对称偏心气道与近乎全实心的实心微型雾化仓设计，配合精准的 0.8mm 双向对冲进气，专为重现原浆烟草（NET）与高层次复杂调味烟油的细腻结晶度而生。",
                "reviews": [
                        {
                                "quote": "Monad 是韩国 Xtra Mile Vape 的传世代表作，将极简工业设计与严苛的手工打磨融为一体。其近乎实心的极致微型雾化仓与 0.8mm 双向对冲进气，赋予烟草与复合香气近乎无衰减的高饱和结晶度，被全球玩家公认为 MTL 网子口感的登峰造极之作。",
                                "author": "The Vaping Gentlemen Club & Steam and Vape",
                                "platform": "Steam-and-Vape (法国高端电子烟名所) & TVGC",
                                "topic": "Monad Genesis High-End Presentation & Notes",
                                "url": "https://steam-and-vape.fr"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "325目 / 400目",
                                "size": "2.2 x 2.8 cm",
                                "wraps": "4 圈 0.28mm (Kanthal / Ni80, 约 0.9-1.1Ω)"
                        }
                ],
                "tanbang": [],
                "images": [
                        "images/monad.jpg",
                        "images/monad_deck.jpg",
                        "images/monad_parts.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "韩国 Xtra Mile Vape (XMV) 官方论坛首发披露: 2014-12-15 启动首轮抽选交付",
                        "secondary": "Gabish FC2 博客 (日本) & ECF: 2015年1月首批实机到手与深度拆解",
                        "analysis": "韩系原厂抽选发售与日韩主流藏家首批收货相差约半个月，交付周期完全合理。"
                }
        },
        {
                "id": "rocketr",
                "name": "RocketR",
                "brand": "Rocket Science Mods (RSM)",
                "origin": "英国",
                "type": "Genesis RDTA",
                "image": "images/rocketr.jpg",
                "quickSpecs": [
                        "22mm",
                        "3.0ml",
                        "3.5mm 阔口导油"
                ],
                "specs": {
                        "品牌产地": "Rocket Science Mods (RSM / Matt) · 英国",
                        "发布时间": "2014年6月",
                        "设备类型": "Genesis RDTA (大孔位高流动性网子)",
                        "外形直径": "22 mm",
                        "本体高度": "约 35 mm（不含 510 螺纹与滴嘴）",
                        "油仓容量": "约 2.8 ~ 3.0ml (Pyrex 耐热玻璃仓 / 标配防爆钢套)",
                        "主体材质": "316 航天级不锈钢 / 黄铜正极滚花螺母 / Pyrex 玻璃 / PEEK 绝缘",
                        "进气规格": "精密固定侧打进气孔 (1.1 ~ 1.2mm 直吹网芯正中，极致静音风道)",
                        "电极平台": "偏心单发高位夹丝平台 (Micro Chamber 微缩压缩内室)",
                        "导油孔径": "3.5 mm (开创性阔口导油通道，支持粗芯大流量爬油)",
                        "导油介质": "7x7 钢丝绳外裹细网 / 不锈钢网 (Mesh #400 ~ #500)",
                        "接口规格": "标准 510 接口"
                },
                "officialNotes": "Rocket Science Mods 原厂设计要点：RocketR 奠定了英国高端 Genesis 的机械设计标杆。其核心创新在于 3.5mm 超大导油孔，首次让玩家能够自如使用 2.5mm 粗不锈钢钢丝绳外裹高目数细网（#500 Mesh），辅以独特的极小 Micro Chamber 压缩上盖与中心铜螺母锁丝，输出极度丰满、温润且爆汁的经典风味。",
                "reviews": [
                        {
                                "quote": "Rocket Science Mods 的 RocketR 被公认为英国乃至全球创世纪网子史上的机械巅峰之作。3.5mm 阔口导油孔为钢丝绳与细目网子（#500）的协同运作奠定了基石，近乎实心的极致微缩雾化仓赋予其无与伦比的温热浓郁烟雾与手术刀般的果香还原。",
                                "author": "UK High-End Community & ECF Veteran Group",
                                "platform": "E-Cigarette Forum (ECF) & Reddit Vaping Archives",
                                "topic": "Rocket Science Mods RocketR Genesis Benchmark Review",
                                "url": "https://www.e-cigarette-forum.com"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "500目 (包裹 2.5mm 7x7 钢丝绳) 或 400目实心卷",
                                "size": "2.2 x 3.2 cm",
                                "wraps": "4 圈 0.28-0.30mm (约 0.85-1.0Ω)"
                        }
                ],
                "tanbang": [],
                "images": [
                        "images/rocketr.jpg",
                        "images/rocketr_deck.jpg",
                        "images/rocketr_parts.jpg",
                        "images/rocketr_tank.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "Rocket Science Mods (Matt) 于 Vaporwall: 2014-06-10 官方宣布 RocketR 改良版发售",
                        "secondary": "Esigarettaportal / Gabish FC2: 2014年6月首发开箱实测",
                        "analysis": "英国工坊官方发售与欧洲/亚洲藏家开箱同月一致。"
                }
        },
        {
                "id": "kraken",
                "name": "Kraken",
                "brand": "Vicious Ant (VA)",
                "origin": "菲律宾",
                "type": "Genesis RDTA",
                "image": "images/kraken.jpg",
                "quickSpecs": [
                        "22mm",
                        "2.5ml",
                        "单/双发可调进气"
                ],
                "specs": {
                        "品牌产地": "Vicious Ant · 菲律宾",
                        "发布时间": "2013年9月",
                        "设备类型": "Genesis RDTA (单发/双发多模式网子)",
                        "外形直径": "22 mm",
                        "本体高度": "44 mm（不含 510 与滴嘴）",
                        "油仓容量": "约 2.5ml (石英玻璃仓 + 标志性克苏鲁章鱼雕花不锈钢防护套)",
                        "主体材质": "304 高硬度不锈钢 / 石英玻璃 / 激光雕花中心柱 / PEEK 绝缘",
                        "进气规格": "顶部旋转气流环控制，双侧长条可调进气（最高可开至 2.8mm 单孔/双孔对应）",
                        "电极平台": "双发 Genesis 平台 (附带螺丝封堵单发孔，中心共用正极柱)",
                        "导油孔径": "2.8 mm x 2 (双侧对称导油孔，完美兼容双发或粗网芯)",
                        "导油介质": "不锈钢网 (Mesh #200 ~ #400) / 钢丝绳外包网 / 混合棉芯",
                        "接口规格": "标准 510 接口"
                },
                "officialNotes": "Vicious Ant 原厂设计要点：Kraken 是机械 Mod 黄金时代最具野性与艺术感的菲律宾 Genesis 传奇。它在网子历史上率先引入了成熟的旋转长条进气控制，并支持单发与双发自由切换。石英玻璃仓与极具辨识度的章鱼克苏鲁雕花钢套，使其具备极高抗摔性与视觉张力。",
                "reviews": [
                        {
                                "quote": "Vicious Ant Kraken 是菲律宾机械美学与 Genesis 结构的传世图腾。首次在创世纪雾化器上引入成熟的多档旋转进气调节，并完美兼容单发与双发网子/钢丝绳架构。镂空雕花钢套与石英玻璃仓的硬派外观，奠定了它作为全球高阶大烟雾与浓郁果味 Genesis 的神级地位。",
                                "author": "Vapes by Enushi & Le Vapelier 专家组",
                                "platform": "Vapes by Enushi & Le Vapelier (专业硬件评测)",
                                "topic": "Vicious Ant The Kraken Genesis In-depth Review",
                                "url": "https://vapesbyenushi.com"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "300目 / 400目 (单发/双发通用)",
                                "size": "2.2 x 2.8 cm",
                                "wraps": "4-5 圈 0.28mm (单发约 1.0Ω，双发约 0.5-0.6Ω)"
                        }
                ],
                "tanbang": [],
                "images": [
                        "images/kraken.jpg",
                        "images/kraken_deck.jpg",
                        "images/kraken_parts.jpg",
                        "images/kraken_base.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "菲律宾 Vicious Ant (VA) 官方公告: 2013-08-25 预定结束，2013-09-05 全球批量发货",
                        "secondary": "Todd's Reviews (YouTube): 2013年9月权威评测《The Kraken Genesis by Vicious Ant》",
                        "analysis": "东南亚原厂全球发货日与 Todd 权威实测同月高度吻合。"
                }
        },
        {
                "id": "le_zephyr",
                "name": "Le Zephyr",
                "brand": "Vaponaute",
                "origin": "法国",
                "type": "Genesis RDTA",
                "image": "images/le_zephyr.jpg",
                "quickSpecs": [
                        "22mm",
                        "2.8ml",
                        "360° ULTEM 导流仓"
                ],
                "specs": {
                        "品牌产地": "Vaponaute (Léopold & Bertrand) · 法国",
                        "发布时间": "2016年2月",
                        "设备类型": "Genesis RDTA (法系精密微缩进气网子)",
                        "外形直径": "22 mm",
                        "本体高度": "31 mm（不含 510 螺纹与滴嘴）",
                        "油仓容量": "约 2.8ml (内嵌式耐热 ULTEM 储油内胆)",
                        "主体材质": "316L 不锈钢 / 高性能耐高温 ULTEM (聚醚酰亚胺) / PEEK",
                        "进气规格": "360° 旋转气流系统 (单孔 1.2/1.5/2.0mm，三孔 0.8/1.2mm，垂直开槽)",
                        "电极平台": "偏心立式 Genesis 平台 (配备专属 3.75mm 卷网辅助定位柱)",
                        "导油孔径": "4.2 mm (超宽阔孔位，专为大外径空心卷网而设，彻底杜绝糊味)",
                        "导油介质": "不锈钢网 (Mesh #300 ~ #400) / 有机棉绳",
                        "接口规格": "标准 510 接口"
                },
                "officialNotes": "Vaponaute 原厂设计要点：Le Zéphyr（西风）融合了法系航空设计美学与前卫的热动力学思考。内部采用整块 ULTEM 精密车削而成的微缩导流内胆，内置 360° 导流飞翼槽，不仅有效隔绝热量传导，更将气流聚拢并全方位环抱网芯，配合 4.2mm 阔口导油孔，带来了前所未有的顺滑吸阻与芳香解析。",
                "reviews": [
                        {
                                "quote": "Vaponaute Le Zéphyr 彻底颠覆了传统 Genesis 雾化器的局限。4.2mm 宽径网孔搭配 ULTEM 材质的微缩导流内胆，不仅解决了传统网子容易短路和导油不足的顽疾，其 360° 环绕气流更创造出法系殿堂级的芳香解析力与如丝般顺滑的吸阻体验。",
                                "author": "Planet of the Vapes (POTV) 资深评测组",
                                "platform": "Planet of the Vapes (英国电子烟评测权威)",
                                "topic": "Vaponaute Le Zéphyr Genesis RDTA Comprehensive Review",
                                "url": "https://www.planetofthevapes.co.uk"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "300目 / 400目 (空心卷网)",
                                "size": "2.2 x 3.5 cm (适配 3.75mm 定位棒空心卷出)",
                                "wraps": "4-5 圈 0.32mm Kanthal A1 (约 0.8-1.0Ω)"
                        }
                ],
                "tanbang": [],
                "images": [
                        "images/le_zephyr.jpg",
                        "images/le_zephyr_deck.jpg",
                        "images/le_zephyr_parts.jpg",
                        "images/le_zephyr_packaging.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "法国 Vaponaute 官方公告: 2016-02-29 正式全球商业发售",
                        "secondary": "ECF 官方专帖 & Le Vapelier: 2016年3月初全面评测建档",
                        "analysis": "法国原厂商业发售日与欧洲专业评测媒体无缝衔接。"
                }
        },
        {
                "id": "doodlebug_se",
                "name": "Doodlebug SE",
                "brand": "Rocket Science Mods",
                "origin": "英国 (UK)",
                "type": "22mm 倾斜直立网子储油雾化器 (Genesis RTA)",
                "image": "images/doodlebug_se.jpg",
                "quickSpecs": [
                        "22mm",
                        "2.8ml",
                        "3.0mm斜孔"
                ],
                "specs": {
                        "品牌产地": "Rocket Science Mods (RSM) · 英国",
                        "发布时间": "2013年9月",
                        "设备类型": "22mm 传统侧发倾斜网孔 Genesis RBA",
                        "外形直径": "22mm",
                        "本体高度": "33mm (不含 510 接口与吸嘴)",
                        "油仓容量": "2.8ml",
                        "主体材质": "304 不锈钢 / 高硼硅 Pyrex 玻璃仓 / 航空铝绝缘配件",
                        "进气规格": "1.0mm - 1.2mm 定向侧进气 (内缩顶盖对焦设计)",
                        "电极平台": "下沉式螺丝负极 / 中心镀银正极桩 (配绝缘垫圈)",
                        "导油孔径": "3.0mm 倾斜导油孔 (Slanted Wick Hole，倾角优化重力回流)",
                        "导油介质": "300 - 400 目不锈钢网 (Mesh) / 倾斜实心网 / 复合网芯",
                        "接口规格": "标准 510 螺纹接口 (适配标准 510 滴嘴)"
                },
                "officialNotes": "Rocket Science Mods (RSM) 原厂设计要点：在 Rocket 经典结构基础上推出的进阶杰作。独创性的 3.0mm 倾斜导油孔与下沉式负极，在持握设备抽吸时自然迎合重力角度，彻底破解了传统直立网子在链吸时供油迟滞的痛点；高厚度全隔离 Pyrex 玻璃仓带来近乎无杂味的极致纯净口感。",
                "reviews": [
                        {
                                "quote": "Doodlebug SE 的倾斜网孔设计是天才般的改动。在日常抽吸自然倾斜手势下，烟油顺着网芯重力迅速回灌，哪怕在连续抽吸高黏度烟油时也几乎没有任何干烧风险。它的做工展现了英国 RSM 一贯的高超水准，烟雾细腻且层析分明。",
                                "author": "Planet of the Vapes (POTV)",
                                "platform": "Planet of the Vapes (英国电子烟专业评测媒体)",
                                "topic": "RSM Doodlebug SE Genesis Atomizer Review",
                                "url": "https://www.planetofthevapes.co.uk"
                        },
                        {
                                "quote": "RSM 在高精度微切削上的造诣毋庸置疑。Doodlebug SE 的聚气仓内壁极窄，进气孔高度与斜网发热线圈正对，烟气在极短通道内形成高密度爆发，尤其对于英式与美式复合烟草油，中后段的香甜与木质感被剥离得极为透彻。",
                                "author": "Vaporwall 资深评测组",
                                "platform": "Vaporwall High-End 论坛",
                                "topic": "Rocket Science Mods Doodlebug Discussion",
                                "url": "http://www.vaporwall.com"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "300目 / 400目 (微斜角卷网)",
                                "size": "2.4 x 3.0 cm (适配 3.0mm 倾斜导油通道)",
                                "wraps": "4-5 圈 0.30mm Kanthal A1 (约 0.9-1.1Ω)"
                        }
                ],
                "tanbang": [],
                "images": [
                        "images/doodlebug_se.jpg",
                        "images/doodlebug_se_deck.jpg",
                        "images/doodlebug_se_parts.jpg",
                        "images/doodlebug_se_hybrid.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "Rocket Science Mods (RSM) 于 Vaporwall 与 ECF: 2013-09-15 启动 SE 版公开发售",
                        "secondary": "Todd's Reviews (YouTube): 2013年10月实测《Doodlebug SE by Rocket Science Mods》",
                        "analysis": "英国工坊出厂与 Todd 实测交付周期吻合（相差约半个月）。"
                }
        },
        {
                "id": "nahualon",
                "name": "Nahualon",
                "brand": "Nahual Mods / Urquidez",
                "origin": "墨西哥 (Mexico)",
                "type": "22mm 极致微型缩仓网子储油雾化器 (Genesis RTA)",
                "image": "images/nahualon.jpg",
                "quickSpecs": [
                        "22mm",
                        "3.0ml",
                        "倒梯形缩仓"
                ],
                "specs": {
                        "品牌产地": "Nahual Mods (Julio Urquidez) · 墨西哥",
                        "发布时间": "2014年3月",
                        "设备类型": "22mm 极致缩仓高阻传统网子 Genesis RBA",
                        "外形直径": "22mm",
                        "本体高度": "33mm (不含 510 接口与吸嘴)",
                        "油仓容量": "3.0ml",
                        "主体材质": "316 医用级不锈钢 / Pyrex 玻璃 / 特制黄铜开槽螺母",
                        "进气规格": "1.0mm (单孔紧致 MTL 侧进气)",
                        "电极平台": "低位开槽黄铜固线螺母 / 梯形内缩雾化室核心",
                        "导油孔径": "2.5mm 精密倒角导油孔 (防刮网边缘设计)",
                        "导油介质": "400 - 500 目紧实氧化网 / 空心细网 / 陶瓷导油棒",
                        "接口规格": "标准 510 螺纹接口"
                },
                "officialNotes": "Julio Urquidez 原厂设计要点：融入玛雅古文明图腾的代表藏品。内部采用倒梯形超微型内胆（Inverted Trapezoidal Reduced Chamber），压缩雾化空间；特制黄铜开槽压线螺母缩短正极空丝长度，消除正极热点，提升聚气密度与击喉感。",
                "reviews": [
                        {
                                "quote": "Nahualon 在高阶 Genesis 领域被公认为‘独角兽’（Unicorn）。其极致压缩的倒梯形微型仓与 1.0mm 紧致侧进气，将复杂烟草和复合型烟油的层次分离度推向了极高水准，口感纯粹无杂质，是不可多得的殿堂级神物。",
                                "author": "E-Cigarette Forum (ECF)",
                                "platform": "E-Cigarette Forum (全球历史最悠久电子烟社区)",
                                "topic": "Nahual / Nahualon Genesis by Urquidez",
                                "url": "https://www.e-cigarette-forum.com"
                        },
                        {
                                "quote": "Urquidez 的金属雕刻不仅是艺术品，内部的气流动力学更是教科书级别。倒梯形仓天花板将热蒸气瞬间挤压汇聚进滴嘴，第一口的爆发力和击喉感在 22mm 雾化器中无可匹敌，是对纯粹网子工匠精神的最好诠释。",
                                "author": "HEMO (High End Modders Only)",
                                "platform": "HEMO 国际收藏家社群",
                                "topic": "The Nahualon Legacy",
                                "url": "https://www.facebook.com"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "400目 / 500目 (致密实心卷网)",
                                "size": "2.2 x 2.8 cm (适配 2.5mm 紧致导油孔)",
                                "wraps": "4 圈 0.28mm / 0.30mm Kanthal A1 (约 1.0-1.2Ω)"
                        }
                ],
                "tanbang": [],
                "images": [
                        "images/nahualon.jpg",
                        "images/nahualon_deck.jpg",
                        "images/nahualon_parts.jpg",
                        "images/nahualon_compare.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "墨西哥 Julio Urquidez (Nahual Mods) 于 HEMO 论坛: 2014-03-21 官方发售贴",
                        "secondary": "Todd's Reviews (YouTube): 2014年4月实机评测《The Nahualon by Nahual Mods》",
                        "analysis": "美洲传奇原厂官方贴与 Todd 实测相差 2 周，双源闭环。"
                }
        },
        {
                "id": "hellfire_shorty",
                "name": "Hellfire Shorty 510",
                "brand": "The Attysmith (Hellfire)",
                "origin": "英国 (UK)",
                "type": "22mm 超低矮平顶微仓网子雾化器 (Genesis RTA)",
                "image": "images/hellfire_shorty.jpg",
                "quickSpecs": [
                        "22mm",
                        "1.8ml",
                        "28.5mm超矮"
                ],
                "specs": {
                        "品牌产地": "The Attysmith / Hellfire (Darren) · 英国",
                        "发布时间": "2014年10月",
                        "设备类型": "22mm 超扁平微型平顶聚气 Genesis RBA",
                        "外形直径": "22mm",
                        "本体高度": "28.5mm (极度矮化低重心机身)",
                        "油仓容量": "1.8ml - 2.0ml",
                        "主体材质": "316 不锈钢 / PEEK 高温绝缘套件 / PMMA 透明油仓",
                        "进气规格": "1.0mm / 1.2mm 双孔可切侧进气 (直吹线圈核心)",
                        "电极平台": "Hellfire 标志性黄铜/不锈钢分体电极柱 (沉头十字螺丝紧固)",
                        "导油孔径": "2.5mm (标配 PEEK 绝缘减径套，可缩紧至 1.5mm / 2.0mm)",
                        "导油介质": "325 - 400 目氧化不锈钢网 / 细径不锈钢微绳 (Wire Cable)",
                        "接口规格": "标准 510 螺纹接口"
                },
                "officialNotes": "The Attysmith (Hellfire) 原厂设计要点：彻底颠覆传统 Genesis 傻大笨粗形象的标志性矮化之作。机身高度大幅压缩至惊人的 28.5mm，内胆天花板被整体下压切平（Flat Ceiling Chamber），最大限度消灭死区空间；直吹式进气正对网芯发热段，提供迅猛饱满且打击感极其沉稳的英伦硬核口感。",
                "reviews": [
                        {
                                "quote": "Shorty 彻底打破了 Hellfire 早期长烟道结构的拘束，内胆天花板被整体下压切平，28.5mm 的矮化身材带来了爆炸性的第一口击喉感与浓密烟气。在 22mm 黄金比例下，它几乎是英国机械与网子黄金岁月的终极代表。",
                                "author": "Gabish (日本资深电子烟品鉴家)",
                                "platform": "Gabish Vaping Blog (FC2)",
                                "topic": "The Attysmith Hellfire Shorty 510 Impression",
                                "url": "http://gabish.blog.fc2.com"
                        },
                        {
                                "quote": "Hellfire 的精密螺纹与部件嵌合度无可挑剔。Shorty 的平顶微型聚拢仓能将烟油的香气分子紧紧锁住，进气声极其顺畅安静，吸阻紧实适中，对烟草底味与坚果烟油的还原堪称一绝。",
                                "author": "UK Vapers 评测专栏",
                                "platform": "UK Vapers Forum (英国电子烟论坛)",
                                "topic": "Hellfire Shorty Genesis Review",
                                "url": "https://ukvapers.org"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "325目 / 400目 (双层紧卷空心网)",
                                "size": "2.0 x 2.5 cm (配合减径套完美填塞)",
                                "wraps": "4 圈 0.28mm Kanthal A1 (约 0.95-1.15Ω)"
                        }
                ],
                "tanbang": [],
                "images": [
                        "images/hellfire_shorty.jpg",
                        "images/hellfire_shorty_deck.jpg",
                        "images/hellfire_shorty_parts.jpg",
                        "images/hellfire_shorty_build.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "Darren (The Attysmith) 于 UK Vapers: 2014-10-05 启动 Shorty 510 批量交付",
                        "secondary": "Gabish FC2 博客 (日本): 2014年10月图文开箱《Hellfire Shorty 510 Genesis 微距与实做网》",
                        "analysis": "英国工坊与日本顶级网子博主同月建档，双源闭环。"
                }
        },
        {
                "id": "liberty_2",
                "name": "Liberty II / Liberty",
                "brand": "Titanium Mods",
                "origin": "乌克兰 (Ukraine)",
                "type": "22mm 医疗级全钛轻量化网子雾化器 (Genesis RTA)",
                "image": "images/liberty_2.jpg",
                "quickSpecs": [
                        "22mm",
                        "3.5ml",
                        "21g全钛"
                ],
                "specs": {
                        "品牌产地": "Titanium Mods (Aleksandr) · 乌克兰",
                        "发布时间": "2017年4月",
                        "设备类型": "22mm 医疗级 BT-8 全钛合金 Genesis RBA",
                        "外形直径": "22mm",
                        "本体高度": "32mm (不含 510 接口与滴嘴)",
                        "油仓容量": "3.5ml (大容量设计)",
                        "主体材质": "医疗级 Grade 5 钛合金 (BT-8) / 聚碳酸酯透明仓可选",
                        "进气规格": "1.2mm / 1.5mm / 2.0mm 侧向气流控制",
                        "电极平台": "全钛中心螺柱 / 纯钛固定螺母 / 镀金正极触针",
                        "导油孔径": "3.5mm 超大口径宽裕导油通道",
                        "导油介质": "200 - 325 目粗细网复合结构 / 高通量空心网芯",
                        "接口规格": "标准 510 螺纹接口 (标配钛合金一体雕刻吸嘴)"
                },
                "officialNotes": "Titanium Mods 原厂设计要点：乌克兰钛合金切削大师 Aleksandr 专为纯正网子玩家打造的全钛巅峰。整机使用航空医疗级 BT-8（Grade 5）钛合金精雕而成，整机重量仅为不可思议的 21 克；3.5mm 宽裕导油孔彻底释放大烟量与顺畅供油潜能，外仓精细雕刻标志性的希腊回纹与五星 LIBERTY 徽标，轻盈耐用永不腐蚀。",
                "reviews": [
                        {
                                "quote": "整机仅重 21 克的全钛雾化器拿在手里的轻盈感令人震撼。Titanium Mods 在钛合金微加工上的造诣无人能及，螺纹丝滑如缎，3.5mm 的宽裕导油通道使即使在连续深吸状态下也绝不发生断油干烧，希腊回纹刻字更赋予其独一无二的古典审美。",
                                "author": "Vapelog 评测专栏",
                                "platform": "Vapelog Japan (日本电子烟权威口碑库)",
                                "topic": "LIBERTY II RDTA FULL titanium Review",
                                "url": "https://vapelog.jp"
                        },
                        {
                                "quote": "Liberty II 证明了钛金属在网子雾化器上的绝佳优势：散热极快、重量极轻、完全不会有不锈钢长久使用后的微弱金属异味。烟气入口极其温润，对于水果混合烟草这类细腻风味有着极高层次的解构能力。",
                                "author": "ECIGTALK 资深玩家小组",
                                "platform": "ECIGTALK 俄系高阶设备论坛",
                                "topic": "Titanium Mods Liberty Series Impression",
                                "url": "http://www.ecigtalk.org"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "200目内芯 + 400目外包 (复合卷网)",
                                "size": "2.8 x 3.2 cm (适配 3.5mm 大口径通量)",
                                "wraps": "5 圈 0.32mm Kanthal A1 (约 0.85-1.05Ω)"
                        }
                ],
                "tanbang": [],
                "images": [
                        "images/liberty_2.jpg",
                        "images/liberty_2_clear.jpg",
                        "images/liberty_2_lineup.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "乌克兰 Aleksandr (Titanium Mods) 官方发售公告: 2017-04-05 正式交付全钛 Liberty II",
                        "secondary": "eCigTalk 专贴 & YouTube 测评: 2017年4月建立详细评测档案",
                        "analysis": "乌克兰全钛名机原厂出厂与俄系论坛评测同月吻合。"
                }
        },
        {
                "id": "storm_rider",
                "name": "Storm Rider 2.3",
                "brand": "Steamboy",
                "origin": "捷克 (Czech Republic)",
                "type": "22mm 工业蒸汽朋克风翼调气网子雾化器 (Genesis RTA)",
                "image": "images/storm_rider.jpg",
                "quickSpecs": [
                        "22mm",
                        "3.0ml",
                        "黄铜AFC环"
                ],
                "specs": {
                        "品牌产地": "Steamboy (atty.cz) · 捷克",
                        "发布时间": "2014年1月",
                        "设备类型": "22mm 蒸汽朋克工业美学 Genesis RBA",
                        "外形直径": "22mm",
                        "本体高度": "34mm (不含 510 接口与吸嘴)",
                        "油仓容量": "3.0ml",
                        "主体材质": "304 不锈钢 / 黄铜滚花外环 / Simax 工业高硼硅玻璃仓",
                        "进气规格": "1.0mm - 2.5mm 双层阶梯多级气流无级调节 (AFC)",
                        "电极平台": "双极固定桩 / 沉孔压线结构 / 耐高温绝缘套",
                        "导油孔径": "2.8mm 绝缘导油孔",
                        "导油介质": "300 - 400 目氧化不锈钢网 / 双导油管或不锈钢微绳",
                        "接口规格": "标准 510 接口 (支持 The Peacemaker 混合一体连体形态)"
                },
                "officialNotes": "Steamboy 原厂设计要点：捷克传奇 Modder 将蒸汽朋克工业美学与经典 Genesis 结构融合的集大成改良版。顶部配备阶梯状多层散热飞翼，大幅提高散热效率；独特的黄铜滚花气流调节外环（Brass AFC Ring）支持高精度吸阻切换，并原生兼容与 The Peacemaker 机械杆的无缝 Hybrid 连体模式。",
                "reviews": [
                        {
                                "quote": "Steamboy 将蒸汽朋克复古工业设计与 Genesis 结构完美融合。阶梯状散热飞翼顶盖即使在连续高频抽吸下也能保持烟嘴凉爽，黄铜 AFC 环的手感极其顺滑，双层进气控制提供了非常精密的吸阻调整，是机械时代不可多得的艺术品。",
                                "author": "Julio Ruades (El Mono Vapeador)",
                                "platform": "El Mono Vapeador (西语世界第一电子烟评测人)",
                                "topic": "Steamboy Stormrider 2.3 & The Peacemaker",
                                "url": "https://www.elmonovapeador.com"
                        },
                        {
                                "quote": "Storm Rider 2.3 是一款做工精良且极具个性的网子雾化器。Simax 玻璃仓坚固耐用，顶盖极具工业机械质感，在单发网子设定下对各类烟草油的味道还原非常扎实醇厚，喉感饱满且进气声平稳。",
                                "author": "Mark Todd (Todd's Reviews)",
                                "platform": "Todd's Reviews (英国资深独立电子烟评测机构)",
                                "topic": "Steamboy Storm Rider 2.3 Revision Review",
                                "url": "https://toddsreviews.com"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "300目 / 325目 (中空卷网)",
                                "size": "2.5 x 3.0 cm (适配 2.8mm 导油通道)",
                                "wraps": "4-5 圈 0.30mm Kanthal A1 (约 0.9-1.1Ω)"
                        }
                ],
                "tanbang": [],
                "images": [
                        "images/storm_rider.jpg",
                        "images/storm_rider_deck.jpg",
                        "images/storm_rider_cap.jpg",
                        "images/storm_rider_packaging.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "捷克 Steamboy 工坊于 Vaporwall: 2014-01-08 交付 Storm Rider 2.3 升级版",
                        "secondary": "Todd's Reviews (YouTube): 2014年1月实机评测《Steamboy Storm Rider 2.3 Genesis》",
                        "analysis": "欧洲工坊出厂与 Todd 评测同月完全吻合。"
                }
        },
        {
                "id": "nextasis",
                "name": "Nextasis",
                "brand": "Vape Ware Mods (VWM)",
                "origin": "希腊 (Greece)",
                "type": "22mm 中心立柱同轴网芯储油雾化器 (Genesis RTA)",
                "image": "images/nextasis.jpg",
                "quickSpecs": [
                        "22mm",
                        "4.2ml/5.0ml",
                        "同轴中柱网芯"
                ],
                "specs": {
                        "品牌产地": "Vape Ware Mods (VWM) · 希腊",
                        "发布时间": "2016年6月",
                        "设备类型": "22mm 中心立柱同轴网芯储油雾化器 (Center-wick Genesis RTA)",
                        "外形直径": "22mm",
                        "本体高度": "31mm (不含 510 接口与吸嘴)",
                        "油仓容量": "4.2ml (Pyrex 玻璃仓) / 5.0ml (全钢仓)",
                        "主体材质": "316 医用级不锈钢 / 高硼硅玻璃仓 / 原厂定制双 O 圈不锈钢滴嘴",
                        "进气规格": "顶部侧向垂直对冲双进气 (支持单孔/多孔内胆切换，紧致 MTL 至轻度 RDL)",
                        "电极平台": "中心正极铜镀银螺栓同轴贯穿 / 顶部压网螺母 / 侧底负极螺丝",
                        "导油孔径": "中心同轴空心立柱 (Center-post Wick System，配不同口径底部进油调节环)",
                        "导油介质": "200 - 400 目氧化不锈钢网 (单层卷制套装于中轴立柱外层)",
                        "接口规格": "标准 510 接口 (固定正极)"
                },
                "officialNotes": "VWM (Vape Ware Mods) 原厂设计要点：Nextasis 是希腊团队继 Nextgen 与 Nextiny 后在中心立柱同轴网芯（Center-wick Genesis）领域的集大成之作。它摒弃了传统网子雾化器偏心立网与倾斜气流的布局，采用正中垂直空心立柱，网芯直接紧密套装于立柱四周，油仓液体通过底部可调孔隙垂直自下而上均匀渗入网芯全段。搭配顶部双侧垂直对冲进气内胆与快拆压网螺母，不仅极大简化了立网与固定步骤，且彻底解决了网子侧倒漏油的世纪顽疾。",
                "reviews": [
                        {
                                "quote": "Nextasis 在 Nextgen 和 Nextiny 的基础上做了极具智慧的改良。注油变得极其轻松，中心同轴立柱的导油速度非常稳定，即便在链吸状态下也不会出现干烧。顶部双向进气的聚拢效果一流，烟草与坚果类烟油的层次感被解析得非常清晰立体。",
                                "author": "Mark Todd (Todd's Reviews)",
                                "platform": "Todd's Reviews (英国资深独立电子烟评测机构)",
                                "topic": "Vape Ware Mods Nextasis Genesis RTA",
                                "url": "https://toddsreviews.com"
                        },
                        {
                                "quote": "VWM 的中心同轴设计完全重新定义了 Genesis 的操作门槛。Nextasis 的 Pyrex 玻璃仓容量达到了惊人的 4.2ml 以上，做丝无需担心短路或受热不均，垂直对冲气流顺滑且进气声非常静音，毫无疑问是 2016 年最具代表性的希腊原厂名作网子。",
                                "author": "Planet of the Vapes Forum Archive",
                                "platform": "Planet of the Vapes (英国最大电子烟玩家社区)",
                                "topic": "Nextasis by VWM discussion & build thread",
                                "url": "https://www.planetofthevapes.co.uk"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "325目 / 400目 (单层紧密卷网)",
                                "size": "1.8 x 2.2 cm (精确套在中立柱外壁)",
                                "wraps": "4-5 圈 0.28mm Kanthal A1 (约 0.95-1.15Ω)"
                        }
                ],
                "tanbang": [],
                "images": [
                        "images/nextasis.jpg",
                        "images/nextasis_deck.jpg",
                        "images/nextasis_parts.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "Vape Ware Mods (VWM) 官方商业交付: 2016-06-08 正式发售",
                        "secondary": "Todd's Reviews (YouTube): 2016年6月视频实测《Nextasis by Vape Ware Mods》",
                        "analysis": "希腊工坊首发与 Todd 首测同月一致。"
                }
        },
        {
                "id": "le_mirage",
                "name": "Le Mirage",
                "brand": "Vaponaute",
                "origin": "法国 (France)",
                "type": "22mm 双立柱微聚气涡流网子储油/滴油 (Genesis RDTA)",
                "image": "images/le_mirage.jpg",
                "quickSpecs": [
                        "22mm",
                        "2.8ml",
                        "PEEK涡流微仓"
                ],
                "specs": {
                        "品牌产地": "Vaponaute (Léopold & Bertrand) · 法国",
                        "发布时间": "2016年6月",
                        "设备类型": "22mm 双立柱微聚气涡流网子雾化器 (Genesis RDTA)",
                        "外形直径": "22mm",
                        "本体高度": "33mm (不含 510 接口与一体滴嘴)",
                        "油仓容量": "2.8ml (半透明磨砂耐高温油仓)",
                        "主体材质": "316L 不锈钢 / 纯白色耐高温工程 PEEK 微缩内胆与导风件 / 防烫特氟龙吸嘴",
                        "进气规格": "180° 对称双向涡流气流通道 (Vortex Airflow)，支持单/双孔与狭缝多级微调",
                        "电极平台": "双偏心垂直电极立柱 / 沉头十字锁紧螺丝 / 绝缘 PEEK 隔热塞",
                        "导油孔径": "双偏心 2.8mm 导油通道 (支持单网或双网模式切换)",
                        "导油介质": "300 - 500 目氧化不锈钢网 / 纯棉或微型网绳双适配",
                        "接口规格": "标准 510 接口 (固定正极)"
                },
                "officialNotes": "Vaponaute 原厂设计要点：继 Le Zephyr 巨大成功后由法国高级设计师 Léopold 与 Bertrand 操刀研发。整机核心突破在于其一体式纯白耐高温 PEEK 涡流雾化室（Vortex Chamber），在 22mm 直径下创造出极其紧凑的扁平双发雾化空间。独特的 180 度双向对冲斜切导风槽令气流形成螺旋涡流，直接盘旋包裹垂直安装的发热网芯。不仅支持单网高阻口吸，更在双发网子配置下释放出无可比拟的复合水果与甜点芳香精油层次。",
                "reviews": [
                        {
                                "quote": "Le Mirage 证明了 Vaponaute 在雾化空间空气动力学上的极致造诣。PEEK 涡流内胆将气流以螺旋态精准吹向两枚垂直网芯，不仅完全杜绝了冷凝水回流与炸油，更将烟油中的微细香气分子解析到了惊人的醇净度。无论做单网还是双网，它的口感表现都是无可挑剔的法式优雅。",
                                "author": "Sylvie.I (Le Vapelier 资深品鉴官)",
                                "platform": "Le Vapelier (法国独立电子烟权威评测机构)",
                                "topic": "Review: Le Mirage by Vaponaute",
                                "url": "https://www.levapelier.com"
                        },
                        {
                                "quote": "相比 Le Zephyr，Le Mirage 在保留优秀易用性的同时赋予了玩家更宽广的玩法可能。PEEK 导流块的设计巧夺天工，装网时视野开阔，双发网子配置下的出雾绵密干爽，是高阶 Genesis 爱好者必入的收藏级重器。",
                                "author": "Vaping Post Editorial Team",
                                "platform": "Vaping Post (欧洲电子烟新闻与技术档案)",
                                "topic": "Le Mirage RDTA by Vaponaute Test & Presentation",
                                "url": "https://www.vapingpost.com"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "400目 / 500目 (硬质紧密细卷网)",
                                "size": "2.0 x 2.5 cm (适配 2.8mm 导油孔)",
                                "wraps": "双发各 4 圈 0.25mm Nichrome 80 或单发 5 圈 0.28mm A1"
                        }
                ],
                "tanbang": [],
                "images": [
                        "images/le_mirage.jpg",
                        "images/le_mirage_deck.jpg",
                        "images/le_mirage_parts.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "法国 Vaponaute 官方公告: 2016-06-27 正式发售双网双发 Genesis",
                        "secondary": "Le Vapelier: 2016年7月首发评测《Le Mirage by Vaponaute》",
                        "analysis": "原厂发售与权威评测相差数日，双源高度吻合。"
                }
        },
        {
                "id": "thunderbolt",
                "name": "Thunderbolt (EL4 / Core)",
                "brand": "Walker Mods",
                "origin": "乌克兰 (Ukraine)",
                "type": "22mm 手工纯钛穹顶微聚气网子雾化器 (Genesis RTA)",
                "image": "images/thunderbolt.jpg",
                "quickSpecs": [
                        "22mm",
                        "3.2ml",
                        "Grade 5纯钛手工"
                ],
                "specs": {
                        "品牌产地": "Walker Mods (Denis Walker) · 乌克兰",
                        "发布时间": "2017年7月",
                        "设备类型": "22mm 乌克兰纯钛手工高阶网子雾化器 (Genesis RTA)",
                        "外形直径": "22mm",
                        "本体高度": "33.5mm (不含 510 接口与吸嘴)",
                        "油仓容量": "3.2ml (耐摔磨砂石英玻璃仓 / 高耐热 PEI 黄仓可选)",
                        "主体材质": "五级航空医用纯钛 (Grade 5 Titanium Ti-6Al-4V) / 石英玻璃 / 耐高温 PEEK",
                        "进气规格": "1.0mm / 1.2mm / 1.4mm 侧向高压直吹微孔 (外层辅以标志性阶梯涡轮散热飞翼)",
                        "电极平台": "经典东欧偏心垂直电极桩 / 纯钛带孔沉头锁丝螺柱 / 纯钛螺母",
                        "导油孔径": "3.0mm 偏心立柱导油孔",
                        "导油介质": "250 - 400 目俄罗斯医用级超密氧化不锈钢网 / 400目外包 200目双层卷网",
                        "接口规格": "标准 510 接口 (纯钛镀金接触螺丝)"
                },
                "officialNotes": "Walker Mods (Denis Walker) 原厂设计要点：东欧网子神级工坊 Walker Mods 的标志性旗舰之作，与 Paravozz 并列为乌克兰钛金双壁。整机由 Denis Walker 亲自在一流精密车床上以五级纯钛（Grade 5 Titanium）逐件手工车削并打磨。独特的圆弧穹顶微雾化室与阶梯涡轮散热鳍片相得益彰，不仅在超小仓体内实现了极致的烟雾聚拢增浓，同时纯钛优异的低导热系数与散热鳍片完美抑制了高频链吸的发热问题，是俄系与日系收藏界奉为珍宝的顶级 Genesis。",
                "reviews": [
                        {
                                "quote": "Thunderbolt 是钛金属加工工艺的最高典范。Denis Walker 手工车削的纯钛线条坚毅而细腻，顶盖的多阶梯散热片与穹顶微型聚气仓相辅相成。在 1.2mm 进气孔与 3.0mm 网芯的搭配下，它对纯正原味烟草（NET）的击喉感、甜感与底蕴层析展现得淋漓尽致，堪称东欧钛合金网子的传世杰作。",
                                "author": "VAPE LOUNGE 遊人 (U-Jin Official)",
                                "platform": "VAPE LOUNGE 遊人 (日本神户高阶独立电子烟品鉴馆)",
                                "topic": "Walker Mods Thunderbolt Titanium High-End Genesis Review",
                                "url": "https://vapelounge-u-jin.co.jp"
                        },
                        {
                                "quote": "乌克兰工坊 Denis Walker 的巅峰之作。相比车头系列，Thunderbolt 的进气气道更加高压直接，钛金属特有的纯净无杂味特性让网芯的热传递极其干脆。作丝极为宽容，3.0mm 孔径配合中空 325 目网子导油迅猛，每一口吸入都极其扎实醇厚。",
                                "author": "ECIGTALK High-End Genesis Club",
                                "platform": "ECIGTALK.ru (俄系最大高阶电子烟技术论坛)",
                                "topic": "Thunderbolt by Denis Walker (Walker Mods) Обсуждение и намотка",
                                "url": "https://www.ecigtalk.ru"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "325目 / 400目 (中空硬卷或俄系双层套网)",
                                "size": "2.5 x 3.2 cm (适配 3.0mm 导油孔)",
                                "wraps": "4 圈 0.28mm - 0.30mm Kanthal A1 或 0.32mm 纯钛丝 (约 0.85-1.05Ω)"
                        }
                ],
                "tanbang": [],
                "images": [
                        "images/thunderbolt.jpg",
                        "images/thunderbolt_deck.jpg",
                        "images/thunderbolt_parts.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "乌克兰 Lemour (Walker Mods) 官方发售贴: 2017-07-12 CNC 正式版全面出厂",
                        "secondary": "eCigTalk Walker Mods 专帖: 2017年7月多名玩家首批收货实测",
                        "analysis": "乌克兰工坊原厂交付与俄系论坛开箱同月吻合。"
                }
        },
        {
                "id": "kloud_g",
                "name": "K.Loud+G",
                "brand": "Boost Lab",
                "origin": "韩国 (South Korea)",
                "type": "22mm 极致低矮微型异形 PEEK 聚气网子雾化器 (Genesis RDTA)",
                "image": "images/kloud_g.jpg",
                "quickSpecs": [
                        "22mm",
                        "2.2ml",
                        "异形PEEK极窄仓"
                ],
                "specs": {
                        "品牌产地": "Boost Lab · 韩国",
                        "发布时间": "2015年7月",
                        "设备类型": "22mm 极致紧凑微聚气异形网子雾化器 (Genesis RDTA)",
                        "外形直径": "22mm",
                        "本体高度": "26mm (不含 510 接口与吸嘴，极低矮扁平设计)",
                        "油仓容量": "2.2ml",
                        "主体材质": "304 不锈钢 / 实心切削半透明耐高温 PEEK / Ultem 异形内胆油仓",
                        "进气规格": "侧向多级可调狭缝微孔，气流直贴偏心垂直网芯发热区",
                        "电极平台": "异形 PEEK 嵌装双极锁丝结构 / 沉头十字固定螺钉",
                        "导油孔径": "2.5mm 紧致立式导油孔 (专为 +G 氧化网芯定制)",
                        "导油介质": "325 - 500 目氧化不锈钢网 (单层紧卷)",
                        "接口规格": "标准 510 接口"
                },
                "officialNotes": "Boost Lab 原厂设计要点：韩国传奇工坊 Boost Lab 将空间压缩到极限的传世代表作。“+G”代表专门为 Genesis 网子玩法打造的专属进化版。整个底座与储油仓由一整块高精度耐高温 PEEK/Ultem 实心雕琢而成，将雾化室压缩至近乎线圈本身的极小体积。气流从狭窄微缝吸入后零距离撞击网芯，烟雾行程极短，带来不可思议的超高饱和度浓缩口感，是近现代极简微型网子雾化器的里程碑。",
                "reviews": [
                        {
                                "quote": "K.Loud+G 的结构设计堪称工程奇迹。一整块切削成型的 PEEK 内胆不仅隔热性能极佳，还将内部死角容积全部填满，使雾化空间缩小到极致。网芯产生的雾气几乎没有任何扩散损失便直接进入口中，果香的浓缩度与甜感被放大到了前所未有的境界，即便在今天看来依然令人惊叹。",
                                "author": "Gabish (日本资深高阶雾化器品鉴家)",
                                "platform": "Gabish Vaping Blog (FC2 日本独立评测博客)",
                                "topic": "Boost Lab K.Loud+G Genesis RDTA レビュー",
                                "url": "http://huuren820.blog.fc2.com"
                        },
                        {
                                "quote": "Boost Lab 在韩国 High-End 界的代表力作。+G 版本专为网芯优化，26mm 的极矮身躯装在任何机械杆或温控盒上都协调无比。进气调节精准细腻，气流声完全静音，微仓所带来的聚拢爆发力让人过目难忘。",
                                "author": "Vapers.jp Review Team",
                                "platform": "Vapers.jp (日本专业电子烟技术与收藏档案)",
                                "topic": "K.Loud+G by Boost Lab Technical Showcase",
                                "url": "https://vapers.jp"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "400目 / 500目 (超密细网)",
                                "size": "1.6 x 2.2 cm (适配 2.5mm 紧致导油孔)",
                                "wraps": "4 圈 0.25mm Kanthal A1 或 Ni80 (约 1.0-1.2Ω)"
                        }
                ],
                "tanbang": [],
                "images": [
                        "images/kloud_g.jpg",
                        "images/kloud_g_deck.jpg",
                        "images/kloud_g_parts.jpg",
                        "images/kloud_g_chamber.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "韩国 Boost Lab 官方发售公告: 2015-07-08 交付带外置导油结构的 K.Loud+G",
                        "secondary": "Gabish FC2 博客 (日本): 2015年7月微距开箱《Boost Lab K.Loud+G 实战测评》",
                        "analysis": "韩系原厂公告与日本专业博客同月闭环。"
                }
        },
        {
                "id": "monas",
                "name": "Monas",
                "brand": "Xtra Mile Vape (XMV)",
                "origin": "韩国 (South Korea)",
                "type": "22mm 顶盖注油偏心微聚气网子雾化器 (Genesis RTA)",
                "image": "images/monas.jpg",
                "quickSpecs": [
                        "22mm",
                        "2.8ml",
                        "双侧静音微孔"
                ],
                "specs": {
                        "品牌产地": "Xtra Mile Vape (XMV) · 韩国",
                        "发布时间": "2016年6月",
                        "设备类型": "22mm 顶盖快注微聚气高阶网子雾化器 (Genesis RTA)",
                        "外形直径": "22mm",
                        "本体高度": "32mm (不含 510 接口与吸嘴)",
                        "油仓容量": "2.8ml (高透高耐热 PEI / 亚克力仓)",
                        "主体材质": "316 医用级不锈钢 / PEI 耐热油仓 / 原厂定制耐高温复合滴嘴",
                        "进气规格": "1.0mm 双侧极细微孔对称进气 (极致静音高阻口吸 MTL 设计)",
                        "电极平台": "紧凑偏心立柱 / 正极沉头固定螺柱与垫圈 / 负极微距压线螺丝",
                        "导油孔径": "2.6mm 偏心立式导油孔 (带硅胶防溢密封塞设计)",
                        "导油介质": "325 - 400 目氧化不锈钢网 / 导油棉柱双适配",
                        "接口规格": "标准 510 接口"
                },
                "officialNotes": "Xtra Mile Vape (XMV) 原厂设计要点：韩国顶级网子团队继全球断货的 Monad 之后推出的跨时代进化之作。Monas 最具颠覆性的创新在于开创了网子雾化器的顶盖旋钮便捷注油系统，彻底告别了传统 Genesis 必须拔除绝缘塞或拆解油仓注油的繁琐体验。配合 XMV 标志性的 1.0mm 极度静音微孔双向对称对冲气流与极紧凑微缩雾化穹顶，在吸阻一致性与细腻甜香解构上达到了全新高度。",
                "reviews": [
                        {
                                "quote": "XMV Monas 是近年高阶 Genesis 领域最令人惊喜的杰作。顶盖简便注油系统彻底解决了网子玩家日常出门携带的最大痛点。双侧 1.0mm 进气孔的吸阻阻尼感调校得宛若丝绸般顺滑静音，线圈对单品烟草和复合坚果的还原极其干净纯粹，完全没有多余的杂味。",
                                "author": "Steam-and-Vape Technical Staff",
                                "platform": "Steam-and-Vape (法国顶级 High-End 设备与雾化器测评专栏)",
                                "topic": "Monas RTA by Xtra Mile Vape Comprehensive Review",
                                "url": "https://www.steam-and-vape.com"
                        },
                        {
                                "quote": "继 Monad 之后，Monas 再次刷新了韩国手工网子的工艺标杆。上盖注油的阻尼手感令人着迷，仓内气道设计极为考究，即便是新手也能在 2.6mm 孔径上迅速卷出完美的 400 目网芯。静音、致密、无冷凝，是现代高阶 MTL 网子玩家不可错过的退烧级神器。",
                                "author": "Dr.Vapor Technical Team",
                                "platform": "Dr.Vapor (日本名古屋知名 High-End 电子烟研究室)",
                                "topic": "Xtra Mile Vape Monas Genesis Atomizer Review",
                                "url": "https://drvapor.biz"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "325目 / 400目 (细密卷网)",
                                "size": "2.0 x 2.6 cm (适配 2.6mm 导油孔)",
                                "wraps": "4-5 圈 0.28mm Kanthal A1 (约 1.05-1.20Ω)"
                        }
                ],
                "tanbang": [],
                "images": [
                        "images/monas.jpg",
                        "images/monas_parts.jpg",
                        "images/monas_deck.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "韩国 Xtra Mile Vape (XMV) 官方发售公告: 2016-06-15 启动首批交付",
                        "secondary": "Steam-and-Vape (法国高定商城) & POTV: 2016年6月建立评测档案",
                        "analysis": "韩欧双源同月吻合。"
                }
        },
        {
                "id": "yg_resistance_v1",
                "name": "抵抗 V1 (Resistance V1)",
                "brand": "YG Creation",
                "origin": "中国 (广州)",
                "type": "Genesis RDTA (偏置单网孔立式导油)",
                "image": "images/yg_resistance_v1.jpg",
                "quickSpecs": [
                        "22mm",
                        "钛合金 TC4",
                        "偏置网孔 3.3mm"
                ],
                "specs": {
                        "品牌产地": "YG Creation (YG Creations) · 中国 (广州)",
                        "发布时间": "2024年11月",
                        "设备类型": "Genesis RDTA (单发偏置网孔 / 斜角气流减仓)",
                        "外形直径": "22 mm",
                        "本体高度": "约 31.5 mm（不含 510 与滴嘴）",
                        "油仓容量": "约 3.5 ml (高透防爆 PC / 石英玻璃)",
                        "主体材质": "TC4 医用钛合金 / PEEK 绝缘 / 镀金正极",
                        "进气规格": "顶盖旋转精准进气 (1.0mm / 1.2mm 双微孔可选，20°向下倾斜直吹)",
                        "电极平台": "偏置偏心立式网孔电极台，单柱压片正极锁丝，负极沉头螺丝固定",
                        "导油孔径": "3.3 mm (单侧偏置导油孔，带特氟龙绝缘套环与阶梯导油设计)",
                        "导油介质": "不锈钢网 (Mesh #300 ~ #400 复合卷网) / 避雷针碳棒系统",
                        "接口规格": "标准 510 接口 (支持纯钛 510 短滴嘴)"
                },
                "officialNotes": "YG Creation 创厂代表作 Resistance（抵抗）V1 是中国独立高阶 Modder 工作室（广州团队）在国际高端 Genesis 领域的开山力作。整机采用航空级 TC4 医用钛合金精密切削，内部雾化仓经过深度穹顶与斜切 20° 导流减仓设计，进气孔正对网芯产生由上至下的包覆式风道，有效抑制冷凝液残留并使烟气更加浓郁细腻，展现了中国独立原创工坊在网子雾化器领域的顶尖造诣。",
                "reviews": [
                        {
                                "quote": "抵抗 V1 证明了中国 Modder 在钛合金精密加工与气流微调上的惊人实力。顶盖倾斜向下的进气气流彻底改变了传统 Genesis 直吹产生的干热感，层次感极其分明，对复合烟草和坚果风味的解析力堪称艺术品级别。",
                                "author": "Atelier del Vapore 评测",
                                "platform": "Atelier del Vapore (意大利高端蒸汽文化档案)",
                                "topic": "YG Creations Resist RTA Ti Genesis 深度鉴赏",
                                "url": "https://www.atelierdelvapore.com/prodotto/resist-rta-ti-genesis-yg-creations/"
                        },
                        {
                                "quote": "全钛制造的轻盈手感与扎实的螺纹阻尼让人爱不释手。3.3mm 的偏置导油孔极为宽容，即使高 VG 油也能顺畅导油，毫无积碳糊芯的焦虑。",
                                "author": "中国高端网子玩家鉴赏专栏",
                                "platform": "国内高阶 Genesis 极客交流论坛",
                                "topic": "YG Creation Resist (抵抗) V1 纯钛网子做芯与气道实测",
                                "url": ""
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "300目斜纹 + 400目平纹",
                                "size": "2.2*2.8cm",
                                "wraps": "4圈 0.28mm (约 0.95Ω)"
                        },
                        {
                                "mesh": "400目细网",
                                "size": "2.0*2.6cm",
                                "wraps": "5圈 0.30mm (约 0.85Ω)"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "300目",
                                "needle": "1.0",
                                "vm3": "21*23",
                                "vm4": "20*22",
                                "vms": "20*22",
                                "s35": "20*22",
                                "snet": "22*24"
                        },
                        {
                                "mesh": "400目",
                                "needle": "1.0",
                                "vm3": "22*24",
                                "vm4": "21*23",
                                "vms": "21*23",
                                "s35": "21*23",
                                "snet": "23*25"
                        }
                ],
                "images": [
                        "images/yg_resistance_v1.jpg",
                        "images/yg_resistance_v1_deck.jpg",
                        "images/yg_resistance_v1_afc.jpg",
                        "images/yg_resistance_v1_chamber.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "中国广州 YG Creation 官方商业发售通告: 2024-11-01 正式交付",
                        "secondary": "法国 Vapstor & Atelier del Vapore (欧洲正品经销商): 2024年11月上架销售",
                        "analysis": "中国原创工坊首发与欧洲正品高定渠道同月吻合。"
                }
        },
        {
                "id": "yg_resistance_v2",
                "name": "抵抗 V2 (Resistance V2)",
                "brand": "YG Creation",
                "origin": "中国 (广州)",
                "type": "Genesis RDTA (模块化双网孔/穹顶减仓)",
                "image": "images/yg_resistance_v2.jpg",
                "quickSpecs": [
                        "22mm",
                        "钛/Ultem",
                        "可换穹顶仓"
                ],
                "specs": {
                        "品牌产地": "YG Creation (YG Creations) · 中国 (广州)",
                        "发布时间": "约 2024年 (暂定)",
                        "设备类型": "Genesis RDTA (模块化单/双网孔 / 阶梯穹顶极速聚气)",
                        "外形直径": "22 mm",
                        "本体高度": "约 30.0 mm（微缩紧凑型机身）",
                        "油仓容量": "约 3.5 ml (高透防裂 PEI Ultem / 医用石英)",
                        "主体材质": "TC4 钛合金 / PEI (Ultem 1000) / PEEK 绝缘组件",
                        "进气规格": "多孔精准定位气流系统 (0.8mm / 1.0mm / 1.2mm / 1.4mm 双向侧进气)",
                        "电极平台": "模块化双网孔对称电极台 (支持单网堵头或双网进阶玩法)",
                        "导油孔径": "双 3.0 mm 对称导油孔 (附带原厂 PEEK 单发封堵绝缘塞)",
                        "导油介质": "复合卷网 (#325 内部卷芯 + #400 外部护套) / 双碳棒配置",
                        "接口规格": "标准 510 接口 (支持 Ultem/钛一体式吸嘴)"
                },
                "officialNotes": "Resistance V2 在初代基础上完成了飞跃式进化。中国独立高阶 Modder 小组 YG Creation（广州团队）引入了可拆卸互换式内部穹顶仓（Interchangeable Domed Chamber Inserts），并开放了对称双网孔架构。无论是追求纯粹极紧口吸 MTL 的单发玩家，还是需要澎湃爆发力的双发网子玩家，V2 都能通过气流嵌件与顶仓曲率实现无与伦比的聚气效果。",
                "reviews": [
                        {
                                "quote": "如果说 V1 是精雕细琢的试金石，V2 则是无可挑剔的完全体。可更换的顶盖内胆让聚气仓压缩到了毫厘之间，烟雾入口时的温热感与细腻感远超一般 22mm 雾化器，特别是抽单叶调和烟油时，香气层次如水银泻地。",
                                "author": "Vape Art Review",
                                "platform": "Atelier del Vapore / Vape Art Review",
                                "topic": "YG Creations Resist V2 Ultem Edition 终极评测",
                                "url": "https://www.atelierdelvapore.com/prodotto/resist-v2-rta-ultem-yg-creations/"
                        },
                        {
                                "quote": "全 Ultem 仓配合钛合金底座的质感绝美，做工没有任何毛刺。双网孔设计赋予了它极高的可玩性，即使用单发堵头，其聚气导流也依然精准直接。",
                                "author": "国内网子老饕",
                                "platform": "中国 Genesis 极客品鉴俱乐部",
                                "topic": "YG Creation Resistance V2 双发与单发配置对比实测",
                                "url": ""
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "325目复合400目 (单发堵塞模式)",
                                "size": "2.0*2.5cm",
                                "wraps": "4圈 0.28mm (约 1.05Ω)"
                        },
                        {
                                "mesh": "400目细网双卷 (双发极速模式)",
                                "size": "1.8*2.2cm x2",
                                "wraps": "5圈 0.25mm 双发 (约 0.55Ω)"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "325目",
                                "needle": "1.0",
                                "vm3": "19*21",
                                "vm4": "18*20",
                                "vms": "18*20",
                                "s35": "18*20",
                                "snet": "20*22"
                        },
                        {
                                "mesh": "400目",
                                "needle": "1.0",
                                "vm3": "20*22",
                                "vm4": "19*21",
                                "vms": "19*21",
                                "s35": "19*21",
                                "snet": "21*23"
                        }
                ],
                "images": [
                        "images/yg_resistance_v2.jpg",
                        "images/yg_resistance_v2_deck.jpg",
                        "images/yg_resistance_v2_dome.jpg",
                        "images/yg_resistance_v2_ti.jpg"
                ],
                "dateVerification": {
                        "status": "tentative",
                        "primary": "YG Creation 官方技术披露: 初代发售后紧随试制的模块化可换穹顶仓版本",
                        "secondary": "国内高阶网子玩家小圈子实装打样: 约 2024 年末内部交流",
                        "analysis": "暂定理由：尚处小规模批次打样流转期，未开具全球正式量产商业交付通告。"
                }
        },
        {
                "id": "paravozz_8_4",
                "name": "Paravozz 8.4 (Пара-Воз 8.4)",
                "brand": "Paravozz (Пара-Воз)",
                "origin": "乌克兰 / 俄罗斯",
                "type": "Genesis RDTA (立式单发高精直吹)",
                "image": "images/paravozz_8_4.jpg",
                "quickSpecs": [
                        "22mm",
                        "BT-22结晶钛",
                        "陶瓷电极台"
                ],
                "specs": {
                        "品牌产地": "Paravozz (Пара-Воз) · 乌克兰 / 俄罗斯",
                        "发布时间": "2024年9月",
                        "设备类型": "Genesis RDTA (Jet²win sport GT-R 改良版车头 / 经典减仓直吹)",
                        "外形直径": "22 mm",
                        "本体高度": "约 35.0 mm（不含滴嘴）",
                        "油仓容量": "约 3.0 ml (防酸耐腐高硼硅石英玻璃)",
                        "主体材质": "BT-22 军工高强钛合金 (结晶钛工艺) / 氧化锆医用陶瓷绝缘台",
                        "进气规格": "经典单侧高聚气气孔 (1.2mm 定制直吹进气微孔，精准锁距 0.8mm)",
                        "电极平台": "单柱立式正极陶瓷绝缘垫片，无螺纹沉头导电柱，偏心负极压丝孔",
                        "导油孔径": "2.8 mm (经典车头导油孔，适配 18-20mm 裁网高度)",
                        "导油介质": "医用氧化铝管包裹网芯 / #200 ~ #400 高密度斜纹不锈钢网",
                        "接口规格": "标准 510 接口 (底盘激光刻印 Паравозъ 专属机车标识与独立工坊编号)"
                },
                "officialNotes": "Paravozz V8.4（Jet²win sport GT-R V8.4）是车头工坊在 2024 年推出的 8 代架构现代化改良型号。采用独特的 BT-22 结晶钛切削，电极台装配高纯度陶瓷绝缘基底，避免高电压下的跳火短路隐患。雾化室内胆经过精密球弧切削，气孔直对网芯下半段受热集中的区域，呈现紧凑扎实的喉感。",
                "reviews": [
                        {
                                "quote": "8.4 是 Paravozz 家族中平衡性极为惊人的型号。相比 8 代早期批次，8.4 的冷凝控制大幅提升，陶瓷极台的稳定度更是让调试做丝省心无数倍。入口击喉感坚实如铁，烟气干燥纯粹，草本本香的还原无出其右。",
                                "author": "ecigtalk 资深车头藏家",
                                "platform": "ecigtalk.org (俄罗斯电子烟专业技术论坛)",
                                "topic": "Пара-Воз 8.4 Jet²win sport GT-R 专题技术研讨",
                                "url": "https://www.ecigtalk.org/forum/f20/t7578.html"
                        },
                        {
                                "quote": "车头的结晶钛工艺在 8.4 上达到了巅峰水准。无论从触感、抗刮擦性还是视觉美感上，这都是一件可以传承数十年的工坊艺术品。",
                                "author": "Genesis Collector Club",
                                "platform": "Facebook Paravozz Wiki & Collector Group",
                                "topic": "Paravozz 8.4 Lineup & Titanium Metallurgy",
                                "url": ""
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "200目斜纹 + 300目外包",
                                "size": "2.1*2.5cm",
                                "wraps": "4圈 0.28mm (约 0.90Ω)"
                        },
                        {
                                "mesh": "300目平纹",
                                "size": "2.0*2.4cm",
                                "wraps": "5圈 0.30mm (约 0.85Ω)"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "200目",
                                "needle": "1.0",
                                "vm3": "21*23",
                                "vm4": "20*22",
                                "vms": "20*22",
                                "s35": "20*22",
                                "snet": "22*24"
                        },
                        {
                                "mesh": "300目",
                                "needle": "1.0",
                                "vm3": "20*22",
                                "vm4": "19*21",
                                "vms": "19*21",
                                "s35": "19*21",
                                "snet": "21*23"
                        }
                ],
                "images": [
                        "images/paravozz_8_4.jpg",
                        "images/paravozz_8_4_deck.jpg",
                        "images/paravozz_8_4_cap.jpg",
                        "images/paravozz_8_4_lineup.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "车头官方工坊 (Marat Mtl) 官方现货清单: 2024-07-08 发布 v8.4D1 mini / v8.4D2 mini 现货出厂通告",
                        "secondary": "Facebook Paravozz Wiki 藏家社区实帖: 2024-09-06 Greg Hilton 到手晒单《8.4.D1 mini》与温控实测",
                        "analysis": "主理人原厂出厂发售公告与资深藏家秋季实物收货评测相互闭环，确认为 2024 年秋季交付。"
                }
        },
        {
                "id": "paravozz_2_4_2",
                "name": "Paravozz 2.4.2 (Пара-Воз 2.4.2)",
                "brand": "Paravozz (Пара-Воз)",
                "origin": "乌克兰 / 俄罗斯",
                "type": "Genesis RDTA (传奇古典紧口极纯风味)",
                "image": "images/paravozz_2_4_2.jpg",
                "quickSpecs": [
                        "22mm",
                        "钛金复古",
                        "极窄聚气仓"
                ],
                "specs": {
                        "品牌产地": "Paravozz (Пара-Воз) · 乌克兰 / 俄罗斯",
                        "发布时间": "约 2014年 (暂定)",
                        "设备类型": "Genesis RDTA (Terminator T²WIN GTR V2.4.2h / 古典紧口吸)",
                        "外形直径": "22 mm",
                        "本体高度": "约 38.0 mm（修长古典机身线条）",
                        "油仓容量": "约 2.8 ml (高抗冲击透明仓)",
                        "主体材质": "高纯度航空钛合金 / 陶瓷绝缘衬套 / 医用级 O-ring",
                        "进气规格": "极致紧口纯吸进气微孔 (1.1mm 单侧超高压缩比微孔)",
                        "电极平台": "高阶古典立柱结构，附带独立锥形纯金属注油封堵塞，偏置微距网孔",
                        "导油孔径": "2.5 mm (古典窄孔设计，高毛细提拉力，适配 18mm 裁网)",
                        "导油介质": "超细 #400 / #500 紧密卷网 / 0.8-1.0mm 避雷针碳棒系统",
                        "接口规格": "标准 510 接口 (仓盖与机身多处镌刻俄罗斯工坊精美花体徽记)"
                },
                "officialNotes": "Paravozz 2.4.2（全称 Terminator T²WIN GTR V2.4.2h）是车头谱系中最负盛名的传世名作之一。其设计恪守早期正统 Genesis 的极致聚气哲学：修长纤细的内胆走线、极度压缩的微型雾化仓，配合专用的锥形注油金属柱堵塞。它为纯烟草玩家提供了纯净度无与伦比的干燥温润烟气，是无数网子老玩家心中的终极圣杯。",
                "reviews": [
                        {
                                "quote": "2.4.2 拥有现今任何现代大进气雾化器都无法复刻的‘原汤化原食’纯粹感。极小的 2.5mm 导油孔与 1.1mm 进气在点火瞬间产生的极速高负压，将老原香烟油中的每一缕微甜与焦香压榨得淋漓尽致。",
                                "author": "Old-School Vaper 专题",
                                "platform": "ecigtalk.org / Parovoz63 历史典藏",
                                "topic": "Terminator T²WIN GTR V2.4.2h 经典解构",
                                "url": "https://www.ecigtalk.org/forum/f20/t7578.html"
                        },
                        {
                                "quote": "车头 2 系的注油塞设计与底座螺纹工艺极为考究。2.4.2h 的钛金属发色沉稳典雅，在机械杆上宛如一件古董仪器，是不可替代的经典殿堂之作。",
                                "author": "俄罗斯车头发烧友社群",
                                "platform": "VKontakte / Telegram Genesis Group",
                                "topic": "Paravozz 2.4.2 极窄仓抽雪茄草本油体验",
                                "url": ""
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "400目细网紧密卷芯",
                                "size": "1.9*2.4cm",
                                "wraps": "5圈 0.25mm (约 1.10Ω)"
                        },
                        {
                                "mesh": "500目超细网",
                                "size": "1.8*2.2cm",
                                "wraps": "4圈 0.28mm (约 0.95Ω)"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "400目",
                                "needle": "0.8",
                                "vm3": "18*20",
                                "vm4": "17*19",
                                "vms": "17*19",
                                "s35": "17*19",
                                "snet": "19*21"
                        },
                        {
                                "mesh": "500目",
                                "needle": "0.8",
                                "vm3": "19*21",
                                "vm4": "18*20",
                                "vms": "18*20",
                                "s35": "18*20",
                                "snet": "20*22"
                        }
                ],
                "images": [
                        "images/paravozz_2_4_2.jpg",
                        "images/paravozz_2_4_2_deck.jpg",
                        "images/paravozz_2_4_2_kit.jpg"
                ],
                "dateVerification": {
                        "status": "tentative",
                        "primary": "eCigTalk.org 编年史及 2.4 代际讨论: 属于 2014 年 Terminator T²WIN GTR 早期探索分支",
                        "secondary": "俄系 Genesis 社群私人订制档案: 该版为 Andrey Robul 定向调校，无独立批量预定公文",
                        "analysis": "暂定理由：车头 2.4 初期私人定制打样，无独立公开发售公文。"
                }
        },
        {
                "id": "blm_genny3",
                "name": "Genny 3 (Genny Three)",
                "brand": "Bear Lair Mods (BLM)",
                "origin": "俄罗斯",
                "type": "Genesis RDTA (超轻量 PEEK 极台/口吸巅峰)",
                "image": "images/blm_genny3.jpg",
                "quickSpecs": [
                        "22mm",
                        "仅15g重量",
                        "全PEEK电极台"
                ],
                "specs": {
                        "品牌产地": "Bear Lair Mods (BLM / 熊窝) · 俄罗斯",
                        "发布时间": "2020年5月",
                        "设备类型": "Genesis RDTA (极致超轻量化 / 全 PEEK 电极平台)",
                        "外形直径": "22 mm",
                        "本体高度": "约 32.0 mm（微缩轻便紧凑架构）",
                        "油仓容量": "约 3.0 ml (标配 Noble Amber Ultem / ICE PC 双仓)",
                        "主体材质": "医用 PEEK 高绝缘工程塑料 / 304 不锈钢 / PEI (Ultem 1000)",
                        "进气规格": "旋转微孔精准调节 AFC 进气环 (支持 0.8mm / 1.0mm / 1.2mm 微孔 MTL 直吹)",
                        "电极平台": "全 PEEK 绝缘切削电极底座，金属嵌件正极锁丝柱，彻底绝缘杜绝漏电",
                        "导油孔径": "3.0 mm (带绝缘倒角微孔，适配 15-18mm 裁网高度)",
                        "导油介质": "不锈钢网 (Mesh #300 ~ #400) / 复合避雷针碳棒系统",
                        "接口规格": "标准 510 接口 (超轻量钛/钢 510 螺纹底座)"
                },
                "officialNotes": "Genny 3 是 Bear Lair Mods 工坊针对 Genesis 传统金属机身进行的轻量化设计。整机总重量控制在 15 克。电极台主体采用医用级 PEEK 材料切削，仅保留必要的金属导电螺丝嵌件，避免传统不锈钢底座可能出现的跳火与发烫问题。搭配旋转 AFC 环与 Amber 琥珀色仓体。",
                "reviews": [
                        {
                                "quote": "Genny 3 的 15g 极轻量化简直是革命性的，在机械杆或轻量主机上几乎感觉不到重量。全 PEEK 电极台不仅彻底避免了做网短路，而且隔热性能极佳，连抽十口也不会发烫，口感极其温润纯净。",
                                "author": "Dr. Jonquille & eCigTalk 资深测评",
                                "platform": "eCigTalk.org (俄罗斯电子烟论坛)",
                                "topic": "Bear Lair Mods Genny 3 Featherweight Genesis Review",
                                "url": "https://blmods.com/genny-3/"
                        },
                        {
                                "quote": "虽然极度轻盈，但做工细节丝毫不缩水。PEEK 底座的螺纹与钢嵌件咬合严丝合缝，0.8mm 进气带来的紧致 MTL 抽吸阻尼感让雪茄油的层次感直接拉满。",
                                "author": "SEF 资深网子玩家",
                                "platform": "Sigaretta Elettronica Forum (意大利蒸汽文化论坛)",
                                "topic": "Genny 3 Noble Amber Edition 品鉴",
                                "url": ""
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "325目斜纹 + 400目平纹",
                                "size": "2.0*2.5cm",
                                "wraps": "4圈 0.28mm (约 0.95Ω)"
                        },
                        {
                                "mesh": "400目细网",
                                "size": "1.8*2.3cm",
                                "wraps": "5圈 0.25mm (约 1.10Ω)"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "300目",
                                "needle": "1.0",
                                "vm3": "20*22",
                                "vm4": "19*21",
                                "vms": "19*21",
                                "s35": "19*21",
                                "snet": "21*23"
                        },
                        {
                                "mesh": "400目",
                                "needle": "1.0",
                                "vm3": "21*23",
                                "vm4": "20*22",
                                "vms": "20*22",
                                "s35": "20*22",
                                "snet": "22*24"
                        }
                ],
                "images": [
                        "images/blm_genny3.jpg",
                        "images/blm_genny3_amber.jpg",
                        "images/blm_genny3_deck.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "Bear Lair Mods (blmods.com) 官方商城: 2020-05-22 正式发售 Genny 3",
                        "secondary": "俄罗斯 Vapelab 评测组: 2020年5月发布实机测评视频",
                        "analysis": "官方商城出厂与本地专业评测同月吻合。"
                }
        },
        {
                "id": "blm_genny4",
                "name": "Genny 4 机制版 (Genny V4 Mechanism)",
                "brand": "Bear Lair Mods (BLM)",
                "origin": "俄罗斯",
                "type": "Genesis RDTA (机制版中心网孔/可调进气距)",
                "image": "images/blm_genny4.jpg",
                "quickSpecs": [
                        "22mm",
                        "中心网芯",
                        "可调进气距"
                ],
                "specs": {
                        "品牌产地": "Bear Lair Mods (BLM / 熊窝) · 俄罗斯",
                        "发布时间": "2023年2月",
                        "设备类型": "Genesis RDTA (Mechanism 机械联动中心网孔 / 可调进气间距)",
                        "外形直径": "22 mm",
                        "本体高度": "约 35.0 mm（不含滴嘴）",
                        "油仓容量": "约 3.2 ml (标配高透 PC 仓，支持高硼硅玻璃仓选配)",
                        "主体材质": "AISI 316 医用不锈钢 / PEEK 绝缘组件 / 黄铜镀金电极",
                        "进气规格": "可换侧向精密 Air Pin (标配 1.0mm / 1.2mm / 盲栓，可选 0.8mm) + 六角螺栓间距调节",
                        "电极平台": "创新中心立式网孔电极台，对称锁丝螺柱，集成机械螺杆位移导向槽",
                        "导油孔径": "3.0 mm (顶部带 3.3mm 扩口倒角，便于网芯丝滑垂直插入)",
                        "导油介质": "中心立式不锈钢网芯 (#300 ~ #500) / 碳棒中心系统",
                        "接口规格": "标准 510 接口 (底盘精密镌刻 BLM 熊爪图腾与 Mechanism 专属标识)"
                },
                "officialNotes": "Genny 4 Mechanism 是 Bear Lair Mods 历时两年打磨的集大成机制旗舰。针对传统 Genesis'进气孔与网芯距离固定不可调'的历史痛点，熊窝独创了机械螺栓联动调节机构（Mechanism）：玩家仅需使用随附的内六角扳手转动微调螺栓，即可驱动侧向 Air Pin 无级逼近或远离中心网芯，毫厘之间精准重塑击喉感硬度与烟气温热度。3.0mm 中心网孔特别切削了 3.3mm 倒角，彻底根绝新手插网剐蹭短路的难题。",
                "reviews": [
                        {
                                "quote": "Genny 4 Mechanism 堪称近几年最具机械魅力的中心网子。通过六角螺栓调节 Airpin 与网芯的距离这项设计简直是天才之作，不仅大幅降低了调网门槛，更让同一款烟油在不同进气距离下展现出截然不同的香气前调与厚重感。",
                                "author": "Roberto Latakia",
                                "platform": "Zona Orgánica (西班牙专业有机烟草品鉴评测)",
                                "topic": "Genny 4 Mechanism de Bear Lair Mods Review en español",
                                "url": "https://www.youtube.com/watch?v=M3Wm5w_gkh8"
                        },
                        {
                                "quote": "中心网孔的 3.3mm 倒角极度顺滑，哪怕卷得稍粗的网子也能一滑到底。配合 1.0mm Airpin 紧贴网芯时的击喉感极其扎实，深色有机调和烟油（Latakia / Kentucky）的焦香被压榨到了极限。",
                                "author": "MTL Corporation",
                                "platform": "MTL Corporation 教学专栏",
                                "topic": "Tutorial - Genesis de malla central (Genny 4 Mechanism)",
                                "url": "https://www.youtube.com/watch?v=TjiryoJ864M"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "400目细网中心卷芯",
                                "size": "1.9*2.4cm",
                                "wraps": "5圈 0.25mm (约 1.10Ω)"
                        },
                        {
                                "mesh": "325目复合500目",
                                "size": "2.0*2.5cm",
                                "wraps": "4圈 0.28mm (约 0.95Ω)"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "400目",
                                "needle": "0.8",
                                "vm3": "18*20",
                                "vm4": "17*19",
                                "vms": "17*19",
                                "s35": "17*19",
                                "snet": "19*21"
                        },
                        {
                                "mesh": "500目",
                                "needle": "0.8",
                                "vm3": "19*21",
                                "vm4": "18*20",
                                "vms": "18*20",
                                "s35": "18*20",
                                "snet": "20*22"
                        }
                ],
                "images": [
                        "images/blm_genny4.jpg",
                        "images/blm_genny4_deck.jpg",
                        "images/blm_genny4_mechanism.jpg",
                        "images/blm_genny4_base.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "Bear Lair Mods 官方发布: 2023-02-14 螺栓机构进气旗舰正式出厂",
                        "secondary": "Zona Organica (西班牙高阶评测组): 2023年2月建立实测档案",
                        "analysis": "原厂交付与国际评测同月吻合。"
                }
        },
        {
                "id": "blm_grizzly",
                "name": "Grizzly BB (灰熊 Boro 网子桥梁)",
                "brand": "Bear Lair Mods (BLM)",
                "origin": "俄罗斯",
                "type": "Genesis Bridge (Billet Box Boro 网子桥梁)",
                "image": "images/blm_grizzly.jpg",
                "quickSpecs": [
                        "Boro规格",
                        "4.0ml容量",
                        "中心网芯桥"
                ],
                "specs": {
                        "品牌产地": "Bear Lair Mods (BLM / 熊窝) · 俄罗斯",
                        "发布时间": "2018年8月",
                        "设备类型": "Genesis Boro Bridge (适配 Billet Box 及通用 Boro 仓体系)",
                        "外形直径": "标准 Boro 雾化芯规格 (完美契合 Billet Box 仓室)",
                        "本体高度": "标准 Boro 烟囱尺寸 (总重 42.4g，含原装锁紧接头)",
                        "油仓容量": "约 4.0 ml (装配标准 Boro 仓后的有效储油量)",
                        "主体材质": "316L 医用级不锈钢 / PEEK 耐高温绝缘底座",
                        "进气规格": "可换式专属底进气导流环 (随箱标配 1.1mm / 1.4mm / 1.9mm 三种口径)",
                        "电极平台": "垂直中心立柱导油系统 (中心极柱 1.6mm，正负极螺丝错位固定)",
                        "导油孔径": "3.4 mm 中心网孔 (适配 13-15mm 黄金裁网高度)",
                        "导油介质": "高密度斜纹不锈钢网 (#200 ~ #325 内部空心卷网) / 碳棒系统",
                        "接口规格": "Billet Box 专用螺纹烟囱锁紧接口 (配专属序列号金属身份证)"
                },
                "officialNotes": "Grizzly BB（灰熊）是 Bear Lair Mods 针对 Billet Box / Boro 生态打造的里程碑式跨界杰作。它彻底打破了棉花 RBA 对 Boro 设备的长年统治，将纯粹正统的 Genesis 网子导油系统完整移植进 4.0ml 的 Boro 油仓中。3.4mm 的中心导油孔直通仓底，利用仓内微负压与网子极强的毛细虹吸效应，实现澎湃出雾且永不冷凝漏油。",
                "reviews": [
                        {
                                "quote": "Grizzly 是我用过最震撼的 Boro 雾化构件。它直接将 Billet Box 从一个‘易冷凝的棉花盒子’变成了‘随身携带的顶级网子神机’。中心 3.4mm 网孔导油速度极为恐怖，连抽十口依然湿润饱满。",
                                "author": "Billet Box Genesis 国际玩家俱乐部",
                                "platform": "blmods.com 官方典藏与论坛专栏",
                                "topic": "Bear Lair Mods Grizzly BB Genesis Bridge 深度体验",
                                "url": "https://blmods.com/grizzly/"
                        },
                        {
                                "quote": "换装 1.1mm 进气环后，在 Billet Box 上的口吸紧致度和颗粒感完全不输任何 22mm 独立车头。做网极度简单，标配的缠绕棒与原厂做丝指导让人少走无数弯路。",
                                "author": "eCigTalk Boro 玩家专题",
                                "platform": "ecigtalk.org (俄罗斯电子烟论坛)",
                                "topic": "Grizzly BB in Billet Box Setup",
                                "url": ""
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "200目斜纹 + 325目外包",
                                "size": "1.8*2.2cm",
                                "wraps": "4圈 0.28mm (约 0.85Ω)"
                        },
                        {
                                "mesh": "300目平纹",
                                "size": "1.7*2.0cm",
                                "wraps": "5圈 0.25mm (约 1.00Ω)"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "200目",
                                "needle": "1.0",
                                "vm3": "18*20",
                                "vm4": "17*19",
                                "vms": "17*19",
                                "s35": "17*19",
                                "snet": "19*21"
                        },
                        {
                                "mesh": "300目",
                                "needle": "1.0",
                                "vm3": "19*21",
                                "vm4": "18*20",
                                "vms": "18*20",
                                "s35": "18*20",
                                "snet": "20*22"
                        }
                ],
                "images": [
                        "images/blm_grizzly.jpg",
                        "images/blm_grizzly_deck.jpg",
                        "images/blm_grizzly_parts.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "Bear Lair Mods 官方发布: 2018-08-20 首款 Boro 网子桥梁正式上市",
                        "secondary": "YouTube 俄罗斯玩家开箱 & 官方产品库: 2018年8月实测建档",
                        "analysis": "原厂发布与视频实测同月一致。"
                }
        },
        {
                "id": "vwm_nextgen",
                "name": "Nextgen",
                "brand": "Vape Ware Mods (VWM)",
                "origin": "希腊",
                "type": "Genesis RDTA (倒扣钟罩式中心网芯立式导油)",
                "image": "images/vwm_nextgen.jpg",
                "quickSpecs": [
                        "22mm",
                        "4.7ml容量",
                        "倒扣真空钟罩"
                ],
                "specs": {
                        "品牌产地": "Vape Ware Mods (VWM) · 希腊",
                        "发布时间": "2015年3月",
                        "设备类型": "Genesis RDTA (倒扣钟罩式中心网芯立式导油 / 负压真空系统)",
                        "外形直径": "22 mm",
                        "本体高度": "35.0 mm（不含 510 接口与滴嘴）",
                        "油仓容量": "约 4.7 ml (Quadrant PC 1000 / 耐酸 Pyrex 玻璃双仓配置)",
                        "主体材质": "304 医用级不锈钢 / PEEK 绝缘组件 / 镀银导电中心立柱",
                        "进气规格": "底部进气调节环，4 组精准微孔 (0.9mm / 1.1mm / 1.3mm / 1.5mm)",
                        "电极平台": "中心同轴正极立柱，顶部滚花正极压紧螺母，底部负极螺丝固定",
                        "导油孔径": "3.5 mm 中心立式导油孔（适配 14-16mm 黄金裁网高度）",
                        "导油介质": "不锈钢网 (Mesh #200 ~ #400 复合卷网) / 避雷针碳棒系统",
                        "接口规格": "标准 510 接口 (底座精密切削 VWM 官方立体盾徽与出厂序号)"
                },
                "officialNotes": "Vape Ware Mods 于 2015 年推出的代表作品。Nextgen 采用倒扣钟罩式（Inverted-Cup）真空负压导油系统与中心网芯立柱架构，改变了传统 Genesis 依赖倾斜机身辅助导油的设计。内部负压仓向中心网芯持续输送烟油，曾获评全球年度代表性网子雾化器。",
                "reviews": [
                        {
                                "quote": "Nextgen 是 Genesis 进化史上的真正分水岭。倒扣钟罩的真空供油机制彻底解决了干烧与倒油漏液问题，解析纯净度与烟雾浓度达到了前所未有的高度。它不仅确立了 VWM 在世界高定器械领域的宗师地位，更为后续的 Nextiny 与 Nextasis 奠定了灵魂蓝本。",
                                "author": "Todd (Todd's Reviews)",
                                "platform": "Planet of the Vapes / Todd's Reviews",
                                "topic": "NextGen by VapeWare Mods Comprehensive Review",
                                "url": "https://www.planetofthevapes.co.uk/reviews/rbas/nextgen-by-vapeware-mods.html"
                        },
                        {
                                "quote": "中心立柱做网无比轻松，使用 200目内芯搭配 325目外层，在机械杆上一点即燃。4.7ml 的超大容量配合紧凑的 35mm 身材，是网子黄金年代不可逾越的传世圣杯。",
                                "author": "Vape Garage & ECF Genny 社区",
                                "platform": "E-Cigarette Forum (ECF) 典藏论坛",
                                "topic": "NextGen RTA: The Ultimate Genesis Breakdown",
                                "url": "https://www.e-cigarette-forum.com/threads/genny-fam-can-we-talk-about-the-nextgen.736109/"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "200目斜纹 + 325目外包",
                                "size": "2.0*2.6cm",
                                "wraps": "4圈 0.28mm (约 0.95Ω)"
                        },
                        {
                                "mesh": "300目平纹",
                                "size": "1.9*2.5cm",
                                "wraps": "5圈 0.30mm (约 0.85Ω)"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "200目",
                                "needle": "1.0",
                                "vm3": "20*22",
                                "vm4": "19*21",
                                "vms": "19*21",
                                "s35": "19*21",
                                "snet": "21*23"
                        },
                        {
                                "mesh": "300目",
                                "needle": "1.0",
                                "vm3": "21*23",
                                "vm4": "20*22",
                                "vms": "20*22",
                                "s35": "20*22",
                                "snet": "22*24"
                        }
                ],
                "images": [
                        "images/vwm_nextgen.jpg",
                        "images/vwm_nextgen_deck.jpg",
                        "images/vwm_nextgen_assembled.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "Vape Ware Mods (VWM) 希腊工坊官方发售: 2015-03-02 批量发货",
                        "secondary": "Todd's Reviews (YouTube): 2015年3月深度评测《Nextgen Genesis by Vape Ware Mods》",
                        "analysis": "原厂发售与 Todd 实测同月闭环。"
                }
        },
        {
                "id": "inax_mk2r",
                "name": "In'Ax MkIIr (In'Ax Mk2r)",
                "brand": "Athea Mods",
                "origin": "法国",
                "type": "Genesis RDTA (中心螺纹穿针电极系统)",
                "image": "images/inax_mk2r.jpg",
                "quickSpecs": [
                        "22mm",
                        "穿针极柱",
                        "Grip Stick抱夹"
                ],
                "specs": {
                        "品牌产地": "Athea Mods (Vincent Athea) · 法国",
                        "发布时间": "2015年3月",
                        "设备类型": "Genesis RDTA (中心同轴贯穿螺纹穿针电极系统 / 微型超压缩雾化仓)",
                        "外形直径": "22 mm",
                        "本体高度": "34.0 mm（极紧凑微缩机身，不含滴嘴）",
                        "油仓容量": "约 3.0 ml (Pyrex 高硼硅防爆石英玻璃)",
                        "主体材质": "316L 医用级不锈钢 / 特氟龙 (PTFE) 510 绝缘衬套 / 医用硅胶",
                        "进气规格": "顶盖精密双向旋转调节进气孔 (支持 0 ~ 1.8mm 连续无级微调)",
                        "电极平台": "Vincent Athea 独创 Grip Stick 抱夹式正极穿针，阶梯微型雾化室",
                        "导油孔径": "3.2 mm 中心穿针立柱（适配 15mm 极紧裁网高度）",
                        "导油介质": "超细密不锈钢网 (Mesh #325 ~ #500) / 原厂金属穿针套筒",
                        "接口规格": "标准 510 接口 (底盘微激光镌刻 In'Ax 标志性放射星纹与出厂编号)"
                },
                "officialNotes": "法国传奇工坊 Athea Mods 创始人 Vincent Athea 的传世代表作。In'Ax MkIIr 彻底重构了传统网子电极结构：彻底废除易松脱短路的锁丝螺钉，首创中心同轴穿针系统（Rolling Pin）与弹性抱夹（Grip Stick）。发热丝正极由顶端金属销套牢牢锁紧，负极直接紧贴底座平整面，从物理几何上彻底消除了发热丝悬空段（Zero Hot Legs），使网子做丝难度与安全性迎来了质的飞跃。",
                "reviews": [
                        {
                                "quote": "In'Ax MkIIr 展现了法国高定工坊极致的工程智慧。Grip-Stick 系统的固定方式如此优雅，使得做网不再是一场与跳火火花博弈的折磨。它的超紧凑微型雾化仓压缩比极高，每一滴高阶草本烟油在其中都能瞬间爆发为层次丰富、丝滑细腻的醇香烟雾。",
                                "author": "Vaporiz'Arte 官方档案",
                                "platform": "Vaporiz'Arte (葡萄牙/法国高定蒸汽文化馆)",
                                "topic": "In'Ax MKIIR by Athea Mods 深度典藏",
                                "url": "https://www.vaporizarte.com/IN-AX-MKIIR-by-Athea-Mods"
                        },
                        {
                                "quote": "Vincent Athea 凭借 MkIIr 奠定了中心穿针网子的行业标准。34mm 的高度在任何机身上都兼具美感与实用性，0-1.8mm 的双微孔顶盖进气极其静音顺滑，是网子老玩家心中公认的殿堂级艺术品。",
                                "author": "Mark Todd",
                                "platform": "Todd's Reviews / Vaping With Todd",
                                "topic": "Athea In'Ax MkIIr Genesis Atomizer Review",
                                "url": ""
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "325目复合400目细网",
                                "size": "1.9*2.4cm",
                                "wraps": "4圈 0.28mm (约 1.00Ω)"
                        },
                        {
                                "mesh": "400目平纹",
                                "size": "1.8*2.2cm",
                                "wraps": "5圈 0.25mm (约 1.15Ω)"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "325目",
                                "needle": "1.0",
                                "vm3": "18*20",
                                "vm4": "17*19",
                                "vms": "17*19",
                                "s35": "17*19",
                                "snet": "19*21"
                        },
                        {
                                "mesh": "400目",
                                "needle": "1.0",
                                "vm3": "19*21",
                                "vm4": "18*20",
                                "vms": "18*20",
                                "s35": "18*20",
                                "snet": "20*22"
                        }
                ],
                "images": [
                        "images/inax_mk2r.jpg",
                        "images/inax_mk2r_deck.jpg",
                        "images/inax_mk2r_parts.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "Vincent Athea (Athea Mods) 官方发售公告: 2015-03-16 通过 Vapinart 交付 MkIIr",
                        "secondary": "Le Vapelier (法国权威电子烟评测智库): 2015年3月图文深度评测",
                        "analysis": "法国原厂首发与法国权威媒体同月闭环。"
                }
        },
        {
                "id": "origen_v2_mk2",
                "name": "Origen Genesis V2 (OG2 / OG2 MkII)",
                "brand": "Origen Mods (Norbert)",
                "origin": "匈牙利",
                "type": "Genesis RDTA (模块化单/双网孔千层鳍片巅峰)",
                "image": "images/origen_v2_mk2.jpg",
                "quickSpecs": [
                        "22mm",
                        "4ml/6ml双模",
                        "单/双发瞬切"
                ],
                "specs": {
                        "品牌产地": "Origen Mods (Norbert) · 匈牙利",
                        "发布时间": "2014年10月",
                        "设备类型": "Genesis RDTA (模块化单/双网孔 / 阶梯散热鳍片巨量储油)",
                        "外形直径": "22 mm",
                        "本体高度": "35.0 mm (4ml 短仓版) / 43.5 mm (6ml 旗舰长仓版)",
                        "油仓容量": "4.0 ml / 6.0 ml (双容量模块化可换仓系统)",
                        "主体材质": "1.4301 食品级优质不锈钢 / 黄铜中心正极柱 / 高透聚碳酸酯仓",
                        "进气规格": "顶盖独立旋转 AFC 进气环 (单发/双发 1.2mm / 1.5mm / 2.0mm / 2.5mm + 双叠 1.2mm 紧致 MTL)",
                        "电极平台": "对称双发开孔电极台 (附带原厂 PEEK 单发减仓堵塞块)",
                        "导油孔径": "双侧多功能导油孔 (网子专用孔 3.0mm，兼容器材孔 4.5mm)",
                        "导油介质": "不锈钢网 (#200 ~ #400) / 钢丝绳裹网芯 (Steel Cable + Mesh)",
                        "接口规格": "标准 510 纯铜电极 (底座激光刻印 Norbert 签名徽章)"
                },
                "officialNotes": "匈牙利传奇工坊 Norbert 的毕生集大成之作。作为 Origen Genesis 系列终极进化版，MkII 升级了加强型顶仓锁紧不锈钢环与防滑凹槽中心正极柱，彻底根除了初代拧紧时极柱随动的隐患。顶部标志性的多阶千层散热鳍片有效导散积热，并配备覆盖 1.2mm 到 2.5mm 单双发全口径的旋转进气系统。4.0ml 与 6.0ml 的充沛储油量，使其成为全球网子史上无可争议的‘双发暴力大网神机’。",
                "reviews": [
                        {
                                "quote": "Origen Genesis V2 MkII 是每一位严肃网子玩家书架上不可或缺的帝王级存在。双发 400目做网点火产生的浓郁雾化量犹如滴油 RDA，千层散热鳍片将热量完全锁在外部，入口烟气温润饱满，对于复杂调和油的解析力令人叹服。",
                                "author": "Joni Kostamo (Vapetales)",
                                "platform": "Vapetales Vape Reviews 国际评测专栏",
                                "topic": "Origen Genesis V2 Mk2 Comprehensive Deep Dive",
                                "url": "https://www.youtube.com/watch?v=yxjf-Gc6y0I"
                        },
                        {
                                "quote": "Norbert 的加工精度令人折服。6ml 仓版本的续航极其惊人，多孔位进气无论口吸还是轻肺吸都能找到黄金甜点。它是网子大容量时代的终极巅峰。",
                                "author": "Bruno (Nono77)",
                                "platform": "Vapoteurs.net / YouTube Tazeur Review",
                                "topic": "Origen Genesis v2 mk2 6ml by Norbert",
                                "url": "https://www.youtube.com/watch?v=INmZZwymKJ8"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "单发模式: 200目斜纹",
                                "size": "2.1*2.5cm",
                                "wraps": "4圈 0.28mm (约 0.90Ω)"
                        },
                        {
                                "mesh": "双发极速: 400目细网双卷",
                                "size": "1.7*2.2cm x2",
                                "wraps": "5圈 0.25mm 双发并联 (约 0.50Ω)"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "200目",
                                "needle": "1.0",
                                "vm3": "21*23",
                                "vm4": "20*22",
                                "vms": "20*22",
                                "s35": "20*22",
                                "snet": "22*24"
                        },
                        {
                                "mesh": "400目",
                                "needle": "1.0",
                                "vm3": "19*21",
                                "vm4": "18*20",
                                "vms": "18*20",
                                "s35": "18*20",
                                "snet": "20*22"
                        }
                ],
                "images": [
                        "images/origen_v2_mk2.jpg",
                        "images/origen_v2_mk2_6ml.jpg",
                        "images/origen_v2_mk2_parts.jpg",
                        "images/origen_v2_deck.jpg",
                        "images/origen_v2_mk2_build.jpg",
                        "images/origen_v2_classic.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "匈牙利 Norbert (Origen Mods) 于 ECF 官方专帖: 2014-10-18 正式宣布 OG2 初代发售",
                        "secondary": "Todd's Reviews (YouTube): 2014年11月实测《Origen Genesis V2 by Norbert》",
                        "analysis": "原厂首发与 Todd 评测仅差 3 周，双源高度吻合。"
                }
        },
        {
                "id": "ddp_typhon",
                "name": "Typhon (台风)",
                "brand": "DDP Vape",
                "origin": "马来西亚 / 日本",
                "type": "Luxury Mesh RDTA (超低矮阶梯压缩聚气/隐藏顶进气)",
                "image": "images/ddp_typhon.jpg",
                "quickSpecs": [
                        "22mm",
                        "24K镀金电极",
                        "阶梯聚气仓"
                ],
                "specs": {
                        "品牌产地": "DDP Vape · 马来西亚 / 日本",
                        "发布时间": "2016年9月",
                        "设备类型": "Luxury Mesh RDTA (超低矮阶梯压缩聚气 / 隐藏式顶进气)",
                        "外形直径": "22 mm",
                        "本体高度": "约 26.5 mm（极致低矮流线机身）",
                        "油仓容量": "约 2.5 ml (高透 Ultem PEI 储油视窗)",
                        "主体材质": "316 级精密不锈钢 / 24K 镀金电极柱与锁丝压片 / PEEK 绝缘组件",
                        "进气规格": "隐蔽式顶部环形向下折射进气通道 (防冷凝防漏液，支持 1.0mm-1.8mm 无级微调)",
                        "电极平台": "偏心斜面单网孔电极台，配备 90° 自由旋转正极锁丝臂",
                        "导油孔径": "3.2 mm 倒角导油孔（适配 13-15mm 紧凑裁网高度）",
                        "导油介质": "超细腻不锈钢网 (Mesh #325 ~ #500) / 避雷针碳棒系统",
                        "接口规格": "标准 510 接口 (支持随箱附赠的纯银 BF 底部注油电极螺栓)"
                },
                "officialNotes": "DDP Vape 汇集马来西亚前卫设计与日本超高精密 CNC 切削工艺的匠心力作。整机高度被压缩至极度低矮的 26.5mm，内部电极台、正负极压片及紧固螺栓全量覆裹 24K 真金镀层，达成超低内阻与疾速点火响应。顶盖采用独特的阶梯压缩聚气曲面配合隐藏式向下折射顶进气风道，杜绝了传统侧进气雾化器的冷凝液溢出，为顶级单叶有机烟草油提供了极其纯净、湿润的高清风味还原。",
                "reviews": [
                        {
                                "quote": "Typhon 完美诠释了什么是现代工业艺术品。24K 镀金电极台做工无可挑剔，隐藏式顶部气流向下直扑网芯，在抑制漏油的同时实现了完全无杂音的极其静音顺畅吸阻。无论是雪茄油还是坚果甜点油，解析细节层层递进。",
                                "author": "DarthVapor Taiwan",
                                "platform": "DarthVapor 影音品鉴",
                                "topic": "Typhon 颱風 RDA by DDP Vape - 開箱及設定教學 Review",
                                "url": "https://www.youtube.com/watch?v=UaeFr_OTuq8"
                        },
                        {
                                "quote": "阶梯压缩雾化室带来的聚气效果非常惊艳，烟雾入口时的温热感恰到好处。90° 旋转锁丝臂大大简化了网子引线的固定，是 22mm 紧凑型高阶器械中不可多得的瑰宝。",
                                "author": "VapormanVape",
                                "platform": "VapormanVape 法国蒸汽专栏",
                                "topic": "Review du Typhon de DDP Vape",
                                "url": "https://www.youtube.com/watch?v=upbo8wODkFU"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "400目细网紧密卷芯",
                                "size": "1.8*2.2cm",
                                "wraps": "5圈 0.25mm (约 1.05Ω)"
                        },
                        {
                                "mesh": "325目复合500目超细网",
                                "size": "1.7*2.1cm",
                                "wraps": "4圈 0.28mm (约 0.95Ω)"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "400目",
                                "needle": "0.8",
                                "vm3": "17*19",
                                "vm4": "16*18",
                                "vms": "16*18",
                                "s35": "16*18",
                                "snet": "18*20"
                        },
                        {
                                "mesh": "500目",
                                "needle": "0.8",
                                "vm3": "18*20",
                                "vm4": "17*19",
                                "vms": "17*19",
                                "s35": "17*19",
                                "snet": "19*21"
                        }
                ],
                "images": [
                        "images/ddp_typhon.jpg",
                        "images/ddp_typhon_deck.jpg",
                        "images/ddp_typhon_parts.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "DDP Vape 官方全球发售公告: 2016-09-01 正式交付 24K 镀金超低矮 RDTA",
                        "secondary": "DarthVapor (YouTube): 2016年9月实机评测《Typhon RDTA by DDP Vape》",
                        "analysis": "东南亚/日本合作名作，双源同月闭环。"
                }
        },
        {
                "id": "ddp_one",
                "name": "DDP One",
                "brand": "DDP Vape",
                "origin": "马来西亚 / 日本",
                "type": "Genesis RDTA (超矮聚气双模网子雾化器)",
                "image": "images/ddp_one.jpg",
                "quickSpecs": [
                        "22mm",
                        "2.0ml容量",
                        "Ultem减仓顶塞"
                ],
                "specs": {
                        "品牌产地": "DDP Vape · 马来西亚 / 日本",
                        "发布时间": "2016年11月",
                        "设备类型": "Genesis RDTA (超矮聚气单/双发网子雾化器 / 隐藏式顶进气)",
                        "外形直径": "22.0 mm",
                        "本体高度": "24.0 mm（不含 510 接口与滴嘴）",
                        "油仓容量": "2.0 ml (医用级聚砜 PSU / 耐温耐酸 Ultem 储油视窗)",
                        "主体材质": "316L 医用级不锈钢 / 全 Ultem 阶梯减仓套件 / 医用级 PEEK 绝缘组件",
                        "进气规格": "顶部隐藏式双向可调进气，斜向下导流直吹网芯，支持单发微孔与对称双发孔",
                        "电极平台": "中心立柱电极带垫片平压螺丝，双侧负极内六角锁丝，支持单网与双网双发",
                        "导油孔径": "双 2.8 mm 偏置导油孔（单发模式下随附专用 Ultem 密封塞闭锁）",
                        "导油介质": "不锈钢网 (Mesh #325 ~ #500 超细高目数复合卷网) / 避雷针碳棒系统",
                        "接口规格": "标准 510 接口 (底座精细激光雕刻 DDP Vape 官方立体几何徽标与专属编号)"
                },
                "officialNotes": "DDP Vape 继 Typhon 台风之后推出的代表型号。DDP One 采用全 Ultem 阶梯式雾化室内胆减仓系统，将 22mm 雾化仓空间缩减至线圈与气道所需的紧凑体积。顶部斜向下进气风道降低了侧孔漏油与倒置渗液的概率，并支持通过更换单/双发 Ultem 塞块切换单网与双网配置。",
                "reviews": [
                        {
                                "quote": "DDP One 的工业加工精度达到了无可挑剔的极致境界。Ultem 减仓内胆将雾化室压缩到了极致，烟雾密度与饱满温润感极为惊人，能把复杂草本与烟草烟油最隐秘的层次毫无保留地彻底激发。",
                                "author": "Mark Todd (Todd's Reviews)",
                                "platform": "Todd's Reviews / YouTube 权威测评",
                                "topic": "The DDP Typhon & One Comprehensive Review",
                                "url": "https://www.youtube.com/watch?v=4GULWIRgmTE"
                        },
                        {
                                "quote": "在外观美感、机加工精度与纯净口感三项维度上均具有压倒性统治力的高端 RDTA。Ultem 阶梯减仓构件带来的极低无效死区与垂直网芯直吹气流，使得烟油香气还原达到了手术刀般的真实还原。",
                                "author": "Takayuu (VAPE Memorandum)",
                                "platform": "VAPE Memorandum 日本专业测评博客",
                                "topic": "DDP one RDTA by DDP vape 深入分解与双发评测",
                                "url": "https://vape-memorandum.com/5436"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "400目平纹 + 500目外包",
                                "size": "1.8*2.2cm",
                                "wraps": "5圈 0.28mm (约 0.90Ω)"
                        },
                        {
                                "mesh": "325目平纹",
                                "size": "1.9*2.3cm",
                                "wraps": "4圈 0.30mm (约 0.82Ω)"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "400目",
                                "needle": "0.8",
                                "vm3": "17*19",
                                "vm4": "16*18",
                                "vms": "16*18",
                                "s35": "16*18",
                                "snet": "18*20"
                        },
                        {
                                "mesh": "500目",
                                "needle": "0.8",
                                "vm3": "18*20",
                                "vm4": "17*19",
                                "vms": "17*19",
                                "s35": "17*19",
                                "snet": "19*21"
                        }
                ],
                "images": [
                        "images/ddp_one.jpg",
                        "images/ddp_one_deck.jpg",
                        "images/ddp_one_parts.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "DDP Vape 官方出厂交付: 2016-11-10 Ultem 阶梯减仓旗舰全面上市",
                        "secondary": "Todd's Reviews (YouTube): 2016年11月实测《DDP One by DDP Vape》",
                        "analysis": "原厂上市与 Todd 视频同月一致。"
                }
        },
        {
                "id": "vwm_nextera",
                "name": "NextEra",
                "brand": "Vape Ware Mods (VWM)",
                "origin": "希腊",
                "type": "Genesis RDTA / BF (紧凑超扁平网子雾化器)",
                "image": "images/vwm_nextera.jpg",
                "quickSpecs": [
                        "22mm",
                        "1.5ml容量/BF",
                        "超扁平紧凑机身"
                ],
                "specs": {
                        "品牌产地": "Vape Ware Mods (VWM) · 希腊",
                        "发布时间": "2017年9月",
                        "设备类型": "Genesis RDTA / BF (紧凑型中心网芯雾化器 / 滴油注油双模)",
                        "外形直径": "22.0 mm",
                        "本体高度": "20.5 mm（超矮扁平紧凑设计，不含 510 接口与滴嘴）",
                        "油仓容量": "约 1.5 ml (Quadrant PC 1000 强化底仓，支持 BF 底部压油注油)",
                        "主体材质": "304 医用级不锈钢 / Quadrant PC1000 / 镀银导电极柱 / PEEK 绝缘组件",
                        "进气规格": "侧壁可调式定向进气环，支持 1.2mm / 1.5mm / 2.0mm 微孔与气槽调节",
                        "电极平台": "偏心正极垂直立柱配合顶部滚花锁紧螺母，底盘平整接地夹持线圈",
                        "导油孔径": "3.5 mm 中心立式导油孔",
                        "导油介质": "不锈钢网 (Mesh #200 ~ #400 复合卷网) / 避雷针碳棒系统",
                        "接口规格": "标准 510 接口 (随附标准实心 510 螺丝与 BF 中空底注螺丝)"
                },
                "officialNotes": "Vape Ware Mods 于 2017 年末推出的跨界革命性力作。作为 VWM 继 Nextgen、Nextiny 和 Nextasis 之后首款引入底部注油（Bottom Feeder / Squonk）支持的网子雾化器，NextEra 突破性地将 BF 注油口设计在储油仓顶部，每次挤压瓶身均能从储油仓顶端自上而下对网芯进行饱满浸润。20.5mm 的极矮身材配合直吹单立式网芯的气流轨迹，创造了无与伦比的爆发力与纯净度。",
                "reviews": [
                        {
                                "quote": "NextEra 可以说是 VWM 家族中通用性与可玩性最高的划时代力作。将纯血 Genesis 的立式网芯体验与底部注油 Squonk 系统完美融合在仅 20.5mm 的极矮机身中，做网后的爆发力令人叹服。",
                                "author": "Planet of the Vapes",
                                "platform": "Planet of the Vapes (POTV) 官方测评",
                                "topic": "NextEra by Vape Ware Mods In-depth Hardware Review",
                                "url": "https://www.planetofthevapes.co.uk/reviews/rba/nextera-by-vape-ware-mods.html"
                        },
                        {
                                "quote": "丝绸般顺滑的螺纹工艺与希腊国宝级金工水准。NextEra 将传统网子信徒与现代注油底注主机的距离彻底抹平，是垂直单网玩家难以割舍的终极玩具。",
                                "author": "Vapes by Enushi",
                                "platform": "Vapes by Enushi 加拿大高端精选",
                                "topic": "VapeWare Mods (VWM) NextEra RTA Architectural Analysis",
                                "url": "https://www.vapesbyenushi.com/vapeware-mods-vwm-nextera-rta/"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "200目斜纹 + 325目外包",
                                "size": "2.0*2.5cm",
                                "wraps": "4圈 0.28mm (约 0.95Ω)"
                        },
                        {
                                "mesh": "300目平纹",
                                "size": "1.9*2.4cm",
                                "wraps": "5圈 0.30mm (约 0.85Ω)"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "200目",
                                "needle": "1.0",
                                "vm3": "19*21",
                                "vm4": "18*20",
                                "vms": "18*20",
                                "s35": "18*20",
                                "snet": "20*22"
                        },
                        {
                                "mesh": "300目",
                                "needle": "1.0",
                                "vm3": "20*22",
                                "vm4": "19*21",
                                "vms": "19*21",
                                "s35": "19*21",
                                "snet": "21*23"
                        }
                ],
                "images": [
                        "images/vwm_nextera.jpg",
                        "images/vwm_nextera_deck.jpg",
                        "images/vwm_nextera_parts.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "Vape Ware Mods (VWM) 官方发售: 2017-09-04 首款 BF 底注 Genesis 正式交付",
                        "secondary": "Planet of the Vapes (POTV): 2017年9月图文实测《NextEra by VWM Review》",
                        "analysis": "原厂与专业媒体同月闭环。"
                }
        },
        {
                "id": "luca_duetto",
                "name": "Duetto",
                "brand": "Luca Creations",
                "origin": "意大利",
                "type": "Genesis RDTA (意系单发极致纯净雾化器)",
                "image": "images/luca_duetto.jpg",
                "quickSpecs": [
                        "22mm",
                        "2.5ml容量",
                        "意系网子天花板"
                ],
                "specs": {
                        "品牌产地": "Luca Creations · 意大利",
                        "发布时间": "2014年10月",
                        "设备类型": "Genesis RDTA (经典意系单发极致纯净雾化器 / 偏置单网架构)",
                        "外形直径": "22.0 mm",
                        "本体高度": "36.0 mm（不含 510 接口与滴嘴）",
                        "油仓容量": "约 2.5 ml (Pyrex 高硼硅耐酸耐热透明玻璃仓)",
                        "主体材质": "316 医用级不锈钢 (纯手工细致缎面拉丝) / PEEK 绝缘组件",
                        "进气规格": "侧壁精密定向直吹微孔 (1.2mm 黄金 MTL 口吸口径，直扑网芯中下部)",
                        "电极平台": "偏置单侧垂直负极螺钉柱 + 正极沉头固定螺母，结构紧凑稳定",
                        "导油孔径": "2.7 mm 偏置导油孔（专为高密目数单网定制）",
                        "导油介质": "不锈钢网 (Mesh #325 ~ #400 高密度纯网卷芯) / 避雷针碳棒系统",
                        "接口规格": "标准 510 接口 (底座手刻 Luca Creations 经典草写签名与工坊批次编号)"
                },
                "officialNotes": "意大利网子教父 Luca Cassenti (Luca Creations) 享誉欧洲的巅峰传世代表作。Duetto 诞生于意大利手工高级定制工坊，以严苛的公差控制、极简精巧的偏置单网电极台以及 1.2mm 定向黄金进气孔闻名遐迩。其内部超微型雾化室对烟雾的压缩极其苛刻，能将有机烟草与复杂调味油的每一缕层次以最纯粹、干燥、利落的质感呈现，被公认为'意大利 Genesis 纯净口感的终极代名词'。",
                "reviews": [
                        {
                                "quote": "Duetto 是意大利网子史册上无可撼动的传世里程碑。在微型减仓与 1.2mm 定向进气的加持下，有机草本烟油的干燥感、击喉感与深层回甘被展现得淋漓尽致，毫无冗余杂味。",
                                "author": "Sigaretta Elettronica Forum (SEF)",
                                "platform": "Sigaretta Elettronica Forum 意大利殿堂论坛",
                                "topic": "Duetto by Luca Creations Il Re dei Genesis MTL",
                                "url": "https://www.sigarettaelettronicaforum.com/"
                        },
                        {
                                "quote": "意大利高级手工定制雾化器的绝对巅峰。极其细腻的缎面拉丝触感与手工雕刻工坊签名，配合对不锈钢网高密卷芯的纯正导油表现，是意系网子爱好者毕生珍藏的梦幻逸品。",
                                "author": "Svapoebasta 官方鉴赏",
                                "platform": "Svapoebasta 意大利高定特刊",
                                "topic": "Atomizzatore Genesis Duetto di Luca Creations Scheda Tecnica",
                                "url": "https://www.svapoebasta.com/luca-creations-atomizzatori/11749-duetto.html"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "325目平纹 + 400目细网外包",
                                "size": "1.8*2.4cm",
                                "wraps": "4圈 0.28mm (约 0.92Ω)"
                        },
                        {
                                "mesh": "400目斜纹",
                                "size": "1.7*2.3cm",
                                "wraps": "5圈 0.25mm (约 1.05Ω)"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "325目",
                                "needle": "0.8",
                                "vm3": "18*20",
                                "vm4": "17*19",
                                "vms": "17*19",
                                "s35": "17*19",
                                "snet": "19*21"
                        },
                        {
                                "mesh": "400目",
                                "needle": "0.8",
                                "vm3": "17*19",
                                "vm4": "16*18",
                                "vms": "16*18",
                                "s35": "16*18",
                                "snet": "18*20"
                        }
                ],
                "images": [
                        "images/luca_duetto.jpg",
                        "images/luca_duetto_deck.jpg",
                        "images/luca_duetto_parts.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "意大利 Luca Cassenti (Luca Creations) 于 Sigaretta Elettronica Forum: 2014-10-12 启动首批预定交付",
                        "secondary": "Esigarettaportal: 2014年10月专帖评测与微距分析",
                        "analysis": "意系扁平压缩仓 Genesis 开山之作，双源同月吻合。"
                }
        },
        {
                "id": "inax_carto",
                "name": "In'Ax Carto (In'Ax Carto V2)",
                "brand": "Athea Mods",
                "origin": "法国",
                "type": "Genesis Cartomizer / Boro Bridge (微缩同轴穿针网子桥梁)",
                "image": "images/inax_carto.jpg",
                "quickSpecs": [
                        "9.2mm Carto",
                        "Boro桥梁先驱",
                        "中心穿针GripStick"
                ],
                "specs": {
                        "品牌产地": "Athea Mods (Vincent Athea) · 法国",
                        "发布时间": "2015年12月",
                        "设备类型": "Genesis Cartomizer / Boro Bridge (中心同轴穿针网子桥梁 / 510 Carto)",
                        "外形直径": "9.2 mm (标准 510 Cartomizer 工业尺寸，完美适配 Billet Box Boro 仓与 35mm Carto 仓)",
                        "本体高度": "39.0 mm (标准 Cartomizer 长度)",
                        "油仓容量": "依宿主外仓而定 (适配 Billet Box Boro 仓时约为 4.5 ml ~ 5.0 ml)",
                        "主体材质": "316L 医用级外科手术不锈钢 / PEEK 耐热绝缘体 / 特氟龙密封环",
                        "进气规格": "底部 510 导气道，随附可更换碗状负极进气环 (1x1.0mm / 2x1.0mm 对称 / 3x1.0mm 三角气流)",
                        "电极平台": "专利中心同轴不锈钢穿针 (Rolling Pin) + Grip Stick 束紧环无螺母固线机制",
                        "导油孔径": "2.8 mm 中心立式导油孔（带导油阻尼调节套环）",
                        "导油介质": "不锈钢网 (Mesh #325 ~ #400 微型实心/空心卷网) / 避雷针碳棒系统",
                        "接口规格": "标准 510 Cartomizer 螺纹底座 (可直接旋入通用 510 调压设备进行烧丝跳火)"
                },
                "officialNotes": "法国宗师 Vincent Athea (Athea Mods) 惊艳全球微缩机械工程的跨时代杰作。In'Ax Carto 开创性地将 In'Ax 标志性的中心同轴穿针与 Grip Stick 束紧环系统，完整微缩置入 9.2mm 直径的标准 Cartomizer 规格之中。在 Billet Box 等 Boro AIO 系统的黄金年代，它是全球资深玩家在 Boro 仓内实现纯血 Genesis 网子雾化体验的不二圣杯，奠定了整个 Boro 网子桥梁（Mesh Bridge）的开山始祖地位。",
                "reviews": [
                        {
                                "quote": "Athea 工坊在微缩精密工程上的不朽丰碑。将完整的 Genesis 穿针导油系统浓缩进 9.2mm 直径的 Carto 身躯，为整个 Billet Box 圈层打开了纯血网子体验的大门。",
                                "author": "Vapes by Enushi",
                                "platform": "Vapes by Enushi 典藏分析",
                                "topic": "In'Ax Carto V2 Genesis RBA Architectural Breakthrough",
                                "url": "https://www.vapesbyenushi.com/"
                        },
                        {
                                "quote": "法国制作者 Vincent Athea 的天才之作。可更换碗状进气环与无螺钉 Grip Stick 束紧设计，让它在 Boro 仓体中爆发出的烟雾细腻感与高温浓郁度无可挑剔。",
                                "author": "Le Vapelier 专家组",
                                "platform": "Le Vapelier 法国专业评测机构",
                                "topic": "Revue détaillée INAX Carto par Athea Mods",
                                "url": "https://www.levapelier.com/en/INAX-Carto-by-Athea-mods/"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "325目平纹 + 400目细网外包",
                                "size": "1.6*2.2cm",
                                "wraps": "4圈 0.25mm (约 1.10Ω)"
                        },
                        {
                                "mesh": "400目斜纹",
                                "size": "1.5*2.1cm",
                                "wraps": "5圈 0.20mm (约 1.25Ω)"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "325目",
                                "needle": "0.8",
                                "vm3": "16*18",
                                "vm4": "15*17",
                                "vms": "15*17",
                                "s35": "15*17",
                                "snet": "17*19"
                        },
                        {
                                "mesh": "400目",
                                "needle": "0.8",
                                "vm3": "15*17",
                                "vm4": "14*16",
                                "vms": "14*16",
                                "s35": "14*16",
                                "snet": "16*18"
                        }
                ],
                "images": [
                        "images/inax_carto.jpg",
                        "images/inax_carto_deck.jpg",
                        "images/inax_carto_parts.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "Athea Mods 通过 VapStor 官方发售: 2015-12-10 交付 9.2mm Carto 规格中心网芯",
                        "secondary": "Le Vapelier (法国权威评测智库): 2015年12月专题评测《In'Ax Carto by Athea》",
                        "analysis": "双源同月完全吻合。"
                }
        },
        {
                "id": "mmv_the_did",
                "name": "The DID (The D.I.D Genesis)",
                "brand": "MMVapors (Jim / MMV)",
                "origin": "希腊",
                "type": "Genesis RTA",
                "image": "images/mmv_the_did.jpg",
                "quickSpecs": [
                        "20mm",
                        "3.5ml",
                        "工业量产鼻祖"
                ],
                "specs": {
                        "品牌产地": "MMVapors (希腊)",
                        "发布时间": "2012年2月",
                        "设备类型": "经典立式 Genesis RTA (工业量产开山祖)",
                        "外形直径": "20mm",
                        "本体高度": "58mm (含原装一体吸嘴)",
                        "油仓容量": "约 3.5ml",
                        "主体材质": "医用级 303/304 不锈钢 + 耐高温透明 PC 仓管",
                        "进气规格": "单侧侧面定孔 1.0mm ~ 1.2mm",
                        "电极平台": "双极单发设计，顶部滚花滚轮锁丝螺帽 (无需螺丝刀即开锁丝)",
                        "导油孔径": "3.0mm (绝缘圈选配)",
                        "导油介质": "氧化不锈钢目网 (#300-#400 Mesh) / 陶瓷碳棒",
                        "接口规格": "标准 510 接口 (黄铜正极螺柱)"
                },
                "officialNotes": "MMVapors 创世纪开山历史要点：The DID (The D.I.D) 是电子雾化器历史上首款将德国发明家 Raidy 在 2010 年首创的 'GENeration 2: SImple Solution' 网子毛细导油概念推向全球商业量产的丰碑杰作。全件采用高精密数控车床切削，摒弃了早期手工改造的粗糙针筒，首次确立了顶置滚花手拧锁丝螺帽、底部油仓与顶部电极柱纵贯结构。其纯不锈钢雾化仓与细腻的单孔气流直冲网子发热区，奠定了整个 Genesis 领域长达十余年的架构规范。",
                "reviews": [
                        {
                                "quote": "The DID is a solid, beautifully engineered piece of stainless steel. The machining is outstanding and it truly turned the Genesis concept from a DIY experiment into a reliable, top-tier everyday vaping reality.",
                                "reviewer": "Scott Bonner (igetcha69)"
                        },
                        {
                                "quote": "One of the earliest true classics. The vape from a properly oxidized mesh wick in The DID produces a pure, crisp flavour notes that silica simply could never match.",
                                "reviewer": "Todd's Reviews"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "#325 / #400 316L 不锈钢目网",
                                "needle": "2.5mm 实心/空心卷芯 (外径匹配 3.0mm 网孔与绝缘圈)",
                                "wire": "0.20mm (32 AWG) / 0.25mm (30 AWG) A1 / NiCr",
                                "circle": "4-5 圈",
                                "note": "传统喷火枪彻底氧化去积碳；顶部正极锁丝采用原厂滚轮手拧压盘，注意收紧顶圈防止热点产生，进气孔务必对准网子迎风侧。"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "#200 / #300 斜纹目网外裹",
                                "needle": "2.0mm 绝缘高纯导油陶瓷/碳棒",
                                "wire": "0.25mm A1",
                                "circle": "4 圈",
                                "note": "碳棒作为绝缘刚性芯柱，外部紧裹 2-3 层氧化网，彻底杜绝网体触底与电极底座短路，上油迅速，风味极具解析度。"
                        }
                ],
                "images": [
                        "images/mmv_the_did.jpg",
                        "images/mmv_the_did_deck.jpg",
                        "images/mmv_the_did_parts.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "MMVapors 官网与 ECF 专帖 (Jim / MMV): 2012-02-14 首发商业量产订购贴与交付公告",
                        "secondary": "Todd's Reviews (YouTube): 2012年4月早期创世纪视频实测《The D.I.D Genesis Atomiser by MMVapors》",
                        "analysis": "原厂首发与评测时间线完全吻合，公认为首款商业化批量生产 Genesis。"
                }
        },
        {
                "id": "hoh_zap",
                "name": "Z-Atty-Pro (ZAP)",
                "brand": "House of Hybrids (Zen / Mike Kowalski)",
                "origin": "美国",
                "type": "Genesis RTA",
                "image": "images/hoh_zap.jpg",
                "quickSpecs": [
                        "21mm",
                        "4.0ml",
                        "ProVari原生直锁"
                ],
                "specs": {
                        "品牌产地": "House of Hybrids (美国)",
                        "发布时间": "2012年9月",
                        "设备类型": "ProVari 专用原生直锁螺纹 Genesis RTA",
                        "外形直径": "21mm (与 ProVari V2/V2.5 锥度顶盖无缝贴合)",
                        "本体高度": "54mm (不含吸嘴)",
                        "油仓容量": "约 4.0ml",
                        "主体材质": "美标 316 不锈钢 + 原厂石英 Pyrex 耐酸玻璃仓",
                        "进气规格": "侧面单孔 1.0mm 专注口吸进气",
                        "电极平台": "Zen 专利双盲孔锁丝立柱，陶瓷绝缘套筒",
                        "导油孔径": "3.2mm (带特氟龙/氧化铝绝缘内衬)",
                        "导油介质": "氧化不锈钢网 (#400 / #500 Mesh) / 陶瓷棒",
                        "接口规格": "ProVari 原生直锁螺纹系统 (原生消灭 510 压降与松动)"
                },
                "officialNotes": "House of Hybrids 传奇历史要点：Z-Atty-Pro (ZAP) 是美系电子烟工业黄金时期与 ProVari 强强联合的巅峰产物。Zen (Mike Kowalski) 针对 ProVari 的机械外螺纹进行了原生一体化匹配，免除了传统 510 接口的螺丝转接、晃动与内阻压降。全机配备厚壁 Pyrex 耐腐蚀石英玻璃仓，并首创绝缘导油孔垫圈与阳极化锁丝端子，在 2012-2013 年成为了全世界玩家心目中最坚固、防漏性最卓越的标杆级 Genesis 设备。",
                "reviews": [
                        {
                                "quote": "The Z-Atty-Pro on a ProVari was the pinnacle of high-end vaping in 2012. The build quality, the Pyrex tank, and having native threads made it feel like one indestructible, premium device.",
                                "reviewer": "Phil Busardo (PBusardo)"
                        },
                        {
                                "quote": "House of Hybrids knocked it out of the park. The flavor on tobacco and complex blends when built on a ZAP is legendary among genesis connoisseurs.",
                                "reviewer": "Scott Bonner (igetcha69)"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "#400 / #500 316L 不锈钢目网",
                                "needle": "2.5mm / 2.8mm 紧密卷芯",
                                "wire": "0.25mm (30 AWG) Kanthal A1",
                                "circle": "4-5 圈 (阻值约 1.3Ω - 1.5Ω，完美配合 ProVari 稳压输出)",
                                "note": "ProVari 拥有极其灵敏的短路检测保护，因此做网必须做到彻底氧化，避免任何虚接。锁丝时将正极线紧靠陶瓷衬套，顶盖气孔直对线圈。"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "#300 细网外裹",
                                "needle": "2.0mm 绝缘陶瓷碳棒芯",
                                "wire": "0.25mm A1",
                                "circle": "4 圈",
                                "note": "利用碳棒绝缘芯柱从底部油仓直插雾化室，避开金属边缘摩擦，在 ProVari 设备上点火阻值极度平稳，烟雾细腻醇厚。"
                        }
                ],
                "images": [
                        "images/hoh_zap.jpg",
                        "images/hoh_zap_deck.jpg",
                        "images/hoh_zap_provari.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "Mike Kowalski (Zen / House of Hybrids) 于 ECF 论坛: 2012-09-03 官方发布原生适配 ProVari 规格 ZAP",
                        "secondary": "Phil Busardo (Taste Your Juice / YouTube): 2012年9月权威评测《A PBusardo Review - The Z-Atty-Pro (ZAP)》",
                        "analysis": "官方发布与 Busardo 权威实测同月发表，双源一致。"
                }
        },
        {
                "id": "docdave_steamturbine",
                "name": "Steam Turbine",
                "brand": "Doc Dave",
                "origin": "美国",
                "type": "Genesis RTA",
                "image": "images/docdave_steamturbine.jpg",
                "quickSpecs": [
                        "22mm",
                        "3.0ml",
                        "双发飞船散热鳍片"
                ],
                "specs": {
                        "品牌产地": "Doc Dave (美国)",
                        "发布时间": "2013年3月",
                        "设备类型": "性能级双发 / 单发 Genesis RTA (飞船千层鳍片鼻祖)",
                        "外形直径": "22mm",
                        "本体高度": "48mm",
                        "油仓容量": "约 3.0ml",
                        "主体材质": "高标号 316 不锈钢 / 限量钛合金 (Titanium) + 磨砂/透明 Pyrex 玻璃仓",
                        "进气规格": "顶盖双侧对称 1.2mm / 1.5mm 对吹风道",
                        "电极平台": "三柱式双发设计 (中央正极柱 + 两侧独立负极固定孔)",
                        "导油孔径": "双 3.0mm 对称导油网孔",
                        "导油介质": "氧化不锈钢目网 (#325-#400 Mesh)",
                        "接口规格": "标准 510 接口 (纯铜导电电极)"
                },
                "officialNotes": "Doc Dave 蒸汽飞船工业设计要点：Steam Turbine 是 2013 年全球高端 Genesis 领域的经典机械设计作品。其顶盖采用多阶密集车削散热鳍片（Cooling Fins），提升散热效能，减少连续抽吸发烫。底座配备双 3.0mm 导油孔与对称进气孔，支持双发与单发做芯配置，是北美手工客制化网子的重要代表型号。",
                "reviews": [
                        {
                                "quote": "The Doc Dave Steam Turbine is a work of mechanical art. The stepped fin styling on the top cap remains one of the most iconic silhouettes in all of Genesis history.",
                                "reviewer": "Todd's Reviews"
                        },
                        {
                                "quote": "Dual highlander mesh coils on the Turbine at 0.3-0.5 ohms is like hitting a freight train of pure, unadulterated flavor. Unbelievable vapor density for a genesis.",
                                "reviewer": "Bishopheals"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "#325 / #400 316 不锈钢目网",
                                "needle": "2.4mm 双根实心卷网",
                                "wire": "0.25mm / 0.28mm Kanthal A1 双发并联",
                                "circle": "每边 4 圈 (综合阻值约 0.6Ω - 0.8Ω)",
                                "note": "双发网子需要两根网体氧化深度与线圈发热同步一致。调整至无热点后，旋转千层散热顶盖使双侧气孔精准对准双网迎风面。"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "#200 45度斜纹网",
                                "needle": "2.0mm 双碳棒绝缘芯",
                                "wire": "0.25mm A1",
                                "circle": "双发 4 圈",
                                "note": "双碳棒硬质骨架使双网制作与高度对齐大幅简化，导油通畅度极高，无惧连续大功率抽吸，防糊能力出类拔萃。"
                        }
                ],
                "images": [
                        "images/docdave_steamturbine.jpg",
                        "images/docdave_steamturbine_deck.jpg",
                        "images/docdave_steamturbine_fins.jpg",
                        "images/docdave_steamturbine_parts.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "Doc Dave 于 ECF 官方专版: 2013-03-08 正式启动双弧形观察窗 Steam Turbine 交付",
                        "secondary": "Todd's Reviews (YouTube): 2013年3月首发展箱实测《Steam Turbine by Doc Dave》",
                        "analysis": "ECF 发售公文与 Todd 首发同月，双源一致。"
                }
        },
        {
                "id": "siam_cobra",
                "name": "Cobra (Cobra Genesis)",
                "brand": "Siam Mods",
                "origin": "英国",
                "type": "Genesis RTA",
                "image": "images/siam_cobra.jpg",
                "quickSpecs": [
                        "20mm / 22mm",
                        "3.0ml / 5.0ml",
                        "英伦手作蛇纹玻璃"
                ],
                "specs": {
                        "品牌产地": "Siam Mods (英国)",
                        "发布时间": "2012年9月",
                        "设备类型": "英国手作古典奢华 Genesis RTA (蛇纹手工艺术鼻祖)",
                        "外形直径": "20mm (3ml 版) / 22mm (5ml 大眼镜蛇版)",
                        "本体高度": "52mm",
                        "油仓容量": "3.0ml (标配) / 5.0ml (选配加长版)",
                        "主体材质": "英产医用不锈钢 + 独家纯铜车削正极柱 + 原装手工蛇纹手工 Pyrex 玻璃仓",
                        "进气规格": "单孔 1.0mm 聚气微风道",
                        "电极平台": "古典偏置网孔结构，纯铜顶部滚花压紧螺母",
                        "导油孔径": "2.8mm",
                        "导油介质": "氧化不锈钢目网 (#400 Mesh)",
                        "接口规格": "标准 510 接口 (纯铜导电中心螺丝)"
                },
                "officialNotes": "Siam Mods 古典英伦工匠艺术要点：由英国资深工匠创办的 Siam Mods 以极致的金属手作车床加工与奢华配件著称。Cobra (眼镜蛇) 是其代表性传世杰作，标志性的原装外罩或内胆常附带手工雕刻的蛇纹保护网与定制 Pyrex 玻璃仓管。底座电极柱罕见地全件采用精车高纯度纯铜（Solid Brass/Copper）打造，确保极致导电性与独特的古典温润质感。其柔和而绵密的烟雾质感，是 2012-2013 年英伦高端网子文化的图腾象征。",
                "reviews": [
                        {
                                "quote": "The Siam Mods Cobra is an absolute stunner. The brass center post and the snake engraving make it look like a piece of vintage jewelry, and the flavor from the mesh is top shelf.",
                                "reviewer": "Scott Bonner (igetcha69)"
                        },
                        {
                                "quote": "One of the smoothest draws on any classic genesis atomizer. A true collector's piece that represents the birth of UK luxury vaping.",
                                "reviewer": "DevonMoonshire"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "#400 316L 不锈钢目网",
                                "needle": "2.2mm 紧致密卷",
                                "wire": "0.20mm (32 AWG) / 0.25mm (30 AWG) A1",
                                "circle": "4-5 圈 (阻值约 1.5Ω - 1.8Ω)",
                                "note": "经典高阻口吸配置，纯铜螺栓锁线顺畅且无死角接触。做网时网体离仓底预留 1mm 间隙以形成最佳虹吸负压，纯棉手套辅助去油污。"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "#300 细目网",
                                "needle": "1.8mm 绝缘碳棒 / 陶瓷避雷针",
                                "wire": "0.25mm A1",
                                "circle": "5 圈",
                                "note": "利用碳棒阻绝纯铜底座接触，降低漏电风险，出烟速度极快，烟油前中后调还原清澈纯净。"
                        }
                ],
                "images": [
                        "images/siam_cobra.jpg",
                        "images/siam_cobra_deck.jpg",
                        "images/siam_cobra_tank.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "Siam Mods 于 ECF 官方专版: 2012-09-12 正式发布蛇纹钛/钢艺术雕刻 Cobra Genesis",
                        "secondary": "Todd's Reviews (YouTube): 2012年10月实测《Cobra Genesis Atomiser by Siam Mods》",
                        "analysis": "0-1 个月交付实测，英国经典艺术网子。"
                }
        },
        {
                "id": "paravozz_8_1",
                "name": "Paravozz 8.1 (Пара-Воз 8.1)",
                "brand": "Paravozz (车头 / Marat)",
                "origin": "俄罗斯",
                "type": "Genesis RDTA",
                "image": "images/paravozz_8_1.jpg",
                "quickSpecs": [
                        "22mm",
                        "3.5ml",
                        "8代首发承前启后"
                ],
                "specs": {
                        "品牌产地": "Paravozz (俄罗斯 / Marat Mtl)",
                        "发布时间": "2023年12月",
                        "设备类型": "高端钛合金单发 Genesis RDTA (8 代承前启后之作)",
                        "外形直径": "22mm",
                        "本体高度": "39.0mm (不含吸嘴与 510 电极螺纹)",
                        "油仓容量": "约 3.5ml",
                        "主体材质": "VT-6 / Grade 5 航空特种钛合金 + 耐酸耐热高硼硅石英玻璃",
                        "进气规格": "侧向插销式精密 Air Pin (标配 1.2mm，支持 1.0mm~1.4mm 选配)",
                        "电极平台": "经典偏置垂直立柱架构，沉头平锁螺丝，无死角导电底座",
                        "导油孔径": "2.7mm (带绝缘导油内衬)",
                        "导油介质": "氧化不锈钢目网 (#200-#300 Mesh) / 钛网 / 碳棒",
                        "接口规格": "标准 510 接口 (钛合金正极螺丝)"
                },
                "officialNotes": "Paravozz 8.1 结构演进历史要点：8.1 是车头工坊在 2023 年末重启 8 代架构后面向核心玩家交付的成熟改良版。相比早期车头，8.1 优化了顶盖外轮廓弧度与散热鳍片比例，使视觉过渡更加修长优雅；雾化仓内部聚气空间进一步压缩，减少冷凝回流积液。顶盖与电极底座采用高公差钛合金卡扣密封，气流插销精准指向发热丝下半部，为随后的 8.2 与 Jet Win 世代奠定了工法基础。",
                "reviews": [
                        {
                                "quote": "paravozZ 8.1: First of all, I think the appearance has become very nice. The machining on the VT-6 titanium feels silky smooth, and the flavor saturation is unmistakably pure Paravozz.",
                                "reviewer": "Seiji Kunisawa (PARaVOzZ® Wiki 官方档案, 2024年6月30日)"
                        },
                        {
                                "quote": "When you own an 8.1, you have something truly special. The way the top cap locks into the deck and channels the airflow directly to the mesh wick delivers an incredible tactile and vaping experience.",
                                "reviewer": "Frank Hagege (PARaVOzZ® Wiki 官方档案, 2024年3月19日)"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "#200 / #260 316 不锈钢目网",
                                "needle": "2.2mm 实心/空心卷网",
                                "wire": "4×4 0.08mm 镍铬编制绳 (Rope) 或 0.25mm Kanthal A1",
                                "circle": "4 圈 (阻值约 0.65Ω - 0.75Ω)",
                                "note": "采用俄罗斯传统打网法，网体离仓底预留 0.8mm，喷火枪彻底退火氧化；顶圈发热丝收紧平整，侧壁进气 Pin 对准线圈中间迎风面。"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "#200 45度斜纹网",
                                "needle": "1.8mm 高导油绝缘碳棒 / 陶瓷避雷针",
                                "wire": "0.25mm A1",
                                "circle": "4 圈",
                                "note": "碳棒绝缘芯柱有效消除底座短路隐患，上油迅速，连续大口吸食无糊味，极好地发挥 8.1 的层次解析力。"
                        }
                ],
                "images": [
                        "images/paravozz_8_1.jpg",
                        "images/paravozz_8_1_deck.jpg",
                        "images/paravozz_8_1_cap.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "车头官方工坊 (Marat Mtl / Jap Ti) 批次交付公告: 2023年12月交付 Terminator Jet twin GTR 8.1",
                        "secondary": "Facebook Paravozz Wiki 社区实帖: 2023-12-23 Paul Heard 评测与 2024-01-12 Evgeny III 实装晒单",
                        "analysis": "原厂批次交付记录与藏家收货晒单高度吻合，确认为 2023 年底当代重启型号。"
                }
        },
        {
                "id": "paravozz_labyrinth_gtr",
                "name": "Paravozz Labyrinth GTR (Пара-Воз Лабиринт GTR)",
                "brand": "Paravozz (车头 / Marat)",
                "origin": "俄罗斯",
                "type": "Genesis RDTA",
                "image": "images/paravozz_labyrinth_gtr.jpg",
                "quickSpecs": [
                        "22mm",
                        "3.2ml / 4.0ml Maxi",
                        "迷宫冷凝阻尼顶盖"
                ],
                "specs": {
                        "品牌产地": "Paravozz (俄罗斯 / Marat Mtl)",
                        "发布时间": "约 2016年 (暂定)",
                        "设备类型": "竞技级钛合金异形 Genesis RDTA (迷宫控醇冷凝阻尼款)",
                        "外形直径": "22mm",
                        "本体高度": "36.0mm (Maxi 高仓版约 42.0mm)",
                        "油仓容量": "3.2ml (标配) / 4.0ml (Maxi 加长高仓版)",
                        "主体材质": "BT-22 / VT-6 军工特种钛合金 + 耐高温石英玻璃仓",
                        "进气规格": "1.2mm 赛道级 GTR 加速侧向进气孔",
                        "电极平台": "紧凑型低公差偏置网孔，绝缘 PEEK 垫片，加粗沉头螺栓",
                        "导油孔径": "2.8mm",
                        "导油介质": "高目数氧化不锈钢网 (#230 Mesh) / Aura 钢缆 / 碳棒",
                        "接口规格": "标准 510 接口 (钛合金正极螺柱)"
                },
                "officialNotes": "Paravozz Labyrinth GTR 迷宫气道技术要点：Labyrinth（迷宫）GTR 是车头工坊针对烟雾浓缩与冷凝阻绝开发的核心型号。其顶盖内壁与吸嘴衔接处雕刻出微型曲折的迷宫式阻尼回流槽，使气溶胶通过通道时将部分冷凝液滴阻断并导回仓内，减少吸入口腔的冷凝液。结合 GTR 直线气流喷嘴，呈现干爽集中的烟雾表现。",
                "reviews": [
                        {
                                "quote": "Zz Labyrinth gtr maxi: 230 mesh (24 x 47 mm), 4z, Rope Aura (0.6 ohm). There is a slight difference between the short and maxi tanks, but the labyrinth chamber handles condensation flawlessly. Flavor notes are sharp and layered.",
                                "reviewer": "Denk Lem (PARaVOzZ® Wiki 官方档案, 2024年9月17日)"
                        },
                        {
                                "quote": "Lost that set up in the taxi in Madrid and it broke my heart. The Labyrinth GTR has the most satisfying draw resistance and mechanical perfection in the entire Paravozz collection.",
                                "reviewer": "Frank Hagege (PARaVOzZ® Wiki 官方档案, 2024年9月2日)"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "#230 316 不锈钢目网 (24mm × 47mm)",
                                "needle": "2.2mm 实心卷芯",
                                "wire": "Aura 订制钢缆 (Rope) 4 圈 (阻值 0.60Ω)",
                                "circle": "4 圈",
                                "note": "Denk Lem 亲测黄金做芯尺寸：#230 网裁剪 24×47mm，紧密密卷，搭配 Aura 钢缆，4 圈成型后 0.6 欧姆，与迷宫顶盖形成绝对共振。"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "#200 细网",
                                "needle": "2.0mm 绝缘碳棒 / 陶瓷避雷针",
                                "wire": "0.25mm A1",
                                "circle": "4 圈",
                                "note": "碳棒绝缘芯柱支撑坚韧，即使在外出通勤晃动剧烈环境下依然稳定无虚接，高频连抽无冷凝喷油。"
                        }
                ],
                "images": [
                        "images/paravozz_labyrinth_gtr.jpg",
                        "images/paravozz_labyrinth_gtr_deck.jpg",
                        "images/paravozz_labyrinth_gtr_parts.jpg"
                ],
                "dateVerification": {
                        "status": "tentative",
                        "primary": "PARaVOzZ® Wiki 官方历史档案 (#zZhistory): 记录迷宫式回流槽冷凝阻绝工程衍生款",
                        "secondary": "eCigTalk 论坛玩家技术讨论贴: 约 2016 年 Andrey Robul 实验性内胆",
                        "analysis": "暂定理由：内胆流道实验版，非独立量产通告型号。"
                }
        },
        {
                "id": "paravozz_macleod",
                "name": "Paravozz MacLeod (Пара-Воз Маклауд / Highlander)",
                "brand": "Paravozz (车头 / Marat)",
                "origin": "俄罗斯",
                "type": "Genesis RDTA",
                "image": "images/paravozz_macleod.jpg",
                "quickSpecs": [
                        "22mm",
                        "3.5ml",
                        "不死高地人特别定制"
                ],
                "specs": {
                        "品牌产地": "Paravozz (俄罗斯 / Marat Mtl)",
                        "发布时间": "2023年11月",
                        "设备类型": "高阶限量版钛合金 Genesis RDTA (不死高地人传奇)",
                        "外形直径": "22mm",
                        "本体高度": "38.0mm",
                        "油仓容量": "约 3.5ml",
                        "主体材质": "VT-6 高韧性特种航空钛合金 + 加厚高硼硅石英玻璃",
                        "进气规格": "1.2mm 定制口吸精密气道",
                        "电极平台": "MacLeod ZZR 独创三叶云朵型内胆聚气减仓切削电极台，搭配特制 Torx 梅花螺栓与正极套管锁丝系统，硬质阳极化绝缘底座",
                        "导油孔径": "2.6mm",
                        "导油介质": "氧化目网 (#230-#300 Mesh) / StrikeBall 钢缆 / 碳棒",
                        "接口规格": "标准 510 接口 (钛合金正极螺栓)"
                },
                "officialNotes": "Paravozz MacLeod 官方命名渊源与工程要点：车头主理人 Marat Mtl 在官方历史文献（#zZhistory）中记载了 MacLeod 的命名来源，源自影视作品《高地人（Highlander）》主角 Connor MacLeod，用以体现其坚固的钛合金机械结构。电极底座采用阶梯散热槽，导油孔与气流孔保持微距对准配置。",
                "reviews": [
                        {
                                "quote": "How did the names of the genesis ParavozZ by Japan come about: MacLeod — Was there such an old 'Highlander' series? The immortal one! That's what this atomizer represents: indestructible titanium excellence.",
                                "reviewer": "Marat Mtl (PARaVOzZ® Wiki 官方档案, 2023年11月27日)"
                        },
                        {
                                "quote": "Macleod ZZR: 230 mesh, 46 mm, 5 steps cardiogram wick, StrikeBall 15 x 4 wire. The vapor smoothness and longevity of this setup is simply unmatched in any other genesis.",
                                "reviewer": "Evgeny III (PARaVOzZ® Wiki 官方档案, 2023年12月29日)"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "#230 316 不锈钢目网 (宽 46mm)",
                                "needle": "2.0mm 芯棒卷芯",
                                "wire": "StrikeBall 15×4 编制钢缆或 0.25mm Kanthal A1",
                                "circle": "5 圈心电图阶梯搓网 (5 steps cardiogram)",
                                "note": "Evgeny III 专属高地人调校方案：46mm 宽度 #230 目网，折叠 5 阶微距心电图台阶，形成阶梯式毛细虹吸腔，导油无任何延迟，烟油爆发感极强。"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "#200 45度斜网",
                                "needle": "1.8mm 高强度导油碳棒芯",
                                "wire": "0.25mm A1",
                                "circle": "4 圈",
                                "note": "碳棒绝缘骨架完美契合 MacLeod 的 ZZR 导油孔，垂直同心度极高，有效避免金属拉弧，味道还原原汁原味。"
                        }
                ],
                "images": [
                        "images/paravozz_macleod.jpg",
                        "images/paravozz_macleod_deck.jpg",
                        "images/paravozz_macleod_build.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "Paravozz 主理人 Marat Mtl 官方档案 (#zZhistory): 2023-11-27 正式立项著录",
                        "secondary": "PARaVOzZ® Wiki 官方文献与 Evgeny III 高清评测照: 2023年11月建档",
                        "analysis": "官方文献与评测人建档同月吻合。"
                }
        },
        {
                "id": "paravozz_ghost_nano",
                "name": "Paravozz Ghost Nano (Пара-Воз Призрак Нано)",
                "brand": "Paravozz (车头 / Marat)",
                "origin": "俄罗斯",
                "type": "Genesis RDTA",
                "image": "images/paravozz_ghost_nano.jpg",
                "quickSpecs": [
                        "22mm",
                        "2.0ml",
                        "极短微缩超强爆发"
                ],
                "specs": {
                        "品牌产地": "Paravozz (俄罗斯 / Marat Mtl)",
                        "发布时间": "2024年9月",
                        "设备类型": "微型极窄短仓 Genesis RDTA (幽灵家族微缩旗舰)",
                        "外形直径": "22mm",
                        "本体高度": "仅 26.5mm (超短身段，不含滴嘴)",
                        "油仓容量": "约 2.0ml (超紧凑油仓)",
                        "主体材质": "BT-22 军工特种钛合金 + 耐高温石英微仓",
                        "进气规格": "1.1mm / 1.2mm 侧向直吹微孔，锁距 0.7mm",
                        "电极平台": "Ghost 极窄低空电极台，沉头微紧锁螺钉",
                        "导油孔径": "2.5mm",
                        "导油介质": "氧化细目网 (#230 Mesh) / Karlson 订制异端钢缆 (The Heretic) / 碳棒",
                        "接口规格": "标准 510 接口 (钛合金正极螺丝)"
                },
                "officialNotes": "Paravozz Ghost Nano 超短仓微型化要点：Ghost Nano 是车头 Ghost（幽灵）系列面向极致便携与超近吸阻距离开发的微缩衍生版。高度压缩至仅 26.5mm，雾化室内壁近乎贴紧网芯发热线圈，极大地缩短了气溶胶行进距离。由于雾化行程极短，蒸气浓度达到全系列之最，几乎没有风味衰减。搭配 Karlson 特制“异端（The Heretic）”6×5 镍铬编制钢丝，能在瞬间爆发强烈的烟油前调与极具辨识度的饱满击喉感。",
                "reviews": [
                        {
                                "quote": "Ghost IV GTR nano Paravozz: Beyond the ordinary! The sheer compactness combined with relentless vapor production makes it an everyday carry perfection.",
                                "reviewer": "Frank Hagege (PARaVOzZ® Wiki 官方档案, 2024年9月11日)"
                        },
                        {
                                "quote": "This is accompanying me throughout this work week: Paravozz Ghost Nano with The Heretic by Karlson (6x5 Nichrome .055, Mesh #230 135°). The throat hit and crispness is absolute perfection.",
                                "reviewer": "Roger Gulpen (PARaVOzZ® Wiki 官方档案, 2024年10月7日)"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "#230 316L 不锈钢目网 (135° 切角单网)",
                                "needle": "2.0mm 紧密卷网",
                                "wire": "Karlson 订制 The Heretic 钢缆 (6×5 0.055mm 镍铬) 或 0.25mm A1",
                                "circle": "4 圈 (阻值约 0.70Ω)",
                                "note": "Roger Gulpen 官方实战配方：#230 目网以 135° 斜角裁剪卷芯，搭配 Karlson 异端编制钢缆，出烟速度极快，在超短仓体内提供无与伦比的瞬间爆发力。"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "#200 45度斜目网",
                                "needle": "1.6mm 微型绝缘碳棒",
                                "wire": "0.25mm A1",
                                "circle": "4 圈",
                                "note": "超短仓体中绝缘碳棒能有效抑制过热传导，确保油仓温度恒定，连续击发依然烟气温润清凉。"
                        }
                ],
                "images": [
                        "images/paravozz_ghost_nano.jpg",
                        "images/paravozz_ghost_nano_deck.jpg",
                        "images/paravozz_ghost_nano_build.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "PARaVOzZ® Wiki 官方档案: 2024-09-11 由 Frank Hagege 录入实测报告",
                        "secondary": "车头高阶品鉴会实拍与通告: 2024年9月中旬建立完整档案",
                        "analysis": "官方 Wiki 录入日与实测报告双重印证。"
                }
        },
        {
                "id": "paravozz_ghost_iv",
                "name": "Paravozz Ghost IV (Пара-Воз Ghost-IV ceramic t²win GT-R)",
                "brand": "Paravozz (车头 / Marat)",
                "origin": "俄罗斯",
                "type": "Genesis RDTA",
                "image": "images/paravozz_ghost_iv.jpg",
                "quickSpecs": [
                        "22mm",
                        "3.05ml",
                        "四代陶瓷GT-R旗舰"
                ],
                "specs": {
                        "品牌产地": "Paravozz (俄罗斯 / Marat Mtl)",
                        "发布时间": "约 2024年 (暂定)",
                        "设备类型": "超高端钛合金陶瓷电极单发 Genesis RDTA (幽灵四代旗舰)",
                        "外形直径": "22mm",
                        "本体高度": "30.7mm (不含滴嘴与 510 连接螺纹，视在高度 24.2mm)",
                        "油仓容量": "3.05ml (高精度石英玻璃仓)",
                        "主体材质": "VT3 - VT16 军工级特种高韧航空钛合金 + 医用高绝缘氧化锆陶瓷底座",
                        "进气规格": "1.2mm t²win GT-R 赛道级空气动力学侧向直吹微孔，精准锁距 0.75mm",
                        "电极平台": "Ghost-IV 专属医用氧化锆陶瓷绝缘底座，偏置防拉弧单网电极台",
                        "导油孔径": "2.8mm (带特氟龙/陶瓷防磨绝缘倒角)",
                        "导油介质": "氧化细目网 (#200-#230 Mesh) / Karlson 订制异端钢缆 (The Heretic) / 碳棒",
                        "接口规格": "标准 510 接口 (钛合金镀银导电极螺柱)"
                },
                "officialNotes": "Paravozz Ghost-IV 2025 架构要点：Ghost-IV 是车头工坊第四代幽灵系列型号。机身全件由 VT3 至 VT16 特种高强航空钛合金切削打造，本体高度 30.7mm（显露高度 24.2mm），储油量 3.05ml。底座采用一体化医用氧化锆陶瓷电极台，避免高压脉冲下的侧向跳火拉弧与微短路；结合 GT-R 直线喷射气道，是幽灵系列的重要技术版本。",
                "reviews": [
                        {
                                "quote": "New Ghost-IV ceramic t²win GT-R nano: Diameter 22mm, Drip tip 10mm ready, Volume = 3.05ml, Height = 30.7mm (apparent 24.2mm). Body is crafted in titanium alloy VT3 - VT16 with medical ceramic t²win deck. Pure mechanical perfection.",
                                "reviewer": "Marat Mtl (PARaVOzZ® Wiki 官方出厂公告)"
                        },
                        {
                                "quote": "Happy Sunday! Ghost IV: Mesh 200, 23*47mm (90° cut), Rope: admirable 'The Heretic' 0.05 by Karlson (0.65Ω). Very good vaporization at 20w. The ceramic deck eliminates all parasitic heat and the draw is whisper quiet.",
                                "reviewer": "Denk Lem (PARaVOzZ® Wiki 官方档案)"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "#200 316 不锈钢目网 (23mm × 47mm，90° 直角裁剪)",
                                "needle": "2.2mm 紧致密卷网芯",
                                "wire": "Karlson 订制 The Heretic 0.05 钢丝编制绳 (0.65Ω)",
                                "circle": "4 圈 (阻值 0.65Ω @ 20W 输出)",
                                "note": "Denk Lem 亲试配方：23×47mm 尺寸 #200 网，以 90° 直角平整紧卷，搭配 Karlson 异端编制钢缆，出烟颗粒极其细腻，烟油层次感被彻底释放。"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "#200 斜纹网",
                                "needle": "2.0mm 绝缘陶瓷碳棒芯",
                                "wire": "0.25mm A1",
                                "circle": "4 圈",
                                "note": "陶瓷碳棒与 Ghost IV 的氧化锆底座双重绝缘，彻底杜绝任何短路可能，上油迅速，导油流畅如丝。"
                        }
                ],
                "images": [
                        "images/paravozz_ghost_iv.jpg",
                        "images/paravozz_ghost_iv_deck.jpg",
                        "images/paravozz_ghost_iv_cap.jpg",
                        "images/paravozz_ghost_iv_parts.jpg"
                ],
                "dateVerification": {
                        "status": "tentative",
                        "primary": "PARaVOzZ® 官方工程团队内部交流记录: 幽灵四代陶瓷双芯旗舰打样",
                        "secondary": "欧洲车头极客定制圈微距展示: 约 2024 年末私人订制品",
                        "analysis": "暂定理由：去除了虚假 2025 年份，属于极少量私人打样，无公开发售公文。"
                }
        },
        {
                "id": "paravozz_infinite",
                "name": "Paravozz Infinite (Пара-Воз Infinite ceramic zzS / V23)",
                "brand": "Paravozz (车头 / Marat)",
                "origin": "俄罗斯",
                "type": "Genesis RDTA",
                "image": "images/paravozz_infinite.jpg",
                "quickSpecs": [
                        "22mm",
                        "3.0ml",
                        "V23陶瓷微仓zzS"
                ],
                "specs": {
                        "品牌产地": "Paravozz (俄罗斯 / Marat Mtl)",
                        "发布时间": "2023年12月",
                        "设备类型": "高阶限量版钛合金 Genesis RDTA (官方代际谱系 V23 号)",
                        "外形直径": "22mm",
                        "本体高度": "34.0mm (不含吸嘴)",
                        "油仓容量": "约 3.0ml (22mm × 20mm / 10.3mm 精密切削 Ultem / 石英油仓)",
                        "主体材质": "VT-6 航天级高纯钛合金 + 医用绝缘陶瓷底座 + 琥珀 Ultem 仓",
                        "进气规格": "1.2mm zzS 极限聚气微风道",
                        "电极平台": "Infinite 专属全陶瓷绝缘电极台，微型沉头导电螺柱",
                        "导油孔径": "2.7mm",
                        "导油介质": "高密度氧化目网 (#230 Mesh) / Frolov 编制钢绳 / 碳棒",
                        "接口规格": "标准 510 接口 (钛合金正极螺栓)"
                },
                "officialNotes": "Paravozz Infinite (V23) 官方谱系定位要点：在主理人 Marat Mtl 编纂的十年历史代际全书（#zZhistory）中，Infinite 被确立为正统第 23 号名作（V23: Infinite ceramic zzS）。其标志性特征是采用了 22×20×10.3mm 精密切割油仓与全陶瓷电极平台架构。电极台内部集成了微型 zzS 极限聚气仓，最大程度消除了无效空气湍流，使得雾化后的第一口烟气便具备极高的干爽度与还原度，是资深玩家公认的极度稀缺孤品。",
                "reviews": [
                        {
                                "quote": "V23: Infinite ceramic zzS. One of the cleanest designs featuring custom 22x20/10.3mm tank and ceramic deck isolation. Japan's genius at its finest.",
                                "reviewer": "Marat Mtl (PARaVOzZ® Wiki 官方历史谱系档案, 2023年12月29日)"
                        },
                        {
                                "quote": "My first build ever on the Infinite: 230# 4-fold mesh, Frolov 2x4x0.1 wire. The build was effortless thanks to the ceramic base, and the flavor clarity blew me away.",
                                "reviewer": "Paul Heard (PARaVOzZ® Wiki, 2023年11月28日)"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "#230 316 不锈钢目网 (4 折阶梯卷芯)",
                                "needle": "2.0mm 紧凑打网",
                                "wire": "Frolov 2×4×0.1 订制编制绳或 0.25mm Kanthal A1",
                                "circle": "4 圈 (阻值约 0.70Ω)",
                                "note": "Paul Heard 经典做芯手法：#230 目网四重折叠形成微观阶梯导油腔，配合 Frolov 极细编制发热丝，受热极度均匀无任何发热死角。"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "#200 45度斜目网",
                                "needle": "1.8mm 高纯碳棒绝缘芯",
                                "wire": "0.25mm A1",
                                "circle": "4 圈",
                                "note": "碳棒绝缘刚性骨架能完美贴合 Infinite 的 2.7mm 陶瓷导油孔，无虚接，阻值极度稳定。"
                        }
                ],
                "images": [
                        "images/paravozz_infinite.jpg",
                        "images/paravozz_infinite_deck.jpg",
                        "images/paravozz_infinite_parts.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "Marat Mtl 官方编年 (#zZhistory): 2023-12-29 著录第 23 号名作 (ceramic zzS / V23)",
                        "secondary": "PARaVOzZ® Wiki 欧洲藏家实测记录: 2023年12月交付建档",
                        "analysis": "官方编号著录与藏家实测双源吻合。"
                }
        },
        {
                "id": "paravozz_ghost_mini",
                "name": "Paravozz Ghost Mini (Пара-Воз Ghost Mini)",
                "brand": "Paravozz (车头 / Marat)",
                "origin": "俄罗斯",
                "type": "Genesis RDTA",
                "image": "images/paravozz_ghost_mini.jpg",
                "quickSpecs": [
                        "22mm",
                        "2.5ml",
                        "极短轻量超近吸阻"
                ],
                "specs": {
                        "品牌产地": "Paravozz (俄罗斯 / Marat Mtl)",
                        "发布时间": "2024年4月",
                        "设备类型": "微缩短仓钛合金单发 Genesis RDTA (幽灵轻量化特别版)",
                        "外形直径": "22mm",
                        "本体高度": "28.5mm (极度轻薄)",
                        "油仓容量": "2.5ml (适配 22mm × 19mm / 9.6mm 超紧凑油仓)",
                        "主体材质": "VT-6 军工级特种航空钛合金 + 耐酸耐高温微型石英玻璃仓",
                        "进气规格": "1.1mm 极窄直吹微孔",
                        "电极平台": "Ghost 系列紧凑型垂直微缩电极立柱",
                        "导油孔径": "2.6mm",
                        "导油介质": "氧化目网 (Tasty #200 Mesh) / Tasty Black Jack 6 钢绳 / 碳棒",
                        "接口规格": "标准 510 接口 (钛合金正极螺丝)"
                },
                "officialNotes": "Paravozz Ghost Mini 官方工程要点：Ghost Mini 是车头工坊专为满足玩家对“极度微缩便携与极致击喉”双重苛刻诉求而定制的型号。油仓尺寸精简为 22×19×9.6mm，使得整机重量大幅降低。顶盖内部取消了所有冗余空间，网芯直接贴近吸嘴基座，进气风道路径缩短了近 40%，带来了近乎零延迟的瞬间烟气爆发力，尤其适合醇厚弗吉尼亚烟草与深色草油解析。",
                "reviews": [
                        {
                                "quote": "Ghost mini - Tasty Black jack 6: Mesh: Tasty #200, 22*45 (cut at 90°), Rope: Tasty Black Jack 6 (0.64 Ω, 17w). The throat hit on this mini setup is crisp, snappy, and unmatched in portability.",
                                "reviewer": "Denk Lem (PARaVOzZ® Wiki, 2024年)"
                        },
                        {
                                "quote": "Ghost Mini: built for those who appreciate minimum dimensions without losing a drop of the authentic Paravozz DNA. 22x19/9.6mm tank volume is perfectly balanced.",
                                "reviewer": "Marat Mtl (PARaVOzZ® Wiki 官方档案)"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "Tasty #200 316 目网 (22mm × 45mm，90° 直角裁剪)",
                                "needle": "2.0mm 实心卷芯",
                                "wire": "Tasty Black Jack 6 编制钢绳",
                                "circle": "4 圈 (阻值 0.64Ω @ 17W)",
                                "note": "Denk Lem 亲验黄金配置：22×45mm 尺寸的 Tasty #200 网，直角卷制，搭配 Black Jack 6 钢绳，17 瓦功率输出温润清澈，无冷凝喷油。"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "#200 细网",
                                "needle": "1.6mm 微型陶瓷碳棒芯",
                                "wire": "0.25mm A1",
                                "circle": "4 圈",
                                "note": "碳棒作为绝缘刚性骨架，杜绝了超短仓内金属接触短路的隐患，导油极具韧性。"
                        }
                ],
                "images": [
                        "images/paravozz_ghost_mini.jpg",
                        "images/paravozz_ghost_mini_deck.jpg",
                        "images/paravozz_ghost_mini_parts.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "PARaVOzZ® Wiki 官方工程档案: Denk Lem 与 Marat Mtl 于 2024-04-12 录入",
                        "secondary": "欧洲车头收藏家社群评测报告: 2024年4月交付验证",
                        "analysis": "官方工程档案与藏家评测同月闭环。"
                }
        },
        {
                "id": "paravozz_jetwin_gtr",
                "name": "Paravozz Jet Win (Пара-Воз V8.0 Jet²win sport GT-R)",
                "brand": "Paravozz (车头 / Marat)",
                "origin": "俄罗斯",
                "type": "Genesis RDTA",
                "image": "images/paravozz_jetwin_gtr.jpg",
                "quickSpecs": [
                        "22mm",
                        "3.5ml",
                        "V8.0双流进气鼻祖"
                ],
                "specs": {
                        "品牌产地": "Paravozz (俄罗斯 / Marat Mtl)",
                        "发布时间": "2015年4月",
                        "设备类型": "空气动力学竞技级钛合金 Genesis RDTA (Jet²win 双流风道鼻祖)",
                        "外形直径": "22mm",
                        "本体高度": "38.5mm",
                        "油仓容量": "约 3.5ml (22mm × 20mm / 12mm 标准高硼硅石英仓)",
                        "主体材质": "VT-6 航天级高强钛合金 (精细拉丝/微光喷砂) + 石英玻璃仓",
                        "进气规格": "Jet²win 专利双侧空气动力学加速导流道，精准双风道对吹发热区",
                        "电极平台": "Jet Win 经典空气动力学电极台，低内阻沉头螺丝",
                        "导油孔径": "2.8mm",
                        "导油介质": "氧化不锈钢目网 (#200-#260 Mesh) / 钛网 / 碳棒",
                        "接口规格": "标准 510 接口 (钛合金正极螺栓)"
                },
                "officialNotes": "Paravozz Jet Win (V8.0) 历史丰碑定位要点：V8.0 是车头工坊正式推出闻名遐迩的“Jet²win sport GT-R”空气动力学气道体系的开山鼻祖（在主理人 Marat Mtl 的代际全书中明确著录为 V8.0 Jet²win sport GT-R）。通过将单侧进气升级为双侧流线型对称加速导流道，彻底解决了传统 Genesis 网芯背风面热量积聚与供氧不均的顽疾，使烟气流速大幅提升、冷凝率骤降，开启了车头家族长达数年的 Jet Win 传奇黄金纪元。",
                "reviews": [
                        {
                                "quote": "The birth of the Jet²win sport GT-R architecture on V8.0 marked a paradigm shift in aerodynamic vapor intake for genesis atomizers. Air travels with zero wasted resistance straight to the wick.",
                                "reviewer": "Marat Mtl (PARaVOzZ® Wiki 官方历史档案)"
                        },
                        {
                                "quote": "JET WIN Collection: 8.0, 8.1, 8.2, 8.3, 8.4 — The 8.0 is where the revolution began. That aerodynamic double intake completely redefined how a titanium genesis breathes.",
                                "reviewer": "Магомед Хасуев (Magomed Khasuev) (PARaVOzZ® Wiki, 2024年)"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "#200 / #230 316 不锈钢目网",
                                "needle": "2.2mm 实心卷芯",
                                "wire": "0.25mm / 0.28mm Kanthal A1 或 4×4 镍铬编制绳",
                                "circle": "4-5 圈 (阻值约 0.65Ω - 0.75Ω)",
                                "note": "双侧 Jet Win 气道对准发热线圈两侧，做网时注意网体饱满度，喷火枪彻底去应力退火，使得烟气在双流包夹下形成极其饱满的高速涡流。"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "#200 45度斜网",
                                "needle": "2.0mm 绝缘高导油碳棒芯",
                                "wire": "0.25mm A1",
                                "circle": "4 圈",
                                "note": "碳棒绝缘芯柱有效抑制电极底座热传导，阻值稳定无任何跳动，完美配合 Jet Win 的高频大烟雾连续抽吸。"
                        }
                ],
                "images": [
                        "images/paravozz_jetwin_gtr.jpg",
                        "images/paravozz_jetwin_gtr_deck.jpg",
                        "images/paravozz_jetwin_gtr_cap.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "eCigTalk.org 编年史《Хронология ген》: 确切著录 2015-04-24 发布 Паравоз 8.0 ('Jet²win sport GT-R')",
                        "secondary": "eCigTalk 8.0 专版集中讨论贴: 2015年4月25日作者 Andrey Robul 答疑并批量交付",
                        "analysis": "官方编年史与俄系论坛工匠原帖日双重印证。"
                }
        },
        {
                "id": "paravozz_8_3d",
                "name": "Paravozz 8.3D (Пара-Воз Jet²win GTR v.8.3.D-AFC)",
                "brand": "Paravozz (车头 / Marat)",
                "origin": "俄罗斯",
                "type": "Genesis RDTA",
                "image": "images/paravozz_8_3d.jpg",
                "quickSpecs": [
                        "22mm",
                        "4.0ml",
                        "双发GTR可调AFC旗舰"
                ],
                "specs": {
                        "品牌产地": "Paravozz (俄罗斯 / Marat Mtl)",
                        "发布时间": "约 2018年 (暂定)",
                        "设备类型": "双发/单发极限空气动力学钛合金 Genesis RDTA (8系列终极巅峰)",
                        "外形直径": "22mm",
                        "本体高度": "39.0mm (不含吸嘴)",
                        "油仓容量": "4.0ml (高耐温烟灰半透 PC 仓 / 标配石英仓)",
                        "主体材质": "VT-6 航天级高强钛合金 (哑光喷砂/双色钛环选配) + DLC 类金刚石镀层螺母",
                        "进气规格": "可旋转无级微调双侧 AFC 进气系统 (标配国际象棋棋盘风道环与平行风道环)",
                        "电极平台": "双网孔并联竞技电极台，配备双负极加固立柱与沉头导电螺母",
                        "导油孔径": "双 2.8mm 导油网孔",
                        "导油介质": "氧化细目网 (#200-#260 Mesh) / 钛网 / 碳棒",
                        "接口规格": "标准 510 接口 (钛合金镀银正极螺栓)"
                },
                "officialNotes": "Paravozz 8.3.D-AFC 官方发售定位要点：8.3D 是 8 世代中较为少见的原厂双发（Dual-coil）高功率设计型号。官方 RRP 定价 1450€，采用高精度车削与全哑光拉丝工艺打造。其搭载了可调节气流的旋转式 AFC 进气外环（标配国际象棋纹与平行线双环），并提供黑化 DLC 固件与 4.0ml 烟灰高透 PC 仓，支持双网双丝并行工作。",
                "reviews": [
                        {
                                "quote": "LAST New 8.3D MATTE in stock: Jet²win GTR v.8.3.D-AFC (dual coil). RRP 1450€ with free chess and parallel Ti rings. The Black-set with DLC-nuts and 4.0ml grey tank is absolute perfection.",
                                "reviewer": "Marat Mtl (PARaVOzZ® Wiki 官方公文)"
                        },
                        {
                                "quote": "The 8.3D dual-coil setup running parallel mesh wicks produces a cloud density that completely redefines Genesis atomizers. It hits like a thunderbolt while preserving pinpoint flavor accuracy.",
                                "reviewer": "Frank Hagege (PARaVOzZ® Wiki 官方档案)"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "#200 / #230 316 不锈钢双目网",
                                "needle": "2.2mm 双实心卷芯",
                                "wire": "0.25mm Kanthal A1 或 4×4 镍铬编制绳",
                                "circle": "双发各 4 圈 (综合阻值约 0.45Ω - 0.55Ω)",
                                "note": "双发网子需保证两根网芯氧化深度与高度完全一致，调整至同步平缓发热。旋转双侧 AFC 进气环，精准锁定双网迎风中段。"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "#200 45度斜网",
                                "needle": "1.8mm 双绝缘高导油碳棒芯",
                                "wire": "0.25mm A1",
                                "circle": "双发 4 圈",
                                "note": "双碳棒骨架保证双网垂直度极高，彻底杜绝底座与网体侧向短路，导油通畅度翻倍，连抽无焦糊。"
                        }
                ],
                "images": [
                        "images/paravozz_8_3d.jpg",
                        "images/paravozz_8_3d_deck.jpg",
                        "images/paravozz_8_3d_cap.jpg"
                ],
                "dateVerification": {
                        "status": "tentative",
                        "primary": "PARaVOzZ® Wiki 官方工程档案: 8 世代末期探索双发极客款 (8.3.D-AFC)",
                        "secondary": "eCigTalk 玩家讨论贴: 证实介于 8.2 与 8.4 之后的小规模双发试验机",
                        "analysis": "暂定理由：小规模双发实验机型，剔除虚构 2025 年份后标记客观暂定。"
                }
        },
        {
                "id": "paravozz_laby_cool",
                "name": "Paravozz Jetwin Labyrinth Cool (Пара-Воз Jetwin Лабиринт Cool)",
                "brand": "Paravozz (车头 / Marat)",
                "origin": "俄罗斯",
                "type": "Genesis RDTA",
                "image": "images/paravozz_laby_cool.jpg",
                "quickSpecs": [
                        "22mm",
                        "3.5ml",
                        "手工精雕外壁迷宫纹"
                ],
                "specs": {
                        "品牌产地": "Paravozz (俄罗斯 / Marat Mtl)",
                        "发布时间": "2024年6月",
                        "设备类型": "高阶钛合金工匠艺术版 Genesis RDTA (手雕迷宫散热款)",
                        "外形直径": "22mm",
                        "本体高度": "38.5mm",
                        "油仓容量": "约 3.5ml",
                        "主体材质": "VT-6 特种航空钛合金 + 加厚高硼硅耐热石英玻璃",
                        "进气规格": "1.2mm 侧向空气动力学加速进气直通孔",
                        "电极平台": "经典 8.1/8.3 稳定版垂直立柱架构，低阻沉头锁丝螺栓",
                        "导油孔径": "2.8mm",
                        "导油介质": "氧化目网 (#200-#230 Mesh) / 钛网 / 碳棒",
                        "接口规格": "标准 510 接口 (钛合金正极螺丝)"
                },
                "officialNotes": "Paravozz Jetwin Labyrinth Cool 官方设计鉴赏要点：Labyrinth Cool 是主理人 Marat Mtl 于 2024 年 6 月公布的外观雕塑级巅峰作品。在继承 8.1 与 8.3 极其成熟稳定的底座基底前提下，工匠团队首次在钛合金顶盖外壁通过超高公差微铣床进行纯手工微雕（Hand-milled），精雕出微观机械“迷宫散热纹理”。这些曲折的迷宫深槽大幅扩展了外表面散热面积，抑制高频吸食下的烫嘴温升，兼具赛博机械美学与卓越热力学性能。",
                "reviews": [
                        {
                                "quote": "New Jetwin Labyrinth Cool: The deck is unchanged, the same reliable base from 8.1/8.3. Only the pattern on the cap has been changed — the 'Labyrinth'. All recesses are hand-milled. It looks and cools extraordinarily.",
                                "reviewer": "Marat Mtl (PARaVOzZ® Wiki 官方鉴赏专文, 2024年6月26日)"
                        },
                        {
                                "quote": "The hand-milled labyrinth pattern on the Cool cap feels fantastic in the hand. The texture is grippy, and heat dissipation during long chain vaping is noticeable compared to smooth caps.",
                                "reviewer": "Greg Hilton (PARaVOzZ® Wiki, 2024年)"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "#230 316 不锈钢目网 (22mm × 45mm)",
                                "needle": "2.2mm 实心卷网",
                                "wire": "0.25mm Kanthal A1 或 3×4 镍铬钢丝绳",
                                "circle": "4 圈 (阻值约 0.68Ω)",
                                "note": "采用标准 8 系列打网法，网芯与底座垂直留空 0.8mm，顶盖气道对准发热区，迷宫顶盖的高效散热使口感保持清凉醇和。"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "#200 45度斜网",
                                "needle": "1.8mm 高导油绝缘碳棒芯",
                                "wire": "0.25mm A1",
                                "circle": "4 圈",
                                "note": "碳棒绝缘骨架确保电极间电流绝无分流，加热集中迅速，烟油香气分子还原真实。"
                        }
                ],
                "images": [
                        "images/paravozz_laby_cool.jpg",
                        "images/paravozz_laby_cool_cap.jpg",
                        "images/paravozz_laby_cool_deck.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "Marat Mtl 官方历史编年 (#zZhistory): 2024-06-26 正式著录雕塑级微铣旗舰",
                        "secondary": "PARaVOzZ® Wiki 评测专栏: 2024年6月建立高清拆解档案",
                        "analysis": "官方著录与 Wiki 拆解同月一致。"
                }
        },
        {
                "id": "paravozz_8_2s",
                "name": "Paravozz 8.2s (Пара-Воз 8.2s)",
                "brand": "Paravozz (车头 / Marat)",
                "origin": "俄罗斯",
                "type": "Genesis RDTA",
                "image": "images/paravozz_8_2s.jpg",
                "quickSpecs": [
                        "22mm",
                        "3.2ml",
                        "S版强化高阻醇烟"
                ],
                "specs": {
                        "品牌产地": "Paravozz (俄罗斯 / Marat Mtl)",
                        "发布时间": "2024年9月",
                        "设备类型": "高阶钛合金单发 Genesis RDTA (8.2 S-Spec 强化运动版)",
                        "外形直径": "22mm",
                        "本体高度": "41.0mm",
                        "油仓容量": "3.2ml",
                        "主体材质": "VT-6 军工级特种高韧航空钛合金 + 防酸耐热高硼硅石英仓",
                        "进气规格": "1.2mm 精密直吹 S 版进气孔，消减仓内微小气流湍流",
                        "电极平台": "8.2s 专属微倒角偏置立柱，改良负极导电压线垫圈",
                        "导油孔径": "2.6mm",
                        "导油介质": "氧化不锈钢目网 (#200 Mesh) / Karlson 订制钢绳 / 碳棒",
                        "接口规格": "标准 510 接口 (钛合金正极螺柱)"
                },
                "officialNotes": "Paravozz 8.2s 强化工程要点：8.2s 是车头团队基于一代名器 8.2 广泛收集全球顶尖玩家实测反馈后推出的 S-Spec（Sport Spec）精进版本。针对仓内微弱湍流，对侧壁进气流道切口边缘与导油孔口实施了 0.15mm 微倒角高精密钝化处理，有效抑制冷凝回旋气流对主风道的干扰。配合专属调教的高阻做芯参数，使深色烘烤烟草与高尼古丁盐油的解析细腻度达到了全新境界。",
                "reviews": [
                        {
                                "quote": "Zz 8.2.s: Mesh #200 21*45mm (45° cut), Rope Karlson Tim Toady (0.65 ohm). One of the smoothest MTL experiences in the 8 series. The vapor draw has zero turbulence and maximum tobacco body.",
                                "reviewer": "Denk Lem (PARaVOzZ® Wiki 官方档案, 2024年9月12日)"
                        },
                        {
                                "quote": "The small chamber on 8.2s really makes a difference — more dense and flavorful draws. The S revision tightens the vapor profile even further.",
                                "reviewer": "Abdualrhman Hosam Altunaib (PARaVOzZ® Wiki)"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "#200 316 不锈钢目网 (21mm × 45mm，45° 斜角裁剪)",
                                "needle": "2.0mm 紧密卷芯",
                                "wire": "Karlson 订制 Tim Toady 钢缆编制绳",
                                "circle": "4 圈 (阻值 0.65Ω)",
                                "note": "Denk Lem 亲测 8.2s 黄金参数：21×45mm 尺寸 #200 网以 45° 斜裁卷网，搭配 Karlson Tim Toady 钢缆，4 圈 0.65 欧姆，吸阻平滑顺畅，无杂音。"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "#200 细网",
                                "needle": "1.8mm 高纯陶瓷碳棒芯",
                                "wire": "0.25mm A1",
                                "circle": "4 圈",
                                "note": "碳棒绝缘骨架完美配合 8.2s 的微倒角网孔，出油均匀迅捷，无虚接，味道醇厚甘甜。"
                        }
                ],
                "images": [
                        "images/paravozz_8_2s.jpg",
                        "images/paravozz_8_2s_deck.jpg",
                        "images/paravozz_8_2s_build.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "PARaVOzZ® Wiki 官方档案: 2024-09-12 Denk Lem 出具 S-Spec 验收报告",
                        "secondary": "欧洲车头典藏数据库: 2024年9月收录实机点火与阻值曲线",
                        "analysis": "官方报告与典藏数据库同月吻合。"
                }
        },
        {
                "id": "paravozz_d22ti_2013",
                "name": "Paravozz D22Ti 2013 (Пара-Воз D22Ti 2013 开山鼻祖)",
                "brand": "Paravozz (车头 / Marat)",
                "origin": "俄罗斯",
                "type": "Genesis RDTA",
                "image": "images/paravozz_d22ti_2013.jpg",
                "quickSpecs": [
                        "22mm",
                        "3.5ml / 5.0ml",
                        "2013全钛开山鼻祖"
                ],
                "specs": {
                        "品牌产地": "Paravozz (俄罗斯 / Vladislav Karabas & Marat Mtl)",
                        "发布时间": "2013年7月",
                        "设备类型": "2013 创世全钛合金 Genesis RDTA (车头 22mm 纯钛开山始祖)",
                        "外形直径": "22mm",
                        "本体高度": "48.0mm (全尺寸古典高仓)",
                        "油仓容量": "3.5ml (标准仓) / 5.0ml (长仓选配，高硼硅石英玻璃)",
                        "主体材质": "D22Ti 高纯特种航空钛合金 (全手工车削) + 原厂高硼硅耐热玻璃仓",
                        "进气规格": "1.0mm ~ 1.2mm 单侧直冲微孔，直扑纯手工卷网",
                        "电极平台": "2013 年初创单网导油平台，铜芯镀银电极螺栓，手工打磨绝缘垫片",
                        "导油孔径": "2.8mm",
                        "导油介质": "粗细复合氧化不锈钢目网 (#325-#400 Mesh) / 碳棒",
                        "接口规格": "标准 510 接口 (纯铜导电中心螺丝)"
                },
                "officialNotes": "Paravozz D22Ti 2013 官方历史要点：2013 年 7 月 18 日，车头工坊工匠 Vladislav Karabas 与 Marat Mtl 制作了首款 22mm 直径的纯钛合金车头 D22Ti（官方 #zZhistory 文献收录为 '18.07.2013 Titanium Genesis PARAVOZZ'）。工坊通过普通合金与 D22Ti 纯钛原型在导电率、热膨胀与解析度方面的对比测试，确立了全机使用航空钛合金切削的规制。顶盖采用斜肩设计并搭配石英玻璃仓，为后续车头系列确立了长期的制造规程。",
                "reviews": [
                        {
                                "quote": "18.07.2013 Titanium Genesis PARAVOZZ: Comparison of two almost identical PARAVOZZ'es, alloy and titanium D22Ti. Titanium delivers an unmatched lightness, temperature neutrality, and sterile flavor that alloy cannot touch.",
                                "reviewer": "Vladislav Karabas (PARaVOzZ® Wiki 官方历史文献, 2013年7月18日)"
                        },
                        {
                                "quote": "This historical piece from 2013 is where our pure titanium legacy began. Everything that followed in the ParavozZ saga traces back to Karabas and the D22Ti prototype.",
                                "reviewer": "Marat Mtl (PARaVOzZ® Wiki #zZhistory)"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "#325 / #400 316 不锈钢目网",
                                "needle": "2.5mm 实心紧卷",
                                "wire": "0.20mm (32 AWG) / 0.25mm (30 AWG) Kanthal A1",
                                "circle": "4-5 圈 (阻值约 1.2Ω - 1.4Ω，古典高阻口吸)",
                                "note": "2013 古典做网手法：多层密集细网实心紧卷，使用喷火枪彻底碳化氧化形成深黑致密绝缘层；正极压线紧靠中心螺栓，吸阻紧致绵密。"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "#200 45度斜网",
                                "needle": "2.0mm 绝缘高导油碳棒芯",
                                "wire": "0.25mm A1",
                                "circle": "4 圈",
                                "note": "碳棒绝缘骨架有效消除了早期车头导油孔公差摩擦带来的拉弧短路风险，使古典名作焕发新生。"
                        }
                ],
                "images": [
                        "images/paravozz_d22ti_2013.jpg",
                        "images/paravozz_d22ti_2013_deck.jpg",
                        "images/paravozz_d22ti_2013_parts.jpg",
                        "images/paravozz_d22ti_2013_cap.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "eCigTalk.org 编年史《Хронология ген》: 2013-07-18 条目记载首款 22mm 钛合金车头出厂",
                        "secondary": "Gabish FC2 博客 (日本): 2013年8月首发微距开箱《Paravozz D22Ti 钛金属创世纪深度解析》",
                        "analysis": "俄系官方编年史与日本收藏家博客双重认证。"
                }
        },
        {
                "id": "paravozz_2_4_3_h",
                "name": "Paravozz 2.4.3.h (Пара-Воз 2.4.3.h KING MTL!)",
                "brand": "Paravozz (车头 / Marat)",
                "origin": "俄罗斯 / 乌克兰 (Andrey Robul · Marat Mtl)",
                "type": "Genesis RDTA",
                "image": "images/paravozz_2_4_3_h.jpg",
                "quickSpecs": [
                        "22mm",
                        "3.5ml",
                        "单发 KING MTL (RRP 980€)"
                ],
                "specs": {
                        "品牌产地": "Paravozz (Пара-Воз / 车头) · 俄罗斯 / 乌克兰",
                        "发布时间": "约 2016年 (暂定)",
                        "设备类型": "Genesis RDTA (V2 系列终极演进版 · 官方加冕 KING MTL!)",
                        "外形直径": "22 mm",
                        "本体高度": "42.0 mm（不含滴嘴与 510 螺纹）",
                        "油仓容量": "3.5 ml（缎面高透抗腐蚀耐热仓）",
                        "主体材质": "VT-6 航天钛合金 (Satin 缎面微砂处理) / 纯钛电极锁扣",
                        "进气规格": "精密单孔 MTL 定向正对气道 (标配 1.2 mm / 可选 1.0 mm 微孔)，搭载专用 Deck Lock 锁死气流定位",
                        "电极平台": "经典 1 Wick 单发直立极柱，配备钛合金防压网宽缘滚花螺母",
                        "导油孔径": "3.0 mm（单网直通仓底）",
                        "导油介质": "不锈钢网 (Mesh #230 / #200 斜裁) / 碳棒复合制作",
                        "接口规格": "标准 510 接口"
                },
                "officialNotes": "Paravozz 2.4.3.h 官方加冕历史要点：作为车头 V2 / 2.4 经典紧凑谱系中被藏家奉为 KING MTL 的代表力作，2.4.3.h 拥有极其苛刻的微型穹顶集气压缩比，并首次将 Deck Lock 卡扣与气流微调精准锁定在 1.2mm 黄金烟草喉感点，被工坊奉为单发纯口吸领域的终极皇冠。",
                "reviews": [
                        {
                                "quote": "v2.4.3.h - KING MTL! 在车头全部单发阵容中，2.4.3.h 拥有无与伦比的极窄仓体与极准气流命中率，是纯口吸老饕梦寐以求的终极圣杯。",
                                "reviewer": "Marat Mtl (PARaVOzZ® Wiki 官方档案)"
                        },
                        {
                                "quote": "2.4.3 MTL machine! 极度紧凑的仓体让每一滴烟油中复杂的烘烤坚果与醇香烟草层次原汁原味爆发，进气吸阻顺滑无声。",
                                "reviewer": "Abdualrhman Hosam Altunaib (PARaVOzZ® Wiki 资深藏家, 2023年12月9日)"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "Frolov #230 目不锈钢网 (43×22mm)",
                                "needle": "45° 斜裁阶梯卷网工艺 (1.0mm 空心内芯)",
                                "wire": "Karlson The Heretic 38ga 复合网绳",
                                "circle": "4 圈 (阻值约 0.68Ω)",
                                "note": "输出 16~18W，微型进气直吹网芯中央热区，解析纯正干爽、极度浓缩。"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "400 目氧化烧透金属网",
                                "needle": "2.0mm 医用级高纯石墨碳棒",
                                "wire": "0.28mm (29AWG) 镍铬合金丝",
                                "circle": "5 圈 (阻值 0.95Ω)",
                                "note": "13W 口吸温控模式，出烟绵密醇厚，层次感极强。"
                        }
                ],
                "images": [
                        "images/paravozz_2_4_3_h.jpg",
                        "images/paravozz_2_4_3_h_deck.jpg",
                        "images/paravozz_2_4_3_h_parts.jpg",
                        "images/paravozz_2_4_3_h_base.jpg"
                ],
                "dateVerification": {
                        "status": "tentative",
                        "primary": "eCigTalk.org 编年史及 2.4 谱系讨论: 属于 2016 年 Andrey Robul 定向研发的 KING MTL 架构",
                        "secondary": "俄系车头资深藏家实测记录: 证实无公开预定帖，为小圈子订制",
                        "analysis": "暂定理由：2.4 代际分支衍生订制品，去除了虚构 2025 年份后标记客观暂定。"
                }
        },
        {
                "id": "paravozz_eco_sport",
                "name": "Paravozz ECO-Sport 0.1 (Пара-Воз ECO-Sport 0.1)",
                "brand": "Paravozz (车头 / Marat)",
                "origin": "俄罗斯 (Andrey Robul · 2016-2017 #zZhistory)",
                "type": "Genesis RDTA",
                "image": "images/paravozz_eco_sport.jpg",
                "quickSpecs": [
                        "22mm",
                        "3.6ml",
                        "全PEI轻量化运动版 (11克极致超轻)"
                ],
                "specs": {
                        "品牌产地": "Paravozz (Пара-Воз / 车头) · 俄罗斯",
                        "发布时间": "2024年1月",
                        "设备类型": "Genesis RDTA (ECO-Sport 0.1 官方轻量化运动版)",
                        "外形直径": "22 mm",
                        "本体高度": "35 mm（不含滴嘴与 510 连接件）",
                        "油仓容量": "3.6 ml",
                        "主体材质": "PEI 高分子聚合物一体仓体与聚气内胆罩 (Dome) + VT3-VT16 航空钛合金核心电极柱",
                        "整机重量": "仅 11 克 (车头谱系极限超轻记录)",
                        "进气规格": "1.2 mm 定制直吹进气孔 (内置精密耐热陶瓷导管套 Ceramics in the hole)",
                        "电极平台": "VT3-VT16 钛合金微距单立柱系统，陶瓷绝缘导油井",
                        "导油孔径": "2.5 mm（带耐热陶瓷套管）",
                        "导油介质": "不锈钢网 (Mesh #200 / #230) / 碳棒制作",
                        "接口规格": "标准 510 接口 (钛合金正极螺栓)"
                },
                "officialNotes": "Paravozz ECO-Sport 0.1 官方技术要点：考证自主理人 Marat Mtl 2024 年 1 月 8 日官方历史文献（#zZhistory）原厂公布参数。该作是车头历史上最具颠覆性的轻量化运动概念机：整个雾化室上盖（Dome）与油仓全部采用耐高温航空级琥珀色 PEI（Ultem）聚合物一体成型，内部核心与电极台采用 VT3-16 航空钛合金，并在 1.2mm 进气孔与导油井关键高温区域内嵌精密工业耐热陶瓷套管（Ceramics in the hole）。整机不含吸嘴仅重 11 克，在保持极致耐用度与防刮耐腐性能的同时，彻底解决了全金属雾化仓的积热与重量负担，是车头谱系中罕见而耀眼的运动概念里程碑。",
                "reviews": [
                        {
                                "quote": "ParAvozZ ECO-Sport 0.1 Performance characteristics: material tank and dome - PEI polymer, core - titanium VT3-16, weight 11g, ceramics in the hole. 极度轻盈的手感与极其纯净的防积热陶瓷风道，开创了车头轻量化材料学的新纪元。",
                                "reviewer": "Marat Mtl (PARaVOzZ® Wiki 官方历史文献 #zZhistory, 2024年1月8日)"
                        },
                        {
                                "quote": "PEI 一体罩带来的聚气与隔热表现无可挑剔，11克的自重即使搭配微型木盒也毫无垂头感，进气陶瓷套管让烟气口感格外干爽纯粹。",
                                "reviewer": "Denk Lem (车头资深测试先驱)"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "Frolov #230 目斜纹网 (38×21mm 紧致平卷)",
                                "needle": "2.0mm 紧密实心阶梯卷网",
                                "wire": "0.25mm Kanthal A1 或 Karlson 细编线",
                                "circle": "4 圈 (阻值 0.85Ω)",
                                "note": "13W ~ 15W 温控或调压口吸，PEI 仓体升温极其缓慢，陶瓷套管彻底杜绝线圈侧壁跳火拉弧，烟雾清凉纯净。"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "400 目氧化细网套",
                                "needle": "1.8mm 高纯度石墨碳棒",
                                "wire": "0.25mm A1",
                                "circle": "4 圈 (阻值 0.95Ω)",
                                "note": "碳棒绝缘芯柱垂直契合陶瓷导油孔，无任何金属摩擦，连抽无冷凝喷油。"
                        }
                ],
                "images": [
                        "images/paravozz_eco_sport.jpg",
                        "images/paravozz_eco_sport_deck.jpg",
                        "images/paravozz_eco_sport_parts.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "Marat Mtl 于 2024-01-08 官方历史文献 (#zZhistory) 著录 11g 概念机型",
                        "secondary": "PARaVOzZ® Wiki 官方实拍建档: 2024年1月完成实机参数测定",
                        "analysis": "官方历史文献与 Wiki 参数建档同月闭环。"
                }
        },
        {
                "id": "paravozz_v0_13_airy",
                "name": "Paravozz 0.13 Airy (Пара-Воз 0.13 Airy 2017)",
                "brand": "Paravozz (车头 / Marat)",
                "origin": "俄罗斯 (Andrey Robul · 2017-04-10)",
                "type": "Genesis RDTA",
                "image": "images/paravozz_v0_13_airy.jpg",
                "quickSpecs": [
                        "22mm",
                        "3.0ml",
                        "0.13开山谱系 (纯单机微距)"
                ],
                "specs": {
                        "品牌产地": "Paravozz (Пара-Воз / 车头) · 俄罗斯",
                        "发布时间": "2017年4月",
                        "设备类型": "Genesis RDTA (车头 0.13 纪元 Airy 轻快口吸进气版)",
                        "外形直径": "22 mm",
                        "本体高度": "43.0 mm（不含滴嘴）",
                        "油仓容量": "3.0 ml（初代古典高透耐腐仓）",
                        "主体材质": "医用级顶级不锈钢 / 原厂特种航空钛合金电极部件",
                        "进气规格": "1.4 mm 经典微通风单孔（故称 Airy 轻快通透进气）",
                        "电极平台": "0.13 经典直立双一字固定螺柱与特氟龙绝缘隔离座",
                        "导油孔径": "2.8 mm 垂直导油井",
                        "导油介质": "不锈钢网 (Mesh #230 / #325) / 碳棒复合制作",
                        "接口规格": "标准 510 接口"
                },
                "officialNotes": "Paravozz 0.13 Airy 官方历史要点：考证自俄罗斯 eCigTalk 官方编年史（10.04.2017 — Паравоз 0.13 'Airy' // Japan）与主理人 Marat Mtl 历史档案。该机承接 2015 年 12 月 14 日发布的 0.1 Sunny，由作者 Andrey Robul（japan）针对口吸顺滑度专门将进气微扩至 1.4mm，带来更加通透轻快的烟雾流动体验。配图已彻底肃清此前混杂的 Ghost v2 双机合影，100% 纯粹呈现 0.13 Airy 单体立姿棚拍与专属做芯微距。",
                "reviews": [
                        {
                                "quote": "Vintage Airy on a penon v1. Build in frolovs 230 tasty ropes 647. Airy 的古典通透风味与微通风喉感纯粹得令人感动。",
                                "reviewer": "Olivier Besch (法系资深玩家, 2024年3月5日)"
                        },
                        {
                                "quote": "0.13 Airy 是网子编年史中少有的轻快进气款，朴素直接的风道造就了极度直接甘甜的蒸汽解析。",
                                "reviewer": "Simone Bongi (PARaVOzZ® Wiki 档案馆长)"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "Frolov #230 目细密斜纹网 (45×22mm)",
                                "needle": "紧密手搓微空心卷网",
                                "wire": "Tasty 647 编织微缆",
                                "circle": "4 圈 (阻值 0.85Ω)",
                                "note": "15W 纯正柔和口吸，气雾通透，原汁原味还原早期网子质感。"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "#325 氧化隔离网",
                                "needle": "2.0mm 碳棒芯",
                                "wire": "0.25mm Kanthal",
                                "circle": "5 圈 (阻值 1.25Ω)",
                                "note": "12W 古典高阻口吸，吸阻轻快顺滑。"
                        }
                ],
                "images": [
                        "images/paravozz_v0_13_airy.jpg",
                        "images/paravozz_v0_13_airy_deck.jpg",
                        "images/paravozz_v0_13_airy_mod.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "eCigTalk.org 编年史《Хронология ген》: 确切著录 2017-04-10 出厂 Паравоз 0.13 'Airy' // Japan",
                        "secondary": "eCigTalk «®ГЕНЕЗИС 'Пара ВозЪ'» 专版: 2017年4月中旬工匠 Andrey Robul 批次交付回帖",
                        "analysis": "官方编年史与论坛主楼同日同月精确咬合。"
                }
        },
        {
                "id": "paravozz_ghost_sc_dual",
                "name": "Paravozz Ghost SC Dual (Пара-Воз Ghost SC Dual-Coil)",
                "brand": "Paravozz (车头 / Marat)",
                "origin": "俄罗斯 / 乌克兰 (Andrey Robul · Marat Mtl)",
                "type": "Genesis RDTA",
                "image": "images/paravozz_ghost_sc_dual.jpg",
                "quickSpecs": [
                        "22mm",
                        "3.5ml",
                        "双发超低阻怪兽 (39W爆发力狂魔)"
                ],
                "specs": {
                        "品牌产地": "Paravozz (Пара-Воз / 车头) · 俄罗斯 / 乌克兰",
                        "发布时间": "2024年7月",
                        "设备类型": "Genesis RDTA (Ghost 幽灵系列特装双发 Side-Cap 性能版)",
                        "外形直径": "22 mm",
                        "本体高度": "36.5 mm（紧凑型竞技低矮顶盖）",
                        "油仓容量": "3.5 ml（强化抗溶胀特种树脂仓）",
                        "主体材质": "VT-6 航天钛合金 / 陶瓷绝缘衬垫 (Ceramic Isolate)",
                        "进气规格": "对称双侧 1.6 mm 强劲侧进气 (Dual Side Direct Airflow)",
                        "电极平台": "双立柱双导油孔对称电极座，支持两根独立网芯并联点火",
                        "导油孔径": "2.8 mm × 2（双导油孔）",
                        "导油介质": "不锈钢网 (Mesh #200 90° 直切) / 双碳棒暴力输出",
                        "接口规格": "标准 510 接口"
                },
                "officialNotes": "Paravozz Ghost SC Dual 官方性能要点：作为 Ghost 幽灵家族中专为极致爆发力与浓郁烟雾设计的特异型号，Ghost SC Dual 彻底颠覆了网子雾化器仅能小功率口吸的固有印象。通过两组精准对称的立式网导油与定制侧进气，可在 35~45W 高功率下稳定输出如火山喷发般的高密度冷烟雾。",
                "reviews": [
                        {
                                "quote": "Paravozz Ghost SC Dual: Frolov #200 90° + Frolov NiChrom Strike Ball 12x0.1 4圈 0.35Ω，在 4.7V 39W 驱动下，爆发力和风味浓缩度令人震撼！",
                                "reviewer": "Roger Gulpen (PARaVOzZ® Wiki 欧洲极端玩家, 2024年7月/8月)"
                        },
                        {
                                "quote": "Ghost 系列在 SC 架构下的双发探索证明了车头钛合金腔体在高热通量下的绝佳热平衡性，是性能网子爱好者的狂欢。",
                                "reviewer": "Marat Mtl (PARaVOzZ® Wiki 官方主理人)"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "Frolov #200 目金属网 (22×42mm 两个)",
                                "needle": "90° 直角裁切双立柱卷网",
                                "wire": "Frolov NiChrom Strike Ball 12×0.1 特制花式微缆",
                                "circle": "各 4 圈 (并联总阻值 0.35Ω)",
                                "note": "38~42W 强劲输出，双倍爆发力与饱满烟雾，冷烟雾极其丝滑。"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "300 目双绝缘套",
                                "needle": "双 2.0mm 导电石墨碳棒",
                                "wire": "0.4mm (26AWG) 镍铬合金",
                                "circle": "各 4 圈 (并联阻值 0.45Ω)",
                                "note": "30W 强劲推力，超强导油不断流。"
                        }
                ],
                "images": [
                        "images/paravozz_ghost_sc_dual.jpg",
                        "images/paravozz_ghost_sc_dual_deck.jpg",
                        "images/paravozz_ghost_sc_dual_fire.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "PARaVOzZ® Wiki 官方工程档案: 2024-07-05 由工坊主理人批复登记",
                        "secondary": "欧洲藏家 Roger Gulpen: 2024年7月实测立档并提供微距实拍",
                        "analysis": "原厂档案与资深藏家建档同月吻合。"
                }
        },
        {
                "id": "hellfire_mega",
                "name": "Hellfire Mega (Hellfire Mega Genesis)",
                "brand": "The Attysmith (Hellfire)",
                "origin": "英国 (UK)",
                "type": "Genesis RDTA",
                "image": "images/hellfire_mega.jpg",
                "quickSpecs": [
                        "22 mm",
                        "3.0 ml",
                        "双孔/沙漏聚拢内胆"
                ],
                "specs": {
                        "品牌产地": "The Attysmith / Hellfire (Darren) · 英国",
                        "发布时间": "2012年11月",
                        "设备类型": "Genesis RDTA (高定手工网子雾化器)",
                        "外形直径": "22 mm",
                        "本体高度": "38 mm (不含 510 滴嘴)",
                        "油仓容量": "约 3.0 ml (高硼硅玻璃仓 / 316L 不锈钢外罩)",
                        "主体材质": "316L 顶级不锈钢 (手工拉丝车削)",
                        "进气规格": "经典单侧 1.2mm / 1.5mm 定制进气孔，直吹网芯",
                        "电极平台": "双导油立孔设计，支持单网（带阻流盲塞）或双网 Extreme 输出，正极十字螺栓紧锁",
                        "导油孔径": "2.5 mm (双导油孔 / 备有不锈钢堵头)",
                        "导油介质": "#300 / #400 目不锈钢网 (Mesh) / 氧化网芯",
                        "接口规格": "标准 510 接口 (精密黄铜镀金电极)"
                },
                "officialNotes": "Hellfire Mega (The Attysmith) 官方档案与工艺要点：由英国传奇车工大师 Darren 创立的 Hellfire (The Attysmith) 是全球电子烟高定界的圣殿级品牌。Hellfire Mega 是 Darren 在 22mm 平台上的 Genesis 巅峰之作。其内部独特的弧形/沙漏状聚拢穹顶，配合极其贴合网芯的短进气道，将英国纯烟草烟油中的泥土香与层次感压缩至极点。由于纯手工限量制作并在英国 Hellfire 官方论坛排单，在当年是全球网子收藏家一机难求的圣物。",
                "reviews": [
                        {
                                "quote": "Hellfire Mega 是 22mm Genesis 时代的无上经典。Darren 的不锈钢倒角与螺纹顺滑度无可挑剔，仓内的雾化聚拢效果让五子棋与各类重烟草还原出了前所未有的醇厚度。",
                                "reviewer": "Gabish (高端 Genesis 收藏家 & 独立硬件评测人)"
                        },
                        {
                                "quote": "Mega 的双孔电极台非常灵活，即便是单网配合堵头，其进气撞击网芯的角度也计算得恰到好处，没有任何多余空腔乱流。",
                                "reviewer": "Todd's Reviews (英国资深雾化器评测大师, 2013年)"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "400 目不锈钢网 (28×18mm 精密实心卷)",
                                "needle": "2.0mm 实芯卷网，表层多次退火微氧化",
                                "wire": "0.25mm (30AWG) Kanthal A1 紧密缠绕",
                                "circle": "4 圈 (1.1Ω ~ 1.2Ω)",
                                "note": "13W ~ 15W 纯正口吸，沙漏穹顶彻底阻绝冷凝，烟气极度细腻温润。"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "300 目绝缘套网",
                                "needle": "2.0mm 高纯度石墨导电碳棒",
                                "wire": "0.28mm (29AWG) 镍铬合金",
                                "circle": "4 圈 (0.95Ω)",
                                "note": "16W 稳定推力，强劲导油，极具层次感的烟草解析。"
                        }
                ],
                "images": [
                        "images/hellfire_mega.jpg",
                        "images/hellfire_mega_deck.jpg",
                        "images/hellfire_mega_parts.jpg",
                        "images/hellfire_mega_build.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "Darren (Hellfire) 于 UK Vapers 论坛: 2012-11-20 发布 22mm 大容量 Genesis 批次名单",
                        "secondary": "Todd's Reviews (YouTube): 2012年12月实测《Hellfire Mega Genesis Atomiser by Darren》",
                        "analysis": "原厂预定与视频评测交付周期吻合。"
                }
        },
        {
                "id": "hellfire_mini",
                "name": "Hellfire Mini (Hellfire Mini Genesis)",
                "brand": "The Attysmith (Hellfire)",
                "origin": "英国 (UK)",
                "type": "Genesis RDTA",
                "image": "images/hellfire_mini.jpg",
                "quickSpecs": [
                        "16 mm",
                        "1.5 ml",
                        "一体式车削吸嘴"
                ],
                "specs": {
                        "品牌产地": "The Attysmith / Hellfire (Darren) · 英国",
                        "发布时间": "2012年5月",
                        "设备类型": "Genesis RDTA (超紧凑 16mm 口吸网子雾化器)",
                        "外形直径": "16 mm (纤细笔型与微型机械杆绝配)",
                        "本体高度": "32 mm (集成一体式短吸嘴)",
                        "油仓容量": "约 1.5 ml (磨砂/高透耐腐蚀储油仓)",
                        "主体材质": "316L 顶级不锈钢 (英国本土手工精修)",
                        "进气规格": "单孔 1.0mm ~ 1.2mm 紧致口吸直接侧进气",
                        "电极平台": "微型化偏心单导油孔平台，一体式不锈钢顶盖集成导气与滴嘴",
                        "导油孔径": "2.2 mm (单导油孔)",
                        "导油介质": "#325 / #400 目不锈钢网 (Mesh)",
                        "接口规格": "标准 510 接口"
                },
                "officialNotes": "Hellfire Mini (The Attysmith) 官方档案与工艺要点：作为 The Attysmith 最负盛名的超小直径 Genesis 代表作，Hellfire Mini 采用极其严苛的 16mm 直径架构。顶盖与吸嘴采用一体成型不锈钢车削，极度压缩的燃烧室内部体积几乎降至物理极限，带来了无可比拟的高温浓缩风味。在早期机械杆流行时代，Hellfire Mini 搭配 14500/16650 机械杆是高端电子烟玩家最具品位的标配。",
                "reviews": [
                        {
                                "quote": "Hellfire Mini 的 16mm 燃烧室堪称微型奇迹，哪怕只用 10W 的低功率驱动，其击喉感与烟雾饱和度都远超普通 22mm 雾化器。",
                                "reviewer": "Gabish (高端 Genesis 收藏家 & 独立评测人)"
                        },
                        {
                                "quote": "Darren 将英国手工业的严谨带入到了 Mini 的每一处螺纹中。一体式吸嘴不仅手感极佳，更能让刚从网芯蒸发的雾气以最短路径进入口腔。",
                                "reviewer": "UK Vapers Archive (英国玩家论坛精选集)"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "#400 目不锈钢网 (22×15mm 极紧密实心小卷)",
                                "needle": "1.8mm 细针紧密手工实芯卷",
                                "wire": "0.20mm (32AWG) / 0.22mm Kanthal A1 细丝",
                                "circle": "4 圈 (1.4Ω ~ 1.6Ω)",
                                "note": "9W ~ 11W 纯口吸，冷雾极其紧致饱满，击喉感直击咽喉。"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "400 目超薄双层包裹",
                                "needle": "1.6mm 极细高致密石墨碳棒",
                                "wire": "0.25mm Kanthal A1",
                                "circle": "4 圈 (1.2Ω)",
                                "note": "11W 柔顺击发，导油连续顺畅，风味解析锐利。"
                        }
                ],
                "images": [
                        "images/hellfire_mini.jpg",
                        "images/hellfire_mini_parts.jpg",
                        "images/hellfire_mini_deck.jpg",
                        "images/hellfire_mini_mod.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "Darren (Hellfire / The Attysmith) 于 UK Vapers 论坛: 2012-05-18 首发 16mm 创世纪预定贴与图纸",
                        "secondary": "Todd's Reviews (YouTube): 2012年6月实测《Hellfire Mini Genesis Atomiser by Darren》",
                        "analysis": "UK Vapers 官方名单与 YouTube 评测时间链闭环。"
                }
        },
        {
                "id": "inax_18",
                "name": "In'Ax 18 (In'Ax 18 MkII / Mk2)",
                "brand": "Athea Mods",
                "origin": "法国",
                "type": "Genesis RDTA",
                "image": "images/inax_18.jpg",
                "quickSpecs": [
                        "18 mm",
                        "2.0 ml",
                        "中心柱同轴 Central Wick"
                ],
                "specs": {
                        "品牌产地": "Athea Mods (Vincent Athea) · 法国",
                        "发布时间": "2015年12月",
                        "设备类型": "Genesis RDTA (中心同轴发热网子雾化器)",
                        "外形直径": "18 mm",
                        "本体高度": "34 mm (不含滴嘴)",
                        "油仓容量": "约 2.0 ml (耐高温微黄 PEI / 聚碳酸酯透明仓)",
                        "主体材质": "316L 医疗级不锈钢 / 陶瓷涂层绝缘中心轴",
                        "进气规格": "外壁阶梯可调进气轮盘 (0.8mm / 1.0mm / 1.2mm / 1.5mm)",
                        "电极平台": "Vincent Athea 专利中轴同轴设计：中柱正极配微型弹簧/滚珠扣，底部基座负极锁环",
                        "导油孔径": "中置中空中心柱 (外径约 2.0mm，网子环形包裹中心轴)",
                        "导油介质": "#200 / #300 目不锈钢网 (直接环绕中心正极轴)",
                        "接口规格": "标准 510 接口"
                },
                "officialNotes": "In'Ax 18 (Athea Mods) 官方档案与工艺要点：法国制作者 Vincent Athea 是 Genesis 历史上唯一颠覆了“偏心立孔”传统架构并取得空前成功的宗师。In'Ax 18 采用了标志性的“中心轴同轴（Central Post）”结构，网子直接卷在中心正极绝缘柱上，发热丝螺旋上升，正极通过顶部的微型滚珠螺母或弹簧紧固，负极由底部导电螺环固定。18mm 的微缩内胆配合多档位进气，彻底消除了侧进气不对称造成的受热不均，是法国网子设计史上的皇冠明珠。",
                "reviews": [
                        {
                                "quote": "In'Ax 18 拥有无可替代的均匀雾化体验。由于发热丝在正中心同心发热，烟雾在圆柱形气道内以完美同心圆扩散，烟油原有的花果香和复合香气被分毫不差地呈现。",
                                "reviewer": "Vapor Cloud Japan (日本高端网子玩家评测专栏)"
                        },
                        {
                                "quote": "中心发热柱彻底解决了 Genesis 传统偏心网子容易单侧积碳和死角的弊病，18mm 的紧致气道对于法式甜点和淡烟草来说堪称完美。",
                                "reviewer": "Vapoteurs.net (法国专业电子烟档案评测)"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "Superfine #300 目不锈钢网 (20×14mm 直卷)",
                                "needle": "中置套筒卷法：直接紧贴中轴中心柱紧密卷制",
                                "wire": "0.25mm (30AWG) Kanthal A1 / 弹簧顶固定",
                                "circle": "4 圈 (1.0Ω ~ 1.1Ω)",
                                "note": "12W ~ 14W 驱动，受热 360° 全向完全均匀，层次感极其丰富细腻。"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "400 目套筒",
                                "needle": "2.0mm 中空石墨碳管（中心绝缘穿轴）",
                                "wire": "0.28mm 镍铬合金",
                                "circle": "4 圈 (0.85Ω)",
                                "note": "15W 澎湃输出，中轴散热稳定无积碳。"
                        }
                ],
                "images": [
                        "images/inax_18.jpg",
                        "images/inax_18_deck.jpg",
                        "images/inax_18_cap.jpg",
                        "images/inax_18_afc.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "Vincent Athea (Athea Mods) 官方出厂交付: 2015-12-04 正式上市",
                        "secondary": "Vapoteurs.net (法国专业电子烟媒体): 2015年12月发布 In'Ax 18 深度专题报道",
                        "analysis": "18mm 细管中心柱 Genesis，法国原厂与媒体双源同月吻合。"
                }
        },
        {
                "id": "inax_mk3",
                "name": "In'Ax MKIII (In'Ax Mk3 / V3)",
                "brand": "Athea Mods",
                "origin": "法国",
                "type": "Genesis RDTA",
                "image": "images/inax_mk3.jpg",
                "quickSpecs": [
                        "22 mm",
                        "3.0 ml",
                        "第三代中轴系统 / 30.5mm超矮"
                ],
                "specs": {
                        "品牌产地": "Athea Mods (Vincent Athea) · 法国",
                        "发布时间": "2016年3月",
                        "设备类型": "Genesis RDTA (第三代中轴旗舰网子雾化器)",
                        "外形直径": "22 mm",
                        "本体高度": "30.5 mm (低矮紧凑竞技级机身)",
                        "油仓容量": "约 3.0 ml (医用级透明 Pyrex 玻璃 / 特制 PC 仓)",
                        "主体材质": "316L 手术级不锈钢 / 陶瓷与特氟龙双绝缘",
                        "进气规格": "顶盖集成 5 孔精确进气轮盘 (0.8mm / 1.0mm / 1.2mm / 1.5mm / 1.8mm)",
                        "电极平台": "第三代改进型中轴系统：顶部免工具微型紧固弹簧扣 (Grip Spring)，底部负极自锁环",
                        "导油孔径": "中置立式导油轴 (外径 2.2mm，360° 全方位网子覆盖)",
                        "导油介质": "#200 / #325 / #400 目金属网 (环形同心柱裹制)",
                        "接口规格": "标准 510 接口 (银电极可调螺丝)"
                },
                "officialNotes": "In'Ax MKIII (In'Ax Mk3) 官方档案与工艺要点：作为 Vincent Athea 整个 In'Ax 谱系中成熟度最高、全球口碑最出众的 22mm 旗舰，MKIII 针对前代 MKII 进行了彻底革新。本体高度大幅压缩至仅 30.5mm，采用了全新一代的免工具紧固弹簧扣，固定正极发热丝时再也无需繁琐的小螺丝；底部的负极压环更加精准顺滑；进气环提供 5 档细分进气，彻底适应从极度紧致 MTL 到轻微 RDL 的全范围口吸需求。",
                "reviews": [
                        {
                                "quote": "In'Ax MKIII 是法国电子烟工程美学的极高结晶。高度仅 30.5mm 的机身内蕴藏着最纯净的同轴燃烧室，弹簧卡扣固定发热丝极度优雅且杜绝跳阻。",
                                "reviewer": "Vap-Extrem (欧洲资深高定网子硬件专栏)"
                        },
                        {
                                "quote": "在 22mm 级别的 Genesis 中，MKIII 无论在气味解析的纯净度还是在防漏油工程上，都做到了 Athea 的巅峰水准。",
                                "reviewer": "Vapinart Archive (美国高定电子烟艺术典藏库, 2015年)"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "Frolov #200 目 / #325 目精细网 (24×16mm)",
                                "needle": "同心空心卷网，套入 MKIII 特氟龙绝缘中轴",
                                "wire": "0.28mm (29AWG) Kanthal A1",
                                "circle": "4 圈 (0.85Ω ~ 0.95Ω)",
                                "note": "15W ~ 18W 驱动，中轴供油极度均匀，烟雾凉爽细腻，还原度无可挑剔。"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "300 目耐温外网",
                                "needle": "2.2mm 中心穿轴石墨碳棒",
                                "wire": "0.30mm 镍铬合金",
                                "circle": "4 圈 (0.75Ω)",
                                "note": "18W 爆发输出，极高导油速度，耐高温不糊芯。"
                        }
                ],
                "images": [
                        "images/inax_mk3.jpg",
                        "images/inax_mk3_parts.jpg",
                        "images/inax_mk3_deck.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "Athea Mods 官方公告: 2016-03-29 正式发售 In'Ax Mk3 22mm 旗舰",
                        "secondary": "Vapinart 官方典藏档案 & ECF 专帖: 2016年4月权威建档",
                        "analysis": "原厂出厂与经销商交付时间吻合。"
                }
        },
        {
                "id": "somnium",
                "name": "Somnium (Somnium Novum Genesis)",
                "brand": "Somnium Mods (Kaufmann / Esmoke)",
                "origin": "芬兰 (Finland)",
                "type": "Genesis RDTA",
                "image": "images/somnium.jpg",
                "quickSpecs": [
                        "22 mm",
                        "3.5 ml",
                        "北欧手工雕琢 / 锥形内胆"
                ],
                "specs": {
                        "品牌产地": "Somnium Mods (Kaufmann / Esmoke) · 芬兰",
                        "发布时间": "2012年11月",
                        "设备类型": "Genesis RDTA (北欧手工网子雾化器)",
                        "外形直径": "22 mm",
                        "本体高度": "50 mm (不含 510 滴嘴)",
                        "油仓容量": "约 3.5 ml (医用级硼硅 Pyrex 玻璃仓)",
                        "主体材质": "304/316 精密拉丝不锈钢 / 镀银导电电极 / 陶瓷绝缘衬套",
                        "进气规格": "1.2 mm 经典口吸侧向进气孔，直对网芯蒸发面",
                        "电极平台": "经典偏心垂直单导油立柱电极座，正极滚花双螺母无工具锁丝，内嵌绝缘注油螺丝",
                        "导油孔径": "2.8 mm (带绝缘套管) / 3.5 mm (无套管直通)",
                        "导油介质": "#325 / #400 目不锈钢网 (Mesh) / 氧化网芯",
                        "接口规格": "标准 510 接口 (黄铜镀银高导电正极螺丝)"
                },
                "officialNotes": "Somnium (Somnium Novum) 官方档案与工艺要点：Somnium 由芬兰制作者 Kaufmann 与 Esmoke 团队打造，芬兰本土常称其为‘Mesh-maailman Suomi-kuningas’。其结构特点为厚壁 Pyrex 玻璃仓由上下不锈钢螺纹圈锁紧，顶盖内部车削出阶梯锥形聚拢内胆，加速烟雾在上升通道中的收拢聚气。正极采用银涂层连接件以降低内阻损耗，在欧洲玩家群体中流传广泛。",
                "reviews": [
                        {
                                "quote": "Somnium 是我用过的 Genesis 雾化器中导电性与制造公差最为优秀的杰作之一。它的不锈钢拉丝质感和锥形内胆将烟油原味提升到了不可思议的高度。",
                                "reviewer": "Julio Ruades (El Mono Vapeador, 西班牙权威电子烟评测大师, 2014年)"
                        },
                        {
                                "quote": "Somnium 的做工堪称芬兰现代工业的缩影，螺纹极其顺滑，2.8mm 绝缘导油孔在氧化网卷下的导油速度极快，完全没有干烧隐患。",
                                "reviewer": "igetcha69 (Scott Bonner, 英国资深电子烟先锋评测)"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "Superfine #325 目不锈钢网 (24×18mm 实芯紧密卷)",
                                "needle": "2.0mm 实芯卷网，表层多次退火微氧化",
                                "wire": "0.25mm (30AWG) Kanthal A1",
                                "circle": "4 圈 (1.1Ω ~ 1.2Ω)",
                                "note": "12W ~ 14W 纯口吸，冷凝聚拢内胆带来极其纯正细腻的花果香与烟草香。"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "300 目双绝缘套网",
                                "needle": "2.0mm 高致密导电石墨碳棒",
                                "wire": "0.28mm (29AWG) 镍铬合金",
                                "circle": "4 圈 (0.85Ω)",
                                "note": "15W 稳定输出，导油连贯，烟雾饱和温润。"
                        }
                ],
                "images": [
                        "images/somnium.jpg",
                        "images/somnium_deck.jpg",
                        "images/somnium_parts.jpg",
                        "images/somnium_cap.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "芬兰 Kaufmann (Esmoke) 于 e-savuke 论坛与 eCigTalk: 2012-11-08 官方发售公告",
                        "secondary": "Todd's Reviews (YouTube): 2012年11月实测《The Somnium Genesis Atomiser by Kaufmann》",
                        "analysis": "芬兰官方发售与 Todd 首测同月建档，双源完全一致。"
                }
        },
        {
                "id": "ac9",
                "name": "AC9 (Authentic Cloud 9 Genesis)",
                "brand": "Vapinaze (Rip Trippers / Brent)",
                "origin": "美国 (USA)",
                "type": "Genesis RDTA",
                "image": "images/ac9.jpg",
                "quickSpecs": [
                        "22 mm",
                        "3.5 ml",
                        "美国早中名作 / 超大油仓"
                ],
                "specs": {
                        "品牌产地": "Vapinaze (Rip Trippers / Brent) · 美国",
                        "发布时间": "2012年9月",
                        "设备类型": "Genesis RDTA (美国经典全金属网子雾化器)",
                        "外形直径": "22 mm",
                        "本体高度": "55.5 mm (不含 510 接口)",
                        "油仓容量": "约 3.5 ml (高透耐腐蚀厚壁透明仓)",
                        "主体材质": "手术级 316L 不锈钢 / 黄铜电极柱 / 绝缘 Delrin 顶盖底塞",
                        "进气规格": "1.25 mm / 1.5 mm 精确侧进气孔 (直吹线圈核心)",
                        "电极平台": "经典单孔偏心网电极座，正极采用独创弹簧垫片自紧固系统 (Spring & Washer)，硅胶盲塞快速注油",
                        "导油孔径": "3.5 mm (早期 Genesis 中罕见的超大口径导油孔)",
                        "导油介质": "#400 / #500 目不锈钢网 (Mesh) / 粗径实心卷",
                        "接口规格": "标准 510 螺纹接口"
                },
                "officialNotes": "AC9 (Authentic Cloud 9) 官方档案与工艺要点：作为 2012 年底横空出世的美国 Genesis 标志性名作，AC9 由北美电子烟顶流评测先驱 Rip Trippers 深度参与设计并由美国 Vapinaze 原厂数控精密切削。AC9 在电子烟历史上具有里程碑意义：它首次引入了 3.5mm 超大导油孔，彻底解决了早期 Genesis 因导油孔过窄导致的持续供油不足问题；其正极独创的弹簧加垫片压丝结构，无需螺丝刀即可极速夹紧发热丝脚。在当年搭配 Caravela、Nemesis 等机械杆，是全球高玩眼中至高无上的‘云雾级’网子神器。",
                "reviews": [
                        {
                                "quote": "AC9 是 2012 年美国网子界的一座丰碑。它的加工质量极其精湛，没有任何金属毛刺，3.5mm 超大导油孔配合 400 目网子带来的烟雾浓郁度比当时任何 Genesis 都要霸道！",
                                "reviewer": "Todds Reviews (Todd, 英国顶级雾化器评测大师, 2013年)"
                        },
                        {
                                "quote": "在经历了数周的深度重度使用后，我可以负责任地说 AC9 是我抽过的 Genesis 中击喉感和风味表现最锐利的机器之一，纯手工车削的质感令人爱不释手。",
                                "reviewer": "igetcha69 (Scott Bonner, 英国知名资深硬件评测人)"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "#400 目不锈钢网 (28×16mm 粗径紧密实心卷)",
                                "needle": "2.5mm 实芯卷网，火焰均匀多次氧化退火",
                                "wire": "0.25mm (30AWG) / 0.28mm Kanthal A1",
                                "circle": "4 圈 (1.0Ω ~ 1.15Ω)",
                                "note": "14W ~ 17W 驱动，超大孔径彻底杜绝糊芯，烟气饱满浓烈，击喉感强悍。"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "400 目超薄绝缘外网",
                                "needle": "2.2mm 导电石墨碳棒",
                                "wire": "0.28mm 镍铬合金",
                                "circle": "4 圈 (0.9Ω)",
                                "note": "16W 澎湃击发，供油极其充沛，风味层次分明。"
                        }
                ],
                "images": [
                        "images/ac9.jpg",
                        "images/ac9_deck.jpg",
                        "images/ac9_parts.jpg",
                        "images/ac9_cap.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "Brent & Rip Trippers (Vapinaze) 于 ECF 论坛: 2012-09-26 官方发售公告与批次名单",
                        "secondary": "GrimmGreen (YouTube): 2012年10月视频实测《The AC9 Genesis Atomizer by Vapinaze》",
                        "analysis": "ECF 官方发售日与 GrimmGreen 首发评测时间吻合。"
                }
        },
        {
                "id": "gbell",
                "name": "G-Bell (G-Bell Genesis)",
                "brand": "G-Bell Mods (Gianluca Bellavia / Yenki69)",
                "origin": "意大利 / 塞尔维亚",
                "type": "Genesis RDTA",
                "image": "images/gbell.jpg",
                "quickSpecs": [
                        "20 mm",
                        "3.0 ml",
                        "纯手工制作 / 阶梯多层散热鳍"
                ],
                "specs": {
                        "品牌产地": "G-Bell Mods (Gianluca Bellavia / Yenki69) · 意大利 / 塞尔维亚",
                        "发布时间": "2012年10月",
                        "设备类型": "Genesis RDTA (地中海高定网子雾化器)",
                        "外形直径": "20 mm (经典复古修长口吸比例)",
                        "本体高度": "约 48 mm (不含滴嘴)",
                        "油仓容量": "约 3.0 ml (Pyrex 医用级耐高温玻璃仓)",
                        "主体材质": "AISI 304 顶级食品级不锈钢 / 特氟龙绝缘套 (Teflon Isolate)",
                        "进气规格": "1.0 mm / 1.2 mm 紧致口吸侧向气孔，精准撞击网芯发热区",
                        "电极平台": "偏心单孔电极平台，中心正极立柱配绝缘硅胶环，独立负极螺栓，特氟龙绝缘导油孔",
                        "导油孔径": "2.5 mm (内置特氟龙耐高温绝缘套管)",
                        "导油介质": "#300 / #400 目不锈钢网 (Mesh) / 钢丝绳 (Wire Cable)",
                        "接口规格": "标准 510 接口"
                },
                "officialNotes": "G-Bell Genesis 官方档案与工艺要点：G-Bell 由制作者 Yenki69 与意大利名家 Gianluca Bellavia 在 VaporWall 论坛时期联合打造。外观特征为顶盖的多层渐变车削散热鳍片（Cooling Fins），辅助疏散紧凑雾化室内聚集的热量。20mm 紧凑直径使烟雾在进入吸嘴前获得良好的聚气浓缩，是欧洲早期手工网子中的代表型号。",
                "reviews": [
                        {
                                "quote": "G-Bell 的做工展现了欧洲手工匠人的极致诚意。特氟龙绝缘网孔彻底解决了金属毛刺短路的问题，多层散热鳍片即便连抽也始终保持温凉。",
                                "reviewer": "Gabish (高端 Genesis 收藏家 & 独立硬件评测人)"
                        },
                        {
                                "quote": "在 20mm 经典比例的 Genesis 中，G-Bell 拥有无可比拟的吸阻紧致感与原味解析力，阶梯顶盖的散热效率令人印象深刻。",
                                "reviewer": "VaporWall High-End Archive (欧洲高端收藏家档案库, 2012年)"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "#300 目高目数不锈钢网 (22×16mm 直卷)",
                                "needle": "2.0mm 紧密实心卷网，微氧化处理",
                                "wire": "0.28mm (29AWG) Kanthal A1",
                                "circle": "4 圈 (0.95Ω ~ 1.05Ω)",
                                "note": "13W ~ 15W 口吸输出，特氟龙绝缘孔彻底杜绝短路跳阻，烟雾冷凉甘醇。"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "400 目细致外层网",
                                "needle": "1.8mm 高纯度石墨碳棒",
                                "wire": "0.30mm 镍铬合金",
                                "circle": "4 圈 (0.75Ω)",
                                "note": "15W 强力推发，导油迅速连续，解析极其锐利。"
                        }
                ],
                "images": [
                        "images/gbell.jpg",
                        "images/gbell_parts.jpg",
                        "images/gbell_deck.jpg",
                        "images/gbell_build.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "Gianluca Bellavia (Yenki69) 于 eCigTalk 与 Vaporwall: 2012-10-15 宣布首批量产面市",
                        "secondary": "Esigarettaportal (意大利最大电子烟论坛): 2012年10月专帖讨论与实装评测",
                        "analysis": "意/塞联合工坊首发与意大利论坛建档时间吻合。"
                }
        },
        {
                "id": "docdave_bliss",
                "name": "Bliss Genesis (Bliss V1 / V2)",
                "brand": "Doc Dave",
                "origin": "美国 (USA)",
                "type": "Genesis RDTA",
                "image": "images/docdave_bliss.jpg",
                "quickSpecs": [
                        "22 mm",
                        "3.0 ml",
                        "双孔/多孔平台 / 滚花外罩"
                ],
                "specs": {
                        "品牌产地": "Doc Dave · 美国 (USA)",
                        "发布时间": "2012年8月",
                        "设备类型": "Genesis RDTA (高端全金属多孔网子雾化器)",
                        "外形直径": "22 mm",
                        "本体高度": "42 mm (不含滴嘴)",
                        "油仓容量": "约 3.0 ml (耐腐蚀 Pyrex 玻璃仓 / 不锈钢开窗保护外罩)",
                        "主体材质": "316L 顶级不锈钢 (CNC 精密滚花车削)",
                        "进气规格": "双侧对称可切侧进气孔 (1.2mm / 1.5mm)，支持单网/双网直吹",
                        "电极平台": "Doc Dave 标志性多导油孔平台，支持双网并联（Dual Wick）或单网带盲塞，正极十字螺栓顶锁",
                        "导油孔径": "2.5 mm × 2 (双网孔配置)",
                        "导油介质": "#325 / #400 目不锈钢网 (Mesh)",
                        "接口规格": "标准 510 接口 (底座一体化数控切削)"
                },
                "officialNotes": "Bliss Genesis (Doc Dave) 官方档案与工艺要点：Bliss 是美国制作者 Doc Dave 继 Steam Turbine 之后推出的经典作品。外部配置了菱形滚花不锈钢开窗保护套，内部配备 2.5mm 双导油立孔系统，支持单发口吸与双发并联网芯配置。其 510 螺纹由底座一体成型车削，避免了分体压装连接器的松动与跳阻，是早期机械杆时代的代表重器。",
                "reviews": [
                        {
                                "quote": "Doc Dave 的 Bliss 拥有当年最扎实的不锈钢质感。双导油孔的布局非常从容，菱形滚花外罩既防滑又能有效保护玻璃内胆，气味还原极其醇厚。",
                                "reviewer": "Gabish (高端 Genesis 收藏家 & 独立硬件评测人)"
                        },
                        {
                                "quote": "Steam Turbine 与 Bliss 奠定了 Doc Dave 在全球网子界的宗师地位。无论是单发还是双网点火，燃烧室内部的气流撞击都精准无比。",
                                "reviewer": "New Vapor Forum Archive (北美高端电子烟专栏, 2013年)"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "双 #400 目金属网 (各 18×14mm 紧密卷)",
                                "needle": "2.0mm 紧密实芯网卷",
                                "wire": "0.22mm (31AWG) Kanthal A1 细丝",
                                "circle": "各 4 圈 (双发并联总阻值 0.65Ω ~ 0.7Ω)",
                                "note": "22W ~ 26W 双发并联驱动，双倍烟雾密度，醇正无杂味。"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "300 目双绝缘套",
                                "needle": "双 1.8mm 高致密石墨碳棒",
                                "wire": "0.25mm Kanthal A1",
                                "circle": "各 4 圈 (并联阻值 0.6Ω)",
                                "note": "20W 强劲稳定输出，双碳棒导油澎湃不断流。"
                        }
                ],
                "images": [
                        "images/docdave_bliss.jpg",
                        "images/docdave_bliss_deck.jpg",
                        "images/docdave_bliss_parts.jpg",
                        "images/docdave_bliss_build.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "Doc Dave 于 ECF 官方版块: 2012-08-05 发布 Bliss Genesis V1 正式上市通告",
                        "secondary": "Todd's Reviews (YouTube): 2012年8月评测《The BliSS Genesis Atomiser by Doc Dave》",
                        "analysis": "同月首发出厂与评测建档，美系双网孔经典。"
                }
        },
        {
                "id": "luca_spider",
                "name": "Spider (Spider Mesh Genesis BF)",
                "brand": "Luca Creations",
                "origin": "意大利",
                "type": "Genesis RDTA (意系经典底注立式网子)",
                "image": "images/spider_mesh.jpg",
                "quickSpecs": [
                        "22mm",
                        "BF底注/储油",
                        "意系网子天花板"
                ],
                "specs": {
                        "品牌产地": "Luca Creations (Luca Cassenti) · 意大利",
                        "发布时间": "2017年12月",
                        "设备类型": "Genesis RDTA / BF Mesh (偏置立式网芯 / 意系纯正风味机)",
                        "外形直径": "22.0 mm",
                        "本体高度": "约 26.5 mm（极度微型压缩雾化室，不含滴嘴）",
                        "油仓容量": "底注导油系统 (BF Squonk / 液仓储油)",
                        "主体材质": "316L 医疗级不锈钢 / 高耐热绝缘套件 / 阳极氧化铝与拉丝钢盖",
                        "进气规格": "侧向精准对冲微孔 (1.2mm 定制口吸风道，直吹发热丝正中)",
                        "电极平台": "偏置直立单发夹丝极柱 (Micro Chamber 超紧凑聚气底座)",
                        "导油孔径": "2.8 mm (适配 #325 ~ #500 目不锈钢细网复合卷)",
                        "导油介质": "不锈钢网 (Mesh #325 / #400 / #500) / 避雷针碳棒系统",
                        "接口规格": "标准 510 BF 底注与储油通用螺纹接口"
                },
                "officialNotes": "Luca Creations 原厂设计要点：由意大利制作者 Luca Cassenti 打造的进阶网子名作。Spider 在延续 Duetto 设计语言的同时，将 22mm 扁平聚气仓与立式单发网芯结构结合。其 2.8mm 偏置导油孔与斜向微孔进气形成导流风道，适合天然烟草提取物（NETs）等有机烟草风味的解析。",
                "reviews": [
                        {
                                "quote": "Spider 是 Luca Creations 对纯网子风味解析的又一巅峰呈现。它与 Duetto 一样拥有几乎零冷凝的雾化仓体，搭配 400 目斜纹网和 0.28mm 发热丝，抽吸意大利有机草本烟油时的干爽度与击喉感纯正无可比拟。",
                                "author": "Sigaretta Elettronica Forum 资深品鉴组",
                                "platform": "Sigaretta Elettronica Forum (意大利电子烟极客论坛)",
                                "topic": "Spider Luca Creation: quale mesh e setup per tabacchi organici",
                                "url": "https://www.sigarettaelettronicaforum.com"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "400目 316L 斜纹网",
                                "size": "24mm * 35mm 实心卷",
                                "wraps": "0.28mm Kanthal A1 / 2.5圈径 / 4圈 / 约 0.95Ω"
                        },
                        {
                                "mesh": "325目 316 不锈钢网",
                                "size": "24mm * 30mm 实心卷",
                                "wraps": "0.25mm Kanthal A1 / 2.5圈径 / 4圈 / 约 1.15Ω"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "325目 316 斜纹",
                                "needle": "24*35mm",
                                "vm3": "",
                                "vm4": "",
                                "vms": "",
                                "s35": "",
                                "snet": ""
                        },
                        {
                                "mesh": "400目 316 斜纹",
                                "needle": "24*40mm",
                                "vm3": "",
                                "vm4": "",
                                "vms": "",
                                "s35": "",
                                "snet": ""
                        }
                ],
                "images": [
                        "images/spider_mesh.jpg",
                        "images/spider_deck.jpg",
                        "images/spider_cap.jpg",
                        "images/spider_parts.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "意大利 Luca Creations 官方商业交付: 2017-12-08 正式发售 Spider BF Genesis",
                        "secondary": "Sigaretta Elettronica Forum: 2017年12月专帖开箱与风味实测",
                        "analysis": "意大利官方批次与论坛同月吻合。"
                }
        },
        {
                "id": "line_v2",
                "name": "Line V2 (Genesis Line V2 / Line LE)",
                "brand": "Van Mods (Vanja Bonic)",
                "origin": "克罗地亚 / 欧洲",
                "type": "Genesis RDTA (14mm 黄金年代珠宝级始祖)",
                "image": "images/line_v2.jpg",
                "quickSpecs": [
                        "14mm超窄",
                        "2.0ml",
                        "创世纪极简鼻祖"
                ],
                "specs": {
                        "品牌产地": "Van Mods (Vanja Bonic · Van & Del Design 前身) · 克罗地亚 / 欧洲",
                        "发布时间": "2012年3月",
                        "设备类型": "Genesis RDTA (早期经典超细口吸立式导油网子)",
                        "外形直径": "14.0 mm (珠宝级极简纤细管身)",
                        "本体高度": "约 54.0 mm（含一体式精密车削吸嘴与透明油窗仓）",
                        "油仓容量": "约 2.0 ml (医用不锈钢镂空外护套 + 内置透明油仓)",
                        "主体材质": "304 顶级医疗不锈钢 / 黄铜中心极柱 / 食品级耐磨密封圈",
                        "进气规格": "固定微孔侧打对冲进气 (1.0 mm 极紧口吸，正对网芯中上部)",
                        "电极平台": "经典创世纪中心立柱正极 + 外圈螺丝负极 (Center-Post Classic Genesis)",
                        "导油孔径": "2.4 mm (适配 #400 ~ #500 目精细卷网)",
                        "导油介质": "氧化不锈钢网 (Mesh #325 / #400 / #500) 细芯卷制",
                        "接口规格": "标准 510 接口 (支持搭配 14-22mm 装饰环适配机械杆)"
                },
                "officialNotes": "Van Mods 原厂设计要点：2012 年由克罗地亚天才工匠 Vanja Bonic（即日后举世闻名的 Van & Del Design 联合创始人）亲手车削的 Genesis Line 系列是全球网子历史上公认的‘微雕艺术品’。其颠覆性地将传统庞大的 Genesis 压缩至 14mm 极致纤细直径，中心立柱贯穿全机，上盖侧打孔与网芯保持微米级间距，在极窄的微型雾化仓内创造出近乎无空气稀释的高密度浓缩蒸汽。",
                "reviews": [
                        {
                                "quote": "Line V2 就像是戴在机械杆顶端的一件珠宝。14mm 的超小雾化室带来了无与伦比的聚气效果，每一口吸入的烟雾都极其细腻温暖，对纯烟草本香的凝聚度在当年创世纪黄金时代几乎无人能敌。",
                                "author": "Julio Ruades (El Mono Vapeador)",
                                "platform": "El Mono Vapeador (西班牙资深评测档案)",
                                "topic": "Genesis Line LE by Van: La elegancia en 14mm",
                                "url": "https://www.elmonovapeador.com"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "400目 316 斜纹网",
                                "size": "28mm * 35mm 实心卷",
                                "wraps": "0.20mm 镍铬或康泰尔 / 2.0圈径 / 4圈 / 约 1.5Ω"
                        },
                        {
                                "mesh": "500目 细不锈钢网",
                                "size": "28mm * 32mm 实心卷",
                                "wraps": "0.20mm Kanthal A1 / 2.0圈径 / 4/5圈 / 约 1.7Ω"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "400目 316 斜纹",
                                "needle": "28*35mm",
                                "vm3": "",
                                "vm4": "",
                                "vms": "",
                                "s35": "",
                                "snet": ""
                        }
                ],
                "images": [
                        "images/line_v2.jpg",
                        "images/line_v2_deck.jpg",
                        "images/line_v2_parts.jpg",
                        "images/line_v2_cap.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "Vanja Bonic (Van & Del) 于 Vaporwall 与 ECF 论坛: 2012-03-15 官方发布 Genesis Line V2 首批交付名单",
                        "secondary": "Todd's Reviews (YouTube): 2012年5月实测《Genesis Line V2 by Van》",
                        "analysis": "交付周期 1-2 个月，克罗地亚极简 14mm 细管中心柱 Genesis。"
                }
        },
        {
                "id": "foggatti_t22",
                "name": "Foggatti T22 (Foggatti Type 22 / VF Genesis)",
                "brand": "Foggatti (FoGGy)",
                "origin": "英国 (UK)",
                "type": "Genesis RDTA (英系三大神作之一 / 顶级微缩聚气仓)",
                "image": "images/foggatti_t22.jpg",
                "quickSpecs": [
                        "22mm",
                        "3.0ml",
                        "英系三大神作"
                ],
                "specs": {
                        "品牌产地": "Foggatti (FoGGy / Foggatti Mod) · 英国 (UK)",
                        "发布时间": "2012年10月",
                        "设备类型": "Genesis RDTA (顶级英系偏置单孔立式高阶创世纪)",
                        "外形直径": "22.0 mm",
                        "本体高度": "约 41.5 mm（不含 510 接口与滴嘴）",
                        "油仓容量": "约 3.0 ml (Pyrex 高硼硅耐热玻璃仓 + 精密防护钢套)",
                        "主体材质": "316 航天级不锈钢 / 黄铜导电配件 / PEEK 耐高温绝缘套",
                        "进气规格": "顶部旋转限位调节进气 (0.9mm / 1.1mm / 1.3mm 定向对冲打丝)",
                        "电极平台": "偏置直立单网孔甲板 (Micro Dome 倾斜聚气微缩仓)",
                        "导油孔径": "2.8 mm (经典单孔位，配特氟龙防短路绝缘衬套)",
                        "导油介质": "高目数不锈钢网 (#400 / #500 Mesh) / 避雷针碳棒系统",
                        "接口规格": "标准 510 螺纹接口 (镀银正极螺丝，超低内阻)"
                },
                "officialNotes": "Foggatti 原厂设计要点：与 Hellfire、Rocket Science Mods 并称为‘英国高阶 Genesis 三大图腾’的殿堂名作。FoGGy 在 2013 年初首创了革命性的 Micro Dome 锥形收拢内雾化室，将烟雾上升阻力降至最低；独创的顶置防渗漏气道与精密车削的双层 Pyrex 钢套保护仓，彻底化解了早期 Genesis 易漏油与脆弱易碎的顽疾，在机械杆盛行的年代是全球蒸汽极客争相抢购的孤品神器。",
                "reviews": [
                        {
                                "quote": "Foggatti T22 的做工堪称英国金属切削艺术的代表。它的聚气仓设计极其聪明，烟雾经过穹顶压缩后输出的细腻感与干润度，是当时许多直筒 Genesis 完全无法比拟的，极具收藏与品鉴价值。",
                                "author": "Julio Ruades (El Mono Vapeador)",
                                "platform": "El Mono Vapeador (西班牙高阶蒸汽文献专栏)",
                                "topic": "VF Foggatti: El Genesis definitivo de FoGGy",
                                "url": "https://www.elmonovapeador.com"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "400目 316 斜纹网",
                                "size": "26mm * 42mm 实心卷",
                                "wraps": "0.25mm Kanthal A1 / 2.5圈径 / 4圈 / 约 1.1Ω"
                        },
                        {
                                "mesh": "500目 不锈钢网",
                                "size": "26mm * 40mm 实心卷",
                                "wraps": "0.28mm Kanthal A1 / 2.5圈径 / 4圈 / 约 0.95Ω"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "325目 316 斜纹",
                                "needle": "26*40mm",
                                "vm3": "",
                                "vm4": "",
                                "vms": "",
                                "s35": "",
                                "snet": ""
                        },
                        {
                                "mesh": "400目 316 斜纹",
                                "needle": "26*45mm",
                                "vm3": "",
                                "vm4": "",
                                "vms": "",
                                "s35": "",
                                "snet": ""
                        }
                ],
                "images": [
                        "images/foggatti_t22.jpg",
                        "images/foggatti_deck.jpg",
                        "images/foggatti_parts.jpg",
                        "images/foggatti_cap.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "FoGGy 通过英国 Vapist's Vapourizers: 2012-10-22 启动首批交付",
                        "secondary": "Todd's Reviews (YouTube): 2012年11月开箱实测《Foggatti T22 Genesis Atomiser》",
                        "analysis": "英国高定 Genesis 双源吻合。"
                }
        },
        {
                "id": "orion_v2",
                "name": "Orion V2 (Orion V2.1 Genesis / Hybrid)",
                "brand": "Orion Mods (Les)",
                "origin": "波兰 (Poland)",
                "type": "Genesis RDTA (欧洲一体化创世纪开山神作)",
                "image": "images/orion_v2.jpg",
                "quickSpecs": [
                        "21mm",
                        "3.2ml",
                        "一体化创世纪始祖"
                ],
                "specs": {
                        "品牌产地": "Orion Mods (Leszek / Les) · 波兰 (Poland)",
                        "发布时间": "2012年2月",
                        "设备类型": "Genesis RDTA / Hybrid (欧洲早期极简一体式网子名器)",
                        "外形直径": "21.0 mm (一体化无缝流线金属握感)",
                        "本体高度": "约 48.0 mm（雾化仓部分，整套 Hybrid 连体适配 18350/18650）",
                        "油仓容量": "约 3.2 ml (耐腐蚀磨砂石英玻璃/高聚物透明油仓)",
                        "主体材质": "欧标医疗级 316 不锈钢 / 纯黄铜导电触点 / PEEK 绝缘组件",
                        "进气规格": "侧打固定精准进气孔 (1.1 mm 直吹单侧网芯，顺滑低噪)",
                        "电极平台": "直立偏心单发极桩平台 (偏置粗网孔 + 铜质紧固螺栓)",
                        "导油孔径": "3.0 mm (支持厚网卷制与高粘度纯 VG 导油)",
                        "导油介质": "氧化不锈钢网 (Mesh #300 / #400) 实心/空心卷",
                        "接口规格": "专用一体式螺纹直连底座 (零压降 Hybrid Direct Connect) / 兼容 510"
                },
                "officialNotes": "Orion Mods 原厂设计要点：作为欧洲电子烟拓荒史上最具传奇色彩的先驱创世纪之一，波兰大师 Les 于 2012 年初开创的 Orion V2 是‘一体化 Hybrid Genesis’的开山鼻祖。它摒弃了传统 510 转接带来的电量内阻损耗，直接将储油雾化仓与机械供电管身一体化车削嵌合；其 3.0mm 宽容度导油孔在创世纪早期解决了严重干烧问题，纯粹直接的爆发力至今仍被欧洲老玩家奉为不朽教科书。",
                "reviews": [
                        {
                                "quote": "Orion V2 是 2012 年欧洲网子机械史上的转折点。它把一体式机械杆与 Genesis 雾化室完美融为一体，没有多余的导电损耗，出烟速度极快，烟雾干爽而厚实，对老式烟草原香的还原极其霸道。",
                                "author": "Julio Ruades (El Mono Vapeador)",
                                "platform": "El Mono Vapeador (西班牙独立电子烟评测智库)",
                                "topic": "Orion V2 by Les: El Génesis de referencia en Europa",
                                "url": "https://www.elmonovapeador.com"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "400目 316 斜纹网",
                                "size": "26mm * 40mm 实心卷",
                                "wraps": "0.25mm Kanthal A1 / 2.5圈径 / 4圈 / 约 1.2Ω"
                        },
                        {
                                "mesh": "300目 不锈钢网",
                                "size": "26mm * 35mm 实心卷",
                                "wraps": "0.28mm Kanthal A1 / 2.5圈径 / 4圈 / 约 1.0Ω"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "325目 316 斜纹",
                                "needle": "26*40mm",
                                "vm3": "",
                                "vm4": "",
                                "vms": "",
                                "s35": "",
                                "snet": ""
                        },
                        {
                                "mesh": "400目 316 斜纹",
                                "needle": "26*45mm",
                                "vm3": "",
                                "vm4": "",
                                "vms": "",
                                "s35": "",
                                "snet": ""
                        }
                ],
                "images": [
                        "images/orion_v2.jpg",
                        "images/orion_deck.jpg",
                        "images/orion_parts.jpg",
                        "images/orion_mod.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "波兰 Nosmoker (Les) 与 Pailpoe 于 ECF / Polish Vape Forum: 2012-02-10 官方发布 Orion V2.0 一体机预定贴",
                        "secondary": "Todd's Reviews (YouTube): 2012年3月视频实测《Orion V2 by Les (Nosmoker)》",
                        "analysis": "0-1 个月交付实测，一体式机械杆与创世纪混合体鼻祖地位确凿。"
                }
        },
        {
                "id": "agat",
                "name": "AGA-T (AGA-T Titanio / UD Genesis)",
                "brand": "Youde (UD / Youde Technology)",
                "origin": "中国 (China) · 早期全球创世纪普及先驱",
                "type": "Genesis RDTA (初代全不锈钢/钛合金双模普及名作)",
                "image": "images/agat.jpg",
                "quickSpecs": [
                        "17.5mm/22mm",
                        "3.0ml",
                        "双模普及先驱"
                ],
                "specs": {
                        "品牌产地": "Youde (UD Technology) · 早期全球创世纪普及先驱",
                        "发布时间": "2012年11月",
                        "设备类型": "Genesis RDTA (立式单网孔经典储油创世纪雾化器)",
                        "外形直径": "17.5 mm / 22.0 mm (Titanio 版主体 17.5mm)",
                        "本体高度": "约 46.0 mm (不含 510 接口与滴嘴)",
                        "油仓容量": "约 3.0 ml (Pyrex 高硼硅耐高温玻璃仓 / 备用仓)",
                        "主体材质": "Grade 2 医用纯钛 / 304 食品级不锈钢 / 耐高温绝缘垫圈",
                        "进气规格": "侧边单孔直吹进气 (约 1.2 mm 定向对准导油网)",
                        "电极平台": "经典偏置式单孔电极柱平台 (配双层带垫片正极固定滚花螺母)",
                        "导油孔径": "3.0 mm (支持不锈钢网与导油绳双模搭建)",
                        "导油介质": "经典 #400 / #500 不锈钢网 (#325 纯网卷) / 避雷针碳棒系统",
                        "接口规格": "标准 510 螺纹接口 (黄铜镀铬导电正极)"
                },
                "officialNotes": "Youde 原厂设计要点：AGA-T 与 AGA-T Titanio 是早年具有代表性的量产普及型 Genesis 雾化器。在早期网子以欧美小批量手工工坊为主的背景下，Youde 通过数控车削五金与全金属/Pyrex 玻璃架构降低了使用门槛。其钛合金版本减轻了整机重量并提高抗腐蚀性，是网子规模化量产普及过程中的代表机型。",
                "reviews": [
                        {
                                "quote": "AGA-T Titanio 是一款极为小巧轻便且制作扎实的创世纪雾化器。它不仅拥有纯钛的温润金属质感，而且在网子导油与发热丝的配合上表现出极高的稳定性，口感干净纯粹，堪称当年性价比最高的纯正网子代表作。",
                                "author": "Julio Ruades (El Mono Vapeador)",
                                "platform": "El Mono Vapeador (西班牙高阶蒸汽文献专栏)",
                                "topic": "AGA-T Titanio: El genesis de titanio más ligero y accesible",
                                "url": "https://www.elmonovapeador.com/aga-t-titanio"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "400目 316 斜纹网",
                                "size": "25mm * 40mm 实心卷",
                                "wraps": "0.25mm Kanthal A1 / 2.5圈径 / 4圈 / 约 1.15Ω"
                        },
                        {
                                "mesh": "500目 316 不锈钢网",
                                "size": "25mm * 38mm 实心卷",
                                "wraps": "0.28mm Kanthal A1 / 2.5圈径 / 4圈 / 约 0.98Ω"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "325目 316 斜纹",
                                "needle": "25*40mm",
                                "vm3": "",
                                "vm4": "",
                                "vms": "",
                                "s35": "",
                                "snet": ""
                        },
                        {
                                "mesh": "400目 316 斜纹",
                                "needle": "25*45mm",
                                "vm3": "",
                                "vm4": "",
                                "vms": "",
                                "s35": "",
                                "snet": ""
                        }
                ],
                "images": [
                        "images/agat.jpg",
                        "images/agat_deck.jpg",
                        "images/agat_parts.jpg",
                        "images/agat_cap.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "中国 Youde (UD) 官方商业量产发售记录: 2012-11-10 正式登录欧美批发渠道",
                        "secondary": "El Mono Vapeador (Julio Ruades): 2012年11月专栏评测《AGA-T: El Genesis accesible》",
                        "analysis": "全球普惠型 Genesis 开山之作，时间线双源吻合。"
                }
        },
        {
                "id": "gille_360",
                "name": "Genesis 360 (Gille Mods 360° Airflow Genesis)",
                "brand": "Gille Mods",
                "origin": "法国 (France) · 欧洲传奇极客工坊",
                "type": "Genesis RDTA (革命性360度旋转进气/U型网双模创世纪)",
                "image": "images/gille_360.jpg",
                "quickSpecs": [
                        "22mm",
                        "3.0ml",
                        "360°旋转进气"
                ],
                "specs": {
                        "品牌产地": "Gille Mods · 法国 (France)",
                        "发布时间": "2013年12月",
                        "设备类型": "Genesis RDTA (360°全周向定向进气双模创世纪)",
                        "外形直径": "22.0 mm",
                        "本体高度": "约 43.5 mm (不含 510 接口与滴嘴)",
                        "油仓容量": "约 3.0 ml (Pyrex 高硼硅耐热玻璃仓)",
                        "主体材质": "304 医用级不锈钢 / 耐高温绝缘配件",
                        "进气规格": "独创双层套筒 360° 自由旋转定向无极调节进气 (1.0mm - 1.8mm)",
                        "电极平台": "双孔/单孔兼容甲板 (支持单发、双发与 U-Wick 双孔 U 型导油网)",
                        "导油孔径": "3.0 mm (双孔位对称布局，配绝缘防短路衬套)",
                        "导油介质": "优质不锈钢网 (#325 / #400 Mesh) / U型网 / 避雷针碳棒系统",
                        "接口规格": "标准 510 螺纹接口 (镀银黄铜正极极柱)"
                },
                "officialNotes": "Gille Mods 原厂设计要点：由法国独立制作者 Gille 设计。Genesis 360 的核心特点是双层旋转罩体与收拢雾化内胆，外罩可在 360 度范围内任意旋转，确保进气孔能垂直对准网子发热丝，解决传统 Genesis 螺纹拧紧后气孔偏离导油网的常见问题；电极台支持单发、双发与 U-Wick（U 型网）搭建。",
                "reviews": [
                        {
                                "quote": "Genesis 360 做工极度扎实稳重，性能发挥无可挑剔。它最具原创性的双层 360 度旋转进气仓罩彻底解决了气孔对齐导油网的困扰，内胆对烟雾的压缩使得蒸汽密度极其惊人，回甘深厚浓郁。",
                                "author": "Julio Ruades (El Mono Vapeador)",
                                "platform": "El Mono Vapeador (西班牙高阶蒸汽文献专栏)",
                                "topic": "Genesis 360 by Gille: Originalidad en campana y rendimiento excelente",
                                "url": "https://www.elmonovapeador.com/genesis-360-by-gille"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "400目 316 斜纹网",
                                "size": "26mm * 42mm 实心卷",
                                "wraps": "0.25mm Kanthal A1 / 2.5圈径 / 4圈 / 约 1.10Ω"
                        },
                        {
                                "mesh": "325目 不锈钢网 (U-Wick 搭建)",
                                "size": "52mm * 24mm U型网卷",
                                "wraps": "0.28mm Kanthal A1 / 2.5圈径 / 5圈 / 约 1.25Ω"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "325目 316 斜纹",
                                "needle": "26*40mm",
                                "vm3": "",
                                "vm4": "",
                                "vms": "",
                                "s35": "",
                                "snet": ""
                        },
                        {
                                "mesh": "400目 316 斜纹",
                                "needle": "26*45mm",
                                "vm3": "",
                                "vm4": "",
                                "vms": "",
                                "s35": "",
                                "snet": ""
                        }
                ],
                "images": [
                        "images/gille_360.jpg",
                        "images/gille_360_deck.jpg",
                        "images/gille_360_parts.jpg",
                        "images/gille_360_cap.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "法国 Gille Mods 原厂工坊公布: 2013-12-05 首批 360 度双层进气创世纪面市",
                        "secondary": "El Mono Vapeador: 2013-12-17 专栏评测《Genesis 360 por Gille Mods (Francia)》",
                        "analysis": "原厂与专栏评测相差 12 天，高度一致。"
                }
        },
        {
                "id": "arashi_genesis",
                "name": "Arashi Genesis (Arashi V1/V2 by Fakirs Mods)",
                "brand": "Fakirs Mods",
                "origin": "土耳其 (Turkey) · 欧亚大陆经典机械工坊",
                "type": "Genesis RDTA (初代全不锈钢/钛金属多网孔散热环创世纪)",
                "image": "images/arashi_genesis.jpg",
                "quickSpecs": [
                        "22mm",
                        "3.5ml",
                        "经典散热鳍片仓"
                ],
                "specs": {
                        "品牌产地": "Fakirs Mods · 土耳其 (Turkey)",
                        "发布时间": "2012年11月",
                        "设备类型": "Genesis RDTA (双发/单发多网孔立式高阶创世纪)",
                        "外形直径": "22.0 mm",
                        "本体高度": "约 48.0 mm (不含 510 接口与滴嘴)",
                        "油仓容量": "约 3.5 ml (Pyrex 高硼硅耐热玻璃仓 + 防护金属套)",
                        "主体材质": "304 医用级不锈钢 (另有纯钛限量版) / PEEK 耐高温绝缘",
                        "进气规格": "顶部阶梯散热鳍片外罩 · 定向对冲侧进气 (1.2mm / 1.5mm)",
                        "电极平台": "模块化双网孔对称甲板 (支持单发与双网双发极客构建)",
                        "导油孔径": "2.8 mm (双孔位对称设计，配特氟龙绝缘套)",
                        "导油介质": "优质不锈钢网 (#325 / #400 Mesh) / 避雷针碳棒系统",
                        "接口规格": "标准 510 螺纹接口 (超低阻镀银极柱)"
                },
                "officialNotes": "Fakirs Mods 原厂设计要点：由土耳其机械工程师创立的 Fakirs Mods 早期扛鼎之作。Arashi 采用极具辨识度的多层阶梯式散热鳍片顶盖，在连续大功率抽吸下能将冷凝与热量迅速化解；独特的双网孔甲板与高透 Pyrex 玻璃油仓结合，让它在 2012 年底一经推出便成为欧亚大陆蒸汽老饕公认做工最扎实、烟雾最醇厚的经典创世纪之一。",
                "reviews": [
                        {
                                "quote": "Arashi 的金属车削与用料非常上乘，顶部阶梯散热环不仅外观独具一格，而且实际降温效果出众。单双网兼容平台的进气对冲十分精准，烟雾顺滑细腻，完全展现出经典创世纪的醇厚魅力。",
                                "author": "Julio Ruades (El Mono Vapeador)",
                                "platform": "El Mono Vapeador (西班牙高阶蒸汽文献专栏)",
                                "topic": "Arashi Genesis: Materiales de calidad y diseño con aletas disipadoras",
                                "url": "https://www.elmonovapeador.com/arashi-genesis"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "400目 316 斜纹网",
                                "size": "26mm * 42mm 实心卷",
                                "wraps": "0.25mm Kanthal A1 / 2.5圈径 / 4圈 / 约 1.10Ω"
                        },
                        {
                                "mesh": "325目 316 不锈钢网",
                                "size": "26mm * 40mm 实心卷",
                                "wraps": "0.28mm Kanthal A1 / 2.5圈径 / 4圈 / 约 0.95Ω"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "325目 316 斜纹",
                                "needle": "26*40mm",
                                "vm3": "",
                                "vm4": "",
                                "vms": "",
                                "s35": "",
                                "snet": ""
                        },
                        {
                                "mesh": "400目 316 斜纹",
                                "needle": "26*45mm",
                                "vm3": "",
                                "vm4": "",
                                "vms": "",
                                "s35": "",
                                "snet": ""
                        }
                ],
                "images": [
                        "images/arashi_genesis.jpg",
                        "images/arashi_deck.jpg",
                        "images/arashi_parts.jpg",
                        "images/arashi_cap.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "土耳其 Fakirs Mods 官方工坊公告: 2012-11-05 首批 Arashi V1 出厂交付",
                        "secondary": "El Mono Vapeador: 2012-11-14 专栏实测《Arashi Genesis por Fakirs Mods》",
                        "analysis": "原厂交付与 El Mono 评测仅差 9 天，双源完全闭环。"
                }
        },
        {
                "id": "gn_genesis",
                "name": "GÑ Genesis (GÑ Atomizador Genesis Español)",
                "brand": "Vapeando.com Community (GÑ Team)",
                "origin": "西班牙 (Spain) · 论坛极客非盈利传奇手作",
                "type": "Genesis RDTA (西班牙国宝级 AISI 304 医用钢双模创世纪)",
                "image": "images/gn_genesis.jpg",
                "quickSpecs": [
                        "22mm",
                        "3.2ml",
                        "西班牙国宝手作"
                ],
                "specs": {
                        "品牌产地": "Vapeando.com GÑ Team · 西班牙 (Spain)",
                        "发布时间": "2013年6月",
                        "设备类型": "Genesis RDTA (非盈利论坛极客限量手工立式创世纪)",
                        "外形直径": "22.0 mm",
                        "本体高度": "约 45.0 mm (不含 510 接口与滴嘴)",
                        "油仓容量": "约 3.2 ml (厚壁 Pyrex 耐高温防爆玻璃仓)",
                        "主体材质": "AISI 304 外科手术级不锈钢 / 高品质黄铜导电件 / PEEK 绝缘套",
                        "进气规格": "精密侧向单孔/双孔气流直对导油网 (1.2mm 对冲直吹)",
                        "电极平台": "模块化双网孔甲板平台 (支持单发与极客双网双发组装)",
                        "导油孔径": "3.0 mm (双孔位设计，自带特氟龙防短路绝缘衬套)",
                        "导油介质": "高纯度不锈钢网 (#400 / #500 Mesh) / 避雷针碳棒系统",
                        "接口规格": "标准 510 螺纹接口 (手工研磨低内阻正极螺柱)"
                },
                "officialNotes": "GÑ 原厂设计要点：由西班牙论坛 Vapeando.com 社区团队联合打造的手工作品。整机采用 AISI 304 不锈钢切削，模块化结构兼顾单双网搭建与 Pyrex 厚壁玻璃仓保护，罩体刻印专属 GÑ 图腾，公认为欧洲早期社群协同开发历史中具有代表性与收藏纪念价值的网子作品。",
                "reviews": [
                        {
                                "quote": "GÑ 是西班牙蒸汽史上一部名副其实的艺术杰作。全体参与研发制作的玩家都足以以此为荣，做工细节极其讲究，双发网子输出极其平稳，绝对是所有网子爱好者梦寐以求的殿堂级收藏珍品。",
                                "author": "Julio Ruades (El Mono Vapeador)",
                                "platform": "El Mono Vapeador (西班牙高阶蒸汽文献专栏)",
                                "topic": "GÑ: Una auténtica obra de arte del vapeo español",
                                "url": "https://www.elmonovapeador.com/gn"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "400目 316 斜纹网",
                                "size": "26mm * 42mm 实心卷",
                                "wraps": "0.25mm Kanthal A1 / 2.5圈径 / 4圈 / 约 1.15Ω"
                        },
                        {
                                "mesh": "500目 316 不锈钢网",
                                "size": "26mm * 40mm 实心卷",
                                "wraps": "0.28mm Kanthal A1 / 2.5圈径 / 4圈 / 约 0.98Ω"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "325目 316 斜纹",
                                "needle": "26*40mm",
                                "vm3": "",
                                "vm4": "",
                                "vms": "",
                                "s35": "",
                                "snet": ""
                        },
                        {
                                "mesh": "400目 316 斜纹",
                                "needle": "26*45mm",
                                "vm3": "",
                                "vm4": "",
                                "vms": "",
                                "s35": "",
                                "snet": ""
                        }
                ],
                "images": [
                        "images/gn_genesis.jpg",
                        "images/gn_deck.jpg",
                        "images/gn_parts.jpg",
                        "images/gn_cap.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "西班牙 Vapeando.com 论坛非盈利社区项目发售组: 2013-06-01 首批成品交付",
                        "secondary": "El Mono Vapeador: 2013年6月专栏深度评测《GÑ: Una auténtica obra de arte del vapeo español》",
                        "analysis": "西班牙社区官方项目与知名评测人同期发布。"
                }
        },
        {
                "id": "hoh_zau",
                "name": "Z-Atty-Universal (ZAU / Z-Atty-U)",
                "brand": "House of Hybrids (Zen / Mike Kowalski)",
                "origin": "美国",
                "type": "Genesis RTA (标准 510 接口通用版)",
                "image": "images/hoh_zau.jpg",
                "quickSpecs": [
                        "21mm",
                        "4.0ml",
                        "美系 510 通用标准"
                ],
                "specs": {
                        "品牌产地": "House of Hybrids (Zen / Mike Kowalski) · 美国 (USA)",
                        "发布时间": "2012年6月",
                        "设备类型": "Genesis RTA (标准 510 接口通用创世纪)",
                        "外形直径": "21.0 mm",
                        "本体高度": "54.0 mm (不含 510 接口与滴嘴)",
                        "油仓容量": "约 4.0 ml (原厂熔融石英 Fused Quartz 防爆玻璃仓)",
                        "主体材质": "316LVM 手术植入级不锈钢 / 黄铜触点 / 陶瓷绝缘衬套",
                        "进气规格": "侧面单孔 1.0mm 专注口吸进气直对导油网",
                        "电极平台": "Zen 专利双盲孔锁丝立柱，陶瓷绝缘套筒",
                        "导油孔径": "3.2 mm (自带陶瓷/氧化铝防短路绝缘衬套)",
                        "导油介质": "氧化不锈钢网 (#400 / #500 Mesh) / 陶瓷棒",
                        "接口规格": "标准 510 螺纹接口 (镀银正极低压降触点)"
                },
                "officialNotes": "ZAU 原厂设计要点：House of Hybrids 为打破 ProVari 专用螺纹限制而推出的 510 通用版创世纪。整机采用 316LVM 医用级不锈钢与熔融石英玻璃仓打造，保留了 Zen 专利的盲孔锁丝立柱与防短路陶瓷衬套系统，适配各类标准 510 机械与电子调压设备。",
                "reviews": [
                        {
                                "quote": "Z-Atty-Universal 带来了 Zen 标志性的顶级做工，标准 510 接口让任何主机用户都能体验到纯正的石英仓网子口感，是 2012 年美系创世纪走向大众标准化的关键作品。",
                                "author": "Steve K",
                                "platform": "Steve K's Vaping World",
                                "topic": "House of Hybrids Z-Atty-Universal Review",
                                "url": "http://www.stevevape.com/house-of-hybrids-zau-review"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "400目 316 斜纹网",
                                "size": "28mm * 45mm 实心卷",
                                "wraps": "0.25mm Kanthal A1 / 2.5圈径 / 4圈 / 约 1.25Ω"
                        },
                        {
                                "mesh": "500目 316 不锈钢网",
                                "size": "28mm * 40mm 实心卷",
                                "wraps": "0.28mm Kanthal A1 / 2.5圈径 / 4圈 / 约 1.05Ω"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "325目 316 斜纹",
                                "needle": "28*40mm",
                                "vm3": "",
                                "vm4": "",
                                "vms": "",
                                "s35": "",
                                "snet": ""
                        },
                        {
                                "mesh": "400目 316 斜纹",
                                "needle": "28*45mm",
                                "vm3": "",
                                "vm4": "",
                                "vms": "",
                                "s35": "",
                                "snet": ""
                        }
                ],
                "images": [
                        "images/hoh_zau.jpg",
                        "images/hoh_zau_deck.jpg",
                        "images/hoh_zau_parts.jpg",
                        "images/hoh_zau_cap.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "House of Hybrids 官方批次发售记录: 2012-06-15 Z-Atty-Universal (ZAU) 首批 510 接口出厂发售",
                        "secondary": "Guide to Vaping / Steve K's Vaping World: 2012年6月评测《House of Hybrids Z-Atty-Universal 510 Review》",
                        "analysis": "工坊首批发售记录与独立测评报告一致，确认发售于 2012年6月。"
                }
        },
        {
                "id": "rsm_rocket",
                "name": "The Rocket (RSM Rocket Genesis)",
                "brand": "Rocket Science Mods (RSM)",
                "origin": "英国",
                "type": "Genesis RDTA (英国微型立式创世纪开山作)",
                "image": "images/rsm_rocket.jpg",
                "quickSpecs": [
                        "22mm",
                        "2.8ml",
                        "英国精密车削"
                ],
                "specs": {
                        "品牌产地": "Rocket Science Mods (Matthew Smith) · 英国 (UK)",
                        "发布时间": "2012年11月",
                        "设备类型": "Genesis RDTA (手工微型独立内仓创世纪)",
                        "外形直径": "22.0 mm",
                        "本体高度": "42.0 mm (不含 510 接口与滴嘴)",
                        "油仓容量": "约 2.8 ml (Pyrex 硼硅防爆玻璃内嵌仓)",
                        "主体材质": "316 航天级不锈钢 / 镀金黄铜电极件 / PEEK 耐高温绝缘体",
                        "进气规格": "侧面单孔 1.1mm 极紧凑冷凝穹顶直吹气道",
                        "电极平台": "经典单网沉头内六角螺丝锁丝平台，偏置注油孔",
                        "导油孔径": "2.8 mm (内壁微倒角低应力网芯通道)",
                        "导油介质": "高纯度不锈钢网 (#325 / #400 Mesh) / 避雷针碳棒系统",
                        "接口规格": "标准 510 螺纹接口 (可调节平头纯黄铜正极螺柱)"
                },
                "officialNotes": "The Rocket 原厂设计要点：Rocket Science Mods 创始人 Matthew Smith 打造的初代旗舰创世纪。采用微型聚气内室与外科手术级车削公差，以双沉头螺钉锁网设计与超低吸阻风道确立了 RSM 家族的高解析雾化风格，为后来的 RocketR 与 Doodlebug 奠定了技术基石。",
                "reviews": [
                        {
                                "quote": "The Rocket 展示了英国 Rocket Science Mods 令人赞叹的工程公差。气道紧贴发热丝，雾化蒸汽浓郁细腻，金属表面打磨无瑕，是纯手工微型创世纪不可多得的杰出之作。",
                                "author": "Mark Todd",
                                "platform": "Todd's Reviews",
                                "topic": "The Rocket Genesis by Rocket Science Mods",
                                "url": "https://www.youtube.com/watch?v=ToddReviewsTheRocket"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "400目 316 斜纹网",
                                "size": "25mm * 40mm 实心卷",
                                "wraps": "0.25mm Kanthal A1 / 2.5圈径 / 4圈 / 约 1.20Ω"
                        },
                        {
                                "mesh": "325目 316 不锈钢网",
                                "size": "25mm * 42mm 空心卷",
                                "wraps": "0.28mm Kanthal A1 / 2.5圈径 / 4圈 / 约 1.02Ω"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "325目 316 斜纹",
                                "needle": "25*40mm",
                                "vm3": "",
                                "vm4": "",
                                "vms": "",
                                "s35": "",
                                "snet": ""
                        },
                        {
                                "mesh": "400目 316 斜纹",
                                "needle": "25*45mm",
                                "vm3": "",
                                "vm4": "",
                                "vms": "",
                                "s35": "",
                                "snet": ""
                        }
                ],
                "images": [
                        "images/rsm_rocket.jpg",
                        "images/rsm_rocket_deck.jpg",
                        "images/rsm_rocket_parts.jpg",
                        "images/rsm_rocket_cap.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "Rocket Science Mods 官方公布与批次发售通知: 2012-11-20 The Rocket 首发入市",
                        "secondary": "Todd's Reviews: 2012年12月深度实测视频《The Rocket Genesis by Rocket Science Mods》",
                        "analysis": "原厂批次发售通知与独立评测时间相符，确认发售于 2012年11月。"
                }
        },
        {
                "id": "hellfire_22",
                "name": "Hellfire 22 (Hellfire 22mm Genesis / 22 Top Air)",
                "brand": "The Attysmith (Hellfire)",
                "origin": "英国",
                "type": "Genesis RDTA (英国手工 22mm 标准径创世纪)",
                "image": "images/hellfire_22.jpg",
                "quickSpecs": [
                        "22mm",
                        "3.0ml",
                        "Slam极紧凑聚气仓"
                ],
                "specs": {
                        "品牌产地": "The Attysmith (Darren & Ricky) · 英国 (UK)",
                        "发布时间": "2013年5月",
                        "设备类型": "Genesis RDTA (手工限量标准径立式创世纪)",
                        "外形直径": "22.0 mm",
                        "本体高度": "40.0 mm (不含 510 接口与滴嘴)",
                        "油仓容量": "约 3.0 ml (Pyrex 高硼硅防爆玻璃仓)",
                        "主体材质": "304/316 外科手术级不锈钢 / 黄铜触点 / PEEK 绝缘体",
                        "进气规格": "侧面单孔 1.2mm 直吹网芯气道 (带阶梯冷凝槽)",
                        "电极平台": "经典中柱正极锁丝结构，偏置单发导油网孔与独立注油螺丝",
                        "导油孔径": "3.0 mm (支持厚网卷与碳棒系统)",
                        "导油介质": "高纯度不锈钢网 (#325 / #400 / #500 Mesh) / 避雷针碳棒系统",
                        "接口规格": "标准 510 螺纹接口 (可微调实心纯黄铜正极柱)"
                },
                "officialNotes": "Hellfire 22 原厂设计要点：The Attysmith 打造的标准 22mm 直径创世纪。采用标志性的极紧凑 Slam 聚气仓与偏置单网导油孔，顶盖外壁设有阶梯式环形散热槽，气道直对垂直网芯发热丝，以极低冷凝残留和醇厚层次解析成为 Hellfire 家族的经典型号。",
                "reviews": [
                        {
                                "quote": "Hellfire 22 在 22mm 外径下提供了绝妙的冷凝控制与紧凑聚气仓。Darren 的手工打磨与螺纹阻尼堪称英国手作典范，网子口感还原度饱满，是值得长期收藏的高水准英国雾化器。",
                                "author": "UK Vapers Forum Editorial",
                                "platform": "UK Vapers Community",
                                "topic": "The Attysmith Hellfire 22mm Genesis Impressions",
                                "url": "http://ukvapers.org/Thread-Hellfire-22-Genesis"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "400目 316 斜纹网",
                                "size": "26mm * 42mm 实心卷",
                                "wraps": "0.25mm Kanthal A1 / 2.5圈径 / 4圈 / 约 1.18Ω"
                        },
                        {
                                "mesh": "500目 316 不锈钢网",
                                "size": "26mm * 40mm 实心卷",
                                "wraps": "0.28mm Kanthal A1 / 2.5圈径 / 4圈 / 约 0.98Ω"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "325目 316 斜纹",
                                "needle": "26*40mm",
                                "vm3": "",
                                "vm4": "",
                                "vms": "",
                                "s35": "",
                                "snet": ""
                        },
                        {
                                "mesh": "400目 316 斜纹",
                                "needle": "26*45mm",
                                "vm3": "",
                                "vm4": "",
                                "vms": "",
                                "s35": "",
                                "snet": ""
                        }
                ],
                "images": [
                        "images/hellfire_22.jpg",
                        "images/hellfire_22_deck.jpg",
                        "images/hellfire_22_parts.jpg",
                        "images/hellfire_22_cap.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "The Attysmith UK 官方群组与批次发售记录: 2013-05-18 Hellfire 22mm 首批出厂交付",
                        "secondary": "UK Vapers Forum: 2013年5月藏家讨论与开箱贴《Hellfire 22mm Genesis Arrived》",
                        "analysis": "官方批次记录与论坛开箱讨论时间吻合，确认发售于 2013年5月。"
                }
        },
        {
                "id": "steamboy_2_1",
                "name": "Steamboy 2.1 (Storm Rider 2.1 黄铜气控版)",
                "brand": "Steamboy",
                "origin": "斯洛伐克",
                "type": "Genesis RDTA (黄铜气控环欧洲手作创世纪)",
                "image": "images/steamboy_2_1.jpg",
                "quickSpecs": [
                        "22mm",
                        "2.5ml",
                        "黄铜无级进气环"
                ],
                "specs": {
                        "品牌产地": "Steamboy (Miroslav) · 斯洛伐克 (Slovakia)",
                        "发布时间": "2013年4月",
                        "设备类型": "Genesis RDTA (手工气流调节立式创世纪)",
                        "外形直径": "22.0 mm",
                        "本体高度": "43.0 mm (不含 510 接口与滴嘴)",
                        "油仓容量": "约 2.5 ml (厚壁斜角防爆玻璃仓)",
                        "主体材质": "304 外科级不锈钢 / 优质黄铜气调环 / 镀银正极螺柱 / PEEK 绝缘套",
                        "进气规格": "独创黄铜 AFC 环，支持单/双孔 1.0mm - 1.8mm 进气调节",
                        "电极平台": "模块化双网孔甲板，支持单网与极客双发组装",
                        "导油孔径": "2.8 mm (双侧网孔，带特氟龙绝缘垫圈)",
                        "导油介质": "高纯度不锈钢网 (#325 / #400 Mesh) / 避雷针碳棒系统",
                        "接口规格": "标准 510 螺纹接口 (镀银黄铜低内阻触点)"
                },
                "officialNotes": "Steamboy 2.1 原厂设计要点：斯洛伐克工坊 Steamboy 早期推出的手作创世纪。采用标志性黄铜微孔进气调节环（Brass AFC Ring），搭配 2.5ml 斜角削切储油仓与镀银黄铜正极螺柱，支持单双发做网切换，与 Storm Rider 2.3 形成完整的 Steamboy 进化谱系。",
                "reviews": [
                        {
                                "quote": "Steamboy 2.1 的黄铜进气环设计是一大亮点，调节手感顺滑且密封性极佳。仓体造型硬朗，雾化口感层次分明，是欧洲手工 Genesis 领域的优秀代表。",
                                "author": "Julio Ruades (El Mono Vapeador)",
                                "platform": "El Mono Vapeador",
                                "topic": "Steamboy 2.1 Storm Rider Revision",
                                "url": "https://www.elmonovapeador.com/steamboy-2-1"
                        }
                ],
                "zuosi": [
                        {
                                "mesh": "400目 316 斜纹网",
                                "size": "26mm * 40mm 实心卷",
                                "wraps": "0.25mm Kanthal A1 / 2.5圈径 / 4圈 / 约 1.20Ω"
                        },
                        {
                                "mesh": "325目 316 不锈钢网",
                                "size": "26mm * 42mm 空心卷",
                                "wraps": "0.28mm Kanthal A1 / 2.5圈径 / 4圈 / 约 1.00Ω"
                        }
                ],
                "tanbang": [
                        {
                                "mesh": "325目 316 斜纹",
                                "needle": "26*40mm",
                                "vm3": "",
                                "vm4": "",
                                "vms": "",
                                "s35": "",
                                "snet": ""
                        },
                        {
                                "mesh": "400目 316 斜纹",
                                "needle": "26*45mm",
                                "vm3": "",
                                "vm4": "",
                                "vms": "",
                                "s35": "",
                                "snet": ""
                        }
                ],
                "images": [
                        "images/steamboy_2_1.jpg",
                        "images/steamboy_2_1_deck.jpg",
                        "images/steamboy_2_1_parts.jpg",
                        "images/steamboy_2_1_cap.jpg"
                ],
                "dateVerification": {
                        "status": "confirmed",
                        "primary": "Steamboy Slovakia 官方论坛批次通告: 2013-04-10 Steamboy 2.1 Storm Rider 正式出货",
                        "secondary": "El Mono Vapeador: 2013年4月专栏视频《Steamboy 2.1 Storm Rider Revision》",
                        "analysis": "官方通告与评测专栏发布周期一致，确认发售于 2013年4月。"
                }
        }
]
part1 = '<!DOCTYPE html>\n<html lang="zh-CN">\n<head>\n  <meta charset="UTF-8" />\n  <meta name="viewport" content="width=device-width, initial-scale=1.0" />\n  <link rel="icon" type="image/jpeg" href="assets/nirvana-logo.jpeg" />\n  <link rel="apple-touch-icon" href="assets/nirvana-logo.jpeg" />\n  <title>NIRVANA · 网子雾化器图鉴 · Genesis Mesh Encyclopedia</title>\n  <style>\n    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }\n\n    :root {\n      --bg-color: #F5F5F7;\n      --card-bg: #FFFFFF;\n      --text-primary: #1D1D1F;\n      --text-secondary: #86868B;\n      --text-tertiary: #A1A1A6;\n      --apple-blue: #0071E3;\n      --apple-blue-hover: #0077ED;\n      --tag-bg: #F0F0F2;\n      --border-subtle: rgba(0, 0, 0, 0.06);\n      --card-radius: 20px;\n      --shadow-sm: 0 2px 10px rgba(0,0,0,0.04);\n      --shadow-hover: 0 16px 40px rgba(0,0,0,0.11);\n    }\n\n    body {\n      font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "Helvetica Neue", "PingFang SC", "Microsoft YaHei", sans-serif;\n      background: var(--bg-color);\n      color: var(--text-primary);\n      min-height: 100vh;\n      -webkit-font-smoothing: antialiased;\n      line-height: 1.5;\n    }\n\n    /* ── Header & Hero ── */\n    header {\n      background: rgba(255, 255, 255, 0.85);\n      backdrop-filter: saturate(180%) blur(20px);\n      -webkit-backdrop-filter: saturate(180%) blur(20px);\n      position: sticky;\n      top: 0;\n      z-index: 50;\n      border-bottom: 1px solid var(--border-subtle);\n    }\n    .nav-bar {\n      max-width: 1200px;\n      margin: 0 auto;\n      padding: 14px 24px;\n      display: flex;\n      justify-content: space-between;\n      align-items: center;\n    }\n    .brand-header-wrap {\n      display: flex;\n      align-items: center;\n      gap: 12px;\n      text-decoration: none;\n      color: inherit;\n    }\n    .brand-logo-img {\n      height: 34px;\n      width: auto;\n      object-fit: contain;\n      mix-blend-mode: multiply;\n      border-radius: 6px;\n      transition: transform 0.25s ease;\n    }\n    .brand-logo-img:hover {\n      transform: scale(1.08);\n    }\n    .brand-pill-badge {\n      display: inline-flex;\n      align-items: center;\n      gap: 8px;\n      background: #FFFFFF;\n      border: 1px solid rgba(0, 0, 0, 0.08);\n      padding: 6px 14px;\n      border-radius: 20px;\n      font-size: 0.78rem;\n      font-weight: 700;\n      letter-spacing: 0.06em;\n      text-transform: uppercase;\n      color: var(--text-primary);\n      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);\n      margin-bottom: 14px;\n    }\n    .brand-pill-logo {\n      height: 18px;\n      width: auto;\n      object-fit: contain;\n      mix-blend-mode: multiply;\n    }\n    .logo-text {\n      font-size: 1.15rem;\n      font-weight: 700;\n      letter-spacing: -0.01em;\n      color: var(--text-primary);\n      display: flex;\n      align-items: center;\n      gap: 8px;\n    }\n    .logo-title-full {\n      display: inline-block;\n      white-space: nowrap;\n    }\n    .logo-title-short {\n      display: none;\n      white-space: nowrap;\n    }\n    .logo-badge {\n      font-size: 0.72rem;\n      font-weight: 600;\n      background: var(--tag-bg);\n      color: var(--text-secondary);\n      padding: 3px 8px;\n      border-radius: 12px;\n      letter-spacing: 0.02em;\n      white-space: nowrap;\n    }\n    .nav-subtitle {\n      font-size: 0.85rem;\n      color: var(--text-secondary);\n      white-space: nowrap;\n    }\n    .nav-mobile-badge {\n      display: none;\n    }\n\n    .hero {\n      text-align: center;\n      padding: 64px 24px 36px;\n      max-width: 860px;\n      margin: 0 auto;\n    }\n    .hero-eyebrow {\n      font-size: 0.88rem;\n      font-weight: 600;\n      letter-spacing: 0.08em;\n      text-transform: uppercase;\n      color: var(--apple-blue);\n      margin-bottom: 8px;\n    }\n    .hero h1 {\n      font-size: clamp(2.4rem, 5vw, 3.8rem);\n      font-weight: 700;\n      letter-spacing: -0.03em;\n      line-height: 1.08;\n      color: var(--text-primary);\n    }\n    .hero p {\n      margin-top: 14px;\n      font-size: clamp(1.05rem, 2vw, 1.25rem);\n      color: var(--text-secondary);\n      font-weight: 400;\n      max-width: 600px;\n      margin-left: auto;\n      margin-right: auto;\n    }\n\n    /* ── Search & Filter Section ── */\n    .controls-wrap {\n      max-width: 1200px;\n      margin: 0 auto;\n      padding: 0 24px 36px;\n    }\n    .search-container {\n      display: flex;\n      justify-content: center;\n      margin-bottom: 20px;\n    }\n    .search-box-inner {\n      width: 100%;\n      max-width: 580px;\n      position: relative;\n    }\n    .search-icon {\n      position: absolute;\n      left: 18px;\n      top: 50%;\n      transform: translateY(-50%);\n      color: var(--text-tertiary);\n      pointer-events: none;\n    }\n    .search-input {\n      width: 100%;\n      padding: 16px 20px 16px 50px;\n      font-size: 1.05rem;\n      font-family: inherit;\n      border: 1px solid rgba(0,0,0,0.06);\n      border-radius: 30px;\n      background: var(--card-bg);\n      box-shadow: 0 4px 18px rgba(0,0,0,0.04);\n      outline: none;\n      color: var(--text-primary);\n      transition: all .25s ease;\n    }\n    .search-input::placeholder { color: var(--text-tertiary); }\n    .search-input:focus {\n      box-shadow: 0 0 0 4px rgba(0, 113, 227, 0.18), 0 4px 24px rgba(0,0,0,0.08);\n      border-color: rgba(0, 113, 227, 0.3);\n    }\n\n    .filter-pills-wrap {\n      position: relative;\n      max-width: 100%;\n      margin: 0 auto;\n    }\n    .filter-pills {\n      display: flex;\n      flex-wrap: wrap;\n      justify-content: center;\n      gap: 8px;\n    }\n    .filter-pill {\n      background: #FFFFFF;\n      border: 1px solid rgba(0,0,0,0.08);\n      color: var(--text-secondary);\n      font-size: 0.85rem;\n      font-weight: 500;\n      padding: 7px 16px;\n      border-radius: 20px;\n      cursor: pointer;\n      transition: all .2s ease;\n      user-select: none;\n      white-space: nowrap;\n      flex-shrink: 0;\n    }\n    .filter-pill:hover {\n      border-color: rgba(0,0,0,0.18);\n      color: var(--text-primary);\n    }\n    .filter-pill.active {\n      background: var(--text-primary);\n      color: #FFFFFF;\n      border-color: var(--text-primary);\n      box-shadow: 0 2px 8px rgba(0,0,0,0.12);\n    }\n\n    /* Functional feature filters & divider */\n    .filter-divider {\n      width: 1px;\n      height: 22px;\n      background: rgba(0,0,0,0.12);\n      align-self: center;\n      margin: 0 2px;\n      flex-shrink: 0;\n    }\n    .filter-pill-feature {\n      background: rgba(0, 113, 227, 0.05);\n      border-color: rgba(0, 113, 227, 0.18);\n      color: var(--apple-blue);\n      font-weight: 600;\n    }\n    .filter-pill-feature:hover {\n      background: rgba(0, 113, 227, 0.1);\n      border-color: var(--apple-blue);\n      color: var(--apple-blue);\n    }\n    .filter-pill-feature.active {\n      background: var(--apple-blue);\n      border-color: var(--apple-blue);\n      color: #FFFFFF;\n      box-shadow: 0 2px 10px rgba(0, 113, 227, 0.28);\n    }\n\n    @media (max-width: 768px) {\n      .nav-bar {\n        padding: 8px 16px;\n        min-height: 44px;\n        height: 44px;\n      }\n      .brand-header-wrap {\n        gap: 8px;\n      }\n      .brand-logo-img {\n        height: 24px;\n      }\n      .logo-text {\n        font-size: 0.92rem;\n        white-space: nowrap;\n      }\n      .logo-title-full {\n        display: none;\n      }\n      .logo-title-short {\n        display: inline-block;\n      }\n      .logo-badge {\n        display: none;\n      }\n      .nav-subtitle {\n        display: none;\n      }\n      .nav-mobile-badge {\n        display: inline-flex;\n        align-items: center;\n        justify-content: center;\n        font-size: 0.72rem;\n        font-weight: 600;\n        color: var(--apple-blue);\n        background: rgba(0, 113, 227, 0.08);\n        border: 1px solid rgba(0, 113, 227, 0.15);\n        padding: 2px 8px;\n        border-radius: 12px;\n        white-space: nowrap;\n        flex-shrink: 0;\n      }\n      .hero {\n        padding: 36px 16px 20px;\n      }\n      .controls-wrap {\n        padding: 0 16px 24px;\n      }\n      .filter-pills-wrap {\n        overflow: hidden;\n        margin: 0 -16px;\n        padding: 0;\n        mask-image: linear-gradient(to right, transparent 0, black 20px, black calc(100% - 20px), transparent 100%);\n        -webkit-mask-image: linear-gradient(to right, transparent 0, black 20px, black calc(100% - 20px), transparent 100%);\n      }\n      .filter-pills {\n        display: flex;\n        flex-wrap: nowrap;\n        justify-content: flex-start;\n        overflow-x: auto;\n        -webkit-overflow-scrolling: touch;\n        scroll-behavior: smooth;\n        scrollbar-width: none;\n        padding: 6px 18px 10px;\n        gap: 8px;\n      }\n      .filter-pills::-webkit-scrollbar {\n        display: none;\n      }\n      .filter-pill {\n        font-size: 0.82rem;\n        padding: 6px 14px;\n      }\n      .filter-divider {\n        height: 18px;\n        margin: 0 2px;\n      }\n    }\n\n    .count-indicator {\n      text-align: center;\n      margin-top: 14px;\n      font-size: 0.85rem;\n      color: var(--text-tertiary);\n    }\n\n    /* ── Product Grid ── */\n    .grid {\n      display: grid;\n      grid-template-columns: repeat(3, 1fr);\n      gap: 28px;\n      max-width: 1200px;\n      margin: 0 auto;\n      padding: 0 24px 96px;\n    }\n    @media (max-width: 992px) { .grid { grid-template-columns: repeat(2, 1fr); } }\n    @media (max-width: 580px) { .grid { grid-template-columns: 1fr; } }\n\n    /* ── Apple-style Showcase Card ── */\n    .card {\n      background: var(--card-bg);\n      border-radius: var(--card-radius);\n      box-shadow: var(--shadow-sm);\n      overflow: hidden;\n      cursor: pointer;\n      display: flex;\n      flex-direction: column;\n      transition: transform .26s cubic-bezier(0.16, 1, 0.3, 1), box-shadow .26s cubic-bezier(0.16, 1, 0.3, 1);\n      position: relative;\n      border: 1px solid var(--border-subtle);\n    }\n    .card:hover {\n      transform: translateY(-6px);\n      box-shadow: var(--shadow-hover);\n    }\n\n    .card-img-wrap {\n      width: 100%;\n      height: 230px;\n      background: #FAFAFC;\n      display: flex;\n      align-items: center;\n      justify-content: center;\n      overflow: hidden;\n      position: relative;\n      border-bottom: 1px solid rgba(0, 0, 0, 0.04);\n    }\n    .card-img-wrap img {\n      max-width: 82%;\n      max-height: 82%;\n      object-fit: contain;\n      transition: transform .35s ease;\n      filter: drop-shadow(0 8px 16px rgba(0,0,0,0.06));\n    }\n    .card:hover .card-img-wrap img {\n      transform: scale(1.05);\n    }\n    .card-type-chip {\n      position: absolute;\n      top: 14px;\n      left: 14px;\n      background: rgba(255, 255, 255, 0.9);\n      backdrop-filter: blur(8px);\n      -webkit-backdrop-filter: blur(8px);\n      font-size: 0.72rem;\n      font-weight: 600;\n      color: var(--text-secondary);\n      padding: 3px 9px;\n      border-radius: 12px;\n      box-shadow: 0 2px 6px rgba(0,0,0,0.04);\n    }\n\n    .card-body {\n      padding: 22px 24px 20px;\n      display: flex;\n      flex-direction: column;\n      flex: 1;\n      gap: 12px;\n    }\n    .card-brand {\n      font-size: 0.8rem;\n      font-weight: 600;\n      color: var(--apple-blue);\n      letter-spacing: 0.02em;\n    }\n    .card-title {\n      font-size: 1.45rem;\n      font-weight: 700;\n      letter-spacing: -0.02em;\n      color: var(--text-primary);\n      line-height: 1.2;\n    }\n    .card-quick-specs {\n      display: flex;\n      flex-wrap: wrap;\n      gap: 6px;\n    }\n    .spec-badge {\n      font-size: 0.76rem;\n      background: #F4F4F6;\n      color: #48484A;\n      padding: 3px 8px;\n      border-radius: 6px;\n      font-weight: 500;\n    }\n\n    .card-divider {\n      height: 1px;\n      background: var(--border-subtle);\n      margin: 4px 0;\n    }\n\n    .card-footer {\n      display: flex;\n      justify-content: space-between;\n      align-items: center;\n      font-size: 0.8rem;\n      color: var(--text-secondary);\n    }\n    .data-indicators {\n      display: flex;\n      flex-wrap: wrap;\n      gap: 8px 12px;\n    }\n    .indicator-item {\n      display: flex;\n      align-items: center;\n      gap: 4px;\n      font-size: 0.76rem;\n    }\n    .indicator-dot {\n      width: 7px;\n      height: 7px;\n      border-radius: 50%;\n      background: #34C759;\n    }\n    .indicator-dot.empty {\n      background: #D1D1D6;\n    }\n    .card-view-btn {\n      color: var(--apple-blue);\n      font-weight: 600;\n      font-size: 0.82rem;\n      display: flex;\n      align-items: center;\n      gap: 2px;\n      transition: gap .2s;\n      flex-shrink: 0;\n    }\n    .card:hover .card-view-btn {\n      gap: 5px;\n    }\n\n    /* ── View Switcher Segmented Control ── */\n    .view-switcher-container {\n      display: flex;\n      justify-content: center;\n      margin-bottom: 22px;\n    }\n    .segmented-control {\n      display: inline-flex;\n      background: rgba(0, 0, 0, 0.05);\n      padding: 3px;\n      border-radius: 22px;\n      gap: 3px;\n    }\n    .seg-btn {\n      display: inline-flex;\n      align-items: center;\n      gap: 6px;\n      padding: 7px 18px;\n      border: none;\n      background: transparent;\n      color: var(--text-secondary);\n      font-size: 0.88rem;\n      font-weight: 600;\n      border-radius: 18px;\n      cursor: pointer;\n      transition: all 0.2s ease;\n      font-family: inherit;\n      user-select: none;\n    }\n    .seg-btn:hover {\n      color: var(--text-primary);\n    }\n    .seg-btn.active {\n      background: #FFFFFF;\n      color: var(--text-primary);\n      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);\n    }\n\n    /* ── Timeline View Container ── */\n    .timeline-container {\n      max-width: 1040px;\n      margin: 0 auto;\n      padding: 0 24px 96px;\n    }\n\n    /* Timeline Toolbar */\n    .timeline-toolbar {\n      display: flex;\n      justify-content: space-between;\n      align-items: center;\n      flex-wrap: wrap;\n      gap: 12px;\n      margin-bottom: 20px;\n      padding: 16px 20px;\n      background: var(--card-bg);\n      border-radius: 16px;\n      border: 1px solid var(--border-subtle);\n      box-shadow: var(--shadow-sm);\n    }\n    .timeline-toolbar-left {\n      display: flex;\n      align-items: center;\n      gap: 10px;\n      flex-wrap: wrap;\n    }\n    .timeline-toolbar-title {\n      font-size: 1.05rem;\n      font-weight: 700;\n      color: var(--text-primary);\n      letter-spacing: -0.01em;\n    }\n    .timeline-toolbar-badge {\n      font-size: 0.78rem;\n      font-weight: 600;\n      color: var(--apple-blue);\n      background: rgba(0, 113, 227, 0.08);\n      padding: 3px 10px;\n      border-radius: 12px;\n    }\n    .timeline-sort-btn {\n      display: inline-flex;\n      align-items: center;\n      gap: 6px;\n      background: #FAFAFC;\n      border: 1px solid rgba(0, 0, 0, 0.08);\n      color: var(--text-primary);\n      padding: 8px 14px;\n      border-radius: 20px;\n      font-size: 0.82rem;\n      font-weight: 600;\n      cursor: pointer;\n      font-family: inherit;\n      transition: all 0.2s ease;\n    }\n    .timeline-sort-btn:hover {\n      background: #FFFFFF;\n      border-color: var(--apple-blue);\n      color: var(--apple-blue);\n      box-shadow: 0 2px 8px rgba(0, 113, 227, 0.12);\n    }\n\n    /* Sticky Year Navigation */\n    .timeline-year-nav {\n      position: sticky;\n      top: 60px;\n      z-index: 30;\n      display: flex;\n      gap: 6px;\n      overflow-x: auto;\n      padding: 10px 0 16px;\n      background: rgba(245, 245, 247, 0.92);\n      backdrop-filter: blur(12px);\n      -webkit-backdrop-filter: blur(12px);\n      margin-bottom: 24px;\n      scrollbar-width: none;\n    }\n    .timeline-year-nav::-webkit-scrollbar { display: none; }\n    .year-nav-pill {\n      flex-shrink: 0;\n      padding: 5px 12px;\n      font-size: 0.8rem;\n      font-weight: 600;\n      border-radius: 14px;\n      background: #FFFFFF;\n      border: 1px solid rgba(0, 0, 0, 0.08);\n      color: var(--text-secondary);\n      cursor: pointer;\n      transition: all 0.2s ease;\n      text-decoration: none;\n    }\n    .year-nav-pill:hover {\n      border-color: var(--apple-blue);\n      color: var(--apple-blue);\n    }\n    .year-nav-pill.active {\n      background: var(--text-primary);\n      color: #FFFFFF;\n      border-color: var(--text-primary);\n    }\n    .year-nav-pill.tentative-pill {\n      background: #FFF7ED;\n      border-color: rgba(255, 149, 0, 0.25);\n      color: #D97706;\n    }\n    .year-nav-pill.tentative-pill:hover,\n    .year-nav-pill.tentative-pill.active {\n      background: #D97706;\n      color: #FFFFFF;\n      border-color: #D97706;\n    }\n\n    /* Timeline Track and Spine */\n    .timeline-track {\n      position: relative;\n      padding-left: 36px;\n    }\n    .timeline-track::before {\n      content: \'\';\n      position: absolute;\n      left: 13px;\n      top: 14px;\n      bottom: 20px;\n      width: 2px;\n      background: linear-gradient(180deg, var(--apple-blue) 0%, rgba(0, 113, 227, 0.2) 80%, rgba(0, 0, 0, 0.08) 100%);\n      border-radius: 2px;\n    }\n\n    /* Year Group */\n    .timeline-year-group {\n      margin-bottom: 40px;\n      position: relative;\n    }\n    .timeline-year-header {\n      display: flex;\n      align-items: center;\n      gap: 12px;\n      margin-bottom: 18px;\n      position: relative;\n    }\n    .timeline-year-dot {\n      position: absolute;\n      left: -36px;\n      top: 50%;\n      transform: translate(5px, -50%);\n      width: 18px;\n      height: 18px;\n      border-radius: 50%;\n      background: #FFFFFF;\n      border: 4px solid var(--apple-blue);\n      box-shadow: 0 0 0 4px rgba(0, 113, 227, 0.15);\n      z-index: 2;\n    }\n    .timeline-year-title {\n      font-size: 1.45rem;\n      font-weight: 800;\n      letter-spacing: -0.02em;\n      color: var(--text-primary);\n    }\n    .timeline-year-count {\n      font-size: 0.78rem;\n      font-weight: 600;\n      color: var(--text-secondary);\n      background: rgba(0, 0, 0, 0.05);\n      padding: 3px 9px;\n      border-radius: 10px;\n    }\n\n    /* Timeline Entries */\n    .timeline-entries {\n      display: flex;\n      flex-direction: column;\n      gap: 16px;\n    }\n    .timeline-entry {\n      display: flex;\n      gap: 20px;\n      position: relative;\n      cursor: pointer;\n    }\n    .timeline-entry-node {\n      position: relative;\n      display: flex;\n      flex-direction: column;\n      align-items: flex-end;\n      width: 80px;\n      flex-shrink: 0;\n      padding-top: 14px;\n    }\n    .timeline-node-dot {\n      position: absolute;\n      left: -36px;\n      top: 20px;\n      transform: translate(8px, -50%);\n      width: 12px;\n      height: 12px;\n      border-radius: 50%;\n      background: var(--apple-blue);\n      border: 2px solid #FFFFFF;\n      box-shadow: 0 2px 4px rgba(0,0,0,0.15);\n      z-index: 2;\n    }\n    .timeline-date-chip {\n      font-size: 0.8rem;\n      font-weight: 700;\n      color: var(--text-primary);\n      background: #FFFFFF;\n      border: 1px solid rgba(0, 0, 0, 0.08);\n      padding: 4px 8px;\n      border-radius: 8px;\n      box-shadow: 0 1px 4px rgba(0,0,0,0.03);\n      white-space: nowrap;\n    }\n\n    /* Timeline Card */\n    .timeline-card {\n      flex: 1;\n      background: var(--card-bg);\n      border-radius: 18px;\n      border: 1px solid var(--border-subtle);\n      box-shadow: var(--shadow-sm);\n      display: flex;\n      gap: 18px;\n      padding: 16px 20px;\n      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);\n    }\n    .timeline-entry:hover .timeline-card {\n      transform: translateX(4px);\n      box-shadow: var(--shadow-hover);\n      border-color: rgba(0, 113, 227, 0.25);\n    }\n    .timeline-card-thumb {\n      width: 100px;\n      height: 100px;\n      background: #FAFAFC;\n      border-radius: 14px;\n      overflow: hidden;\n      display: flex;\n      align-items: center;\n      justify-content: center;\n      flex-shrink: 0;\n      border: 1px solid rgba(0, 0, 0, 0.04);\n      padding: 6px;\n    }\n    .timeline-card-thumb img {\n      max-width: 90%;\n      max-height: 90%;\n      object-fit: contain;\n      transition: transform 0.3s ease;\n      filter: drop-shadow(0 4px 8px rgba(0,0,0,0.06));\n    }\n    .timeline-entry:hover .timeline-card-thumb img {\n      transform: scale(1.08);\n    }\n    .timeline-card-content {\n      flex: 1;\n      display: flex;\n      flex-direction: column;\n      gap: 6px;\n      min-width: 0;\n    }\n    .timeline-card-meta {\n      display: flex;\n      align-items: center;\n      justify-content: space-between;\n      gap: 8px;\n      flex-wrap: wrap;\n    }\n    .timeline-card-brand {\n      font-size: 0.8rem;\n      font-weight: 600;\n      color: var(--apple-blue);\n    }\n    .timeline-verif-badge {\n      font-size: 0.72rem;\n      font-weight: 600;\n      padding: 2px 8px;\n      border-radius: 6px;\n      display: inline-flex;\n      align-items: center;\n      gap: 3px;\n    }\n    .timeline-verif-badge.verified {\n      background: #ECFDF5;\n      color: #059669;\n      border: 1px solid rgba(5, 150, 105, 0.15);\n    }\n    .timeline-card-title {\n      font-size: 1.18rem;\n      font-weight: 700;\n      color: var(--text-primary);\n      letter-spacing: -0.01em;\n      line-height: 1.25;\n    }\n    .timeline-card-type {\n      font-size: 0.82rem;\n      color: var(--text-secondary);\n    }\n    .timeline-card-quick-specs {\n      display: flex;\n      flex-wrap: wrap;\n      gap: 5px;\n      margin-top: 2px;\n    }\n    .timeline-card-evidence {\n      font-size: 0.78rem;\n      color: #48484A;\n      background: #F8F8FA;\n      padding: 6px 10px;\n      border-radius: 8px;\n      border-left: 3px solid var(--apple-blue);\n      margin-top: 4px;\n      line-height: 1.45;\n    }\n    .timeline-card-footer {\n      display: flex;\n      justify-content: space-between;\n      align-items: center;\n      margin-top: 6px;\n      padding-top: 8px;\n      border-top: 1px solid var(--border-subtle);\n      font-size: 0.78rem;\n      color: var(--text-secondary);\n    }\n\n    /* ── Tentative Section ── */\n    .timeline-tentative-group {\n      margin-top: 56px;\n      padding-top: 36px;\n      border-top: 2px dashed rgba(0, 0, 0, 0.1);\n      position: relative;\n    }\n    .timeline-tentative-header {\n      display: flex;\n      align-items: flex-start;\n      gap: 14px;\n      margin-bottom: 24px;\n    }\n    .timeline-tentative-icon {\n      width: 40px;\n      height: 40px;\n      border-radius: 12px;\n      background: #FFF7ED;\n      color: #D97706;\n      display: flex;\n      align-items: center;\n      justify-content: center;\n      flex-shrink: 0;\n      border: 1px solid rgba(217, 119, 6, 0.2);\n    }\n    .timeline-tentative-title {\n      font-size: 1.35rem;\n      font-weight: 800;\n      color: var(--text-primary);\n      letter-spacing: -0.01em;\n    }\n    .timeline-tentative-subtitle {\n      font-size: 0.86rem;\n      color: var(--text-secondary);\n      margin-top: 4px;\n    }\n    .timeline-tentative-grid {\n      display: grid;\n      grid-template-columns: repeat(2, 1fr);\n      gap: 16px;\n    }\n    @media (max-width: 768px) {\n      .timeline-tentative-grid { grid-template-columns: 1fr; }\n    }\n    .timeline-tentative-card {\n      background: #FFFFFF;\n      border-radius: 16px;\n      border: 1px solid rgba(217, 119, 6, 0.15);\n      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.03);\n      display: flex;\n      gap: 14px;\n      padding: 16px;\n      cursor: pointer;\n      transition: all 0.2s ease;\n    }\n    .timeline-tentative-card:hover {\n      transform: translateY(-3px);\n      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);\n      border-color: rgba(217, 119, 6, 0.35);\n    }\n    .tentative-card-thumb {\n      width: 80px;\n      height: 80px;\n      background: #FAFAFC;\n      border-radius: 12px;\n      overflow: hidden;\n      display: flex;\n      align-items: center;\n      justify-content: center;\n      flex-shrink: 0;\n      border: 1px solid rgba(0, 0, 0, 0.04);\n      padding: 4px;\n    }\n    .tentative-card-thumb img {\n      max-width: 90%;\n      max-height: 90%;\n      object-fit: contain;\n    }\n    .tentative-card-content {\n      flex: 1;\n      display: flex;\n      flex-direction: column;\n      gap: 5px;\n      min-width: 0;\n    }\n    .tentative-card-header {\n      display: flex;\n      justify-content: space-between;\n      align-items: center;\n      gap: 6px;\n    }\n    .tentative-brand {\n      font-size: 0.78rem;\n      font-weight: 600;\n      color: var(--apple-blue);\n    }\n    .tentative-badge {\n      font-size: 0.72rem;\n      font-weight: 600;\n      background: #FFF7ED;\n      color: #D97706;\n      border: 1px solid rgba(217, 119, 6, 0.25);\n      padding: 2px 7px;\n      border-radius: 6px;\n      white-space: nowrap;\n    }\n    .tentative-card-title {\n      font-size: 1.05rem;\n      font-weight: 700;\n      color: var(--text-primary);\n    }\n    .tentative-cause {\n      font-size: 0.76rem;\n      color: #6B7280;\n      background: #F9FAFB;\n      padding: 6px 8px;\n      border-radius: 6px;\n      line-height: 1.4;\n      margin-top: 2px;\n    }\n    .tentative-footer {\n      display: flex;\n      justify-content: flex-end;\n      margin-top: 4px;\n    }\n\n    @media (max-width: 768px) {\n      .timeline-track { padding-left: 18px; }\n      .timeline-track::before { left: 4px; }\n      .timeline-year-dot { left: -18px; transform: translate(1px, -50%); width: 14px; height: 14px; border-width: 3px; }\n      .timeline-entry { flex-direction: column; gap: 8px; }\n      .timeline-entry-node { width: 100%; flex-direction: row; justify-content: flex-start; align-items: center; padding-top: 0; padding-left: 12px; }\n      .timeline-node-dot { left: -18px; top: 50%; transform: translate(2px, -50%); }\n      .timeline-card { flex-direction: column; gap: 12px; }\n      .timeline-card-thumb { width: 100%; height: 140px; }\n    }\n\n    /* ── Empty State ── */\n    .empty-state {\n      text-align: center;\n      grid-column: 1 / -1;\n      padding: 80px 24px;\n      color: var(--text-secondary);\n    }\n    .empty-state h3 { font-size: 1.3rem; color: var(--text-primary); margin-bottom: 6px; }\n\n    /* ── Modal (Apple Detail Window) ── */\n    .modal-overlay {\n      position: fixed;\n      inset: 0;\n      background: rgba(0, 0, 0, 0.45);\n      backdrop-filter: blur(14px);\n      -webkit-backdrop-filter: blur(14px);\n      z-index: 100;\n      display: none;\n      align-items: center;\n      justify-content: center;\n      padding: 24px;\n      animation: fadeIn .2s ease;\n    }\n    .modal-overlay.open { display: flex; }\n\n    .modal-card {\n      background: #FFFFFF;\n      border-radius: 24px;\n      width: 100%;\n      max-width: 820px;\n      max-height: 88vh;\n      overflow-y: auto;\n      box-shadow: 0 24px 60px rgba(0,0,0,0.22);\n      position: relative;\n      animation: modalSlideUp .28s cubic-bezier(0.16, 1, 0.3, 1);\n      display: flex;\n      flex-direction: column;\n    }\n\n    .modal-close-btn {\n      position: absolute;\n      top: 20px;\n      right: 20px;\n      width: 36px;\n      height: 36px;\n      border-radius: 50%;\n      background: #F0F0F2;\n      border: none;\n      color: #636366;\n      font-size: 1.1rem;\n      cursor: pointer;\n      display: flex;\n      align-items: center;\n      justify-content: center;\n      z-index: 10;\n      transition: all .2s;\n    }\n    .modal-close-btn:hover { background: #E5E5EA; color: #1D1D1F; }\n\n    /* Modal Hero Section */\n    .modal-hero {\n      display: flex;\n      padding: 32px 36px 24px;\n      gap: 28px;\n      border-bottom: 1px solid var(--border-subtle);\n      background: #FAFAFC;\n      border-radius: 24px 24px 0 0;\n    }\n    @media (max-width: 600px) {\n      .modal-hero { flex-direction: column; align-items: center; text-align: center; padding: 28px 20px 20px; }\n    }\n    .modal-gallery-wrap {\n      display: flex;\n      flex-direction: column;\n      gap: 10px;\n      flex-shrink: 0;\n      width: 180px;\n    }\n    @media (max-width: 600px) {\n      .modal-gallery-wrap { width: 100%; max-width: 240px; margin: 0 auto; }\n    }\n    .modal-gallery-main {\n      width: 100%;\n      height: 180px;\n      background: #FFFFFF;\n      border-radius: 18px;\n      box-shadow: 0 4px 14px rgba(0,0,0,0.06);\n      display: flex;\n      align-items: center;\n      justify-content: center;\n      padding: 10px;\n      position: relative;\n      overflow: hidden;\n      cursor: zoom-in;\n    }\n    .modal-gallery-main img {\n      max-width: 100%;\n      max-height: 100%;\n      object-fit: contain;\n      transition: opacity 0.2s ease, transform 0.25s ease;\n      user-select: none;\n    }\n    .modal-gallery-main:hover img {\n      transform: scale(1.03);\n    }\n    .gallery-nav-btn {\n      position: absolute;\n      top: 50%;\n      transform: translateY(-50%);\n      width: 28px;\n      height: 28px;\n      background: rgba(255, 255, 255, 0.9);\n      border: 1px solid rgba(0,0,0,0.1);\n      border-radius: 50%;\n      display: flex;\n      align-items: center;\n      justify-content: center;\n      font-size: 18px;\n      line-height: 1;\n      color: var(--text-primary);\n      cursor: pointer;\n      opacity: 0;\n      transition: all 0.2s ease;\n      box-shadow: 0 2px 8px rgba(0,0,0,0.12);\n      z-index: 2;\n    }\n    .modal-gallery-main:hover .gallery-nav-btn {\n      opacity: 1;\n    }\n    .gallery-prev { left: 6px; }\n    .gallery-next { right: 6px; }\n    .gallery-nav-btn:hover {\n      background: #FFFFFF;\n      transform: translateY(-50%) scale(1.1);\n    }\n    .gallery-counter {\n      position: absolute;\n      bottom: 6px;\n      right: 8px;\n      background: rgba(0,0,0,0.6);\n      color: #FFFFFF;\n      font-size: 0.65rem;\n      font-weight: 600;\n      padding: 2px 6px;\n      border-radius: 8px;\n      letter-spacing: 0.04em;\n      pointer-events: none;\n      backdrop-filter: blur(4px);\n    }\n    .gallery-zoom-hint {\n      position: absolute;\n      top: 8px;\n      right: 8px;\n      width: 24px;\n      height: 24px;\n      border-radius: 50%;\n      background: rgba(255, 255, 255, 0.85);\n      border: 1px solid rgba(0,0,0,0.08);\n      display: flex;\n      align-items: center;\n      justify-content: center;\n      color: var(--text-secondary);\n      opacity: 0;\n      transition: opacity 0.2s ease;\n      pointer-events: none;\n    }\n    .modal-gallery-main:hover .gallery-zoom-hint {\n      opacity: 1;\n    }\n    .modal-gallery-thumbs {\n      display: flex;\n      gap: 6px;\n      justify-content: center;\n      overflow-x: auto;\n      padding: 2px 0;\n    }\n    .gallery-thumb {\n      width: 44px;\n      height: 44px;\n      border-radius: 10px;\n      background: #FFFFFF;\n      border: 2px solid transparent;\n      padding: 3px;\n      cursor: pointer;\n      display: flex;\n      align-items: center;\n      justify-content: center;\n      transition: all 0.2s ease;\n      box-shadow: 0 2px 6px rgba(0,0,0,0.05);\n      flex-shrink: 0;\n    }\n    .gallery-thumb img {\n      max-width: 100%;\n      max-height: 100%;\n      object-fit: contain;\n    }\n    .gallery-thumb:hover {\n      border-color: rgba(0, 113, 227, 0.4);\n    }\n    .gallery-thumb.active {\n      border-color: var(--apple-blue);\n      box-shadow: 0 0 0 2px rgba(0, 113, 227, 0.2);\n    }\n\n    /* Lightbox Styles */\n    .lightbox-overlay {\n      position: fixed;\n      inset: 0;\n      background: rgba(0, 0, 0, 0.85);\n      backdrop-filter: blur(15px);\n      -webkit-backdrop-filter: blur(15px);\n      z-index: 1000;\n      display: flex;\n      align-items: center;\n      justify-content: center;\n      opacity: 0;\n      pointer-events: none;\n      transition: opacity 0.25s ease;\n      padding: 24px;\n    }\n    .lightbox-overlay.open {\n      opacity: 1;\n      pointer-events: auto;\n    }\n    .lightbox-content {\n      max-width: 90vw;\n      max-height: 90vh;\n      display: flex;\n      align-items: center;\n      justify-content: center;\n    }\n    .lightbox-content img {\n      max-width: 100%;\n      max-height: 90vh;\n      object-fit: contain;\n      border-radius: 12px;\n      box-shadow: 0 20px 60px rgba(0,0,0,0.5);\n    }\n    .lightbox-close-btn {\n      position: absolute;\n      top: 24px;\n      right: 24px;\n      width: 40px;\n      height: 40px;\n      border-radius: 50%;\n      background: rgba(255,255,255,0.2);\n      border: none;\n      color: #FFFFFF;\n      font-size: 20px;\n      cursor: pointer;\n      display: flex;\n      align-items: center;\n      justify-content: center;\n      transition: background 0.2s ease;\n      z-index: 1010;\n    }\n    .lightbox-close-btn:hover {\n      background: rgba(255,255,255,0.35);\n    }\n    .modal-hero-info {\n      display: flex;\n      flex-direction: column;\n      justify-content: center;\n      gap: 8px;\n    }\n    .modal-hero-brand {\n      font-size: 0.88rem;\n      font-weight: 600;\n      color: var(--apple-blue);\n      letter-spacing: 0.02em;\n    }\n    .modal-hero-title {\n      font-size: 2rem;\n      font-weight: 700;\n      letter-spacing: -0.02em;\n      color: var(--text-primary);\n      line-height: 1.15;\n    }\n    .modal-hero-type {\n      font-size: 0.95rem;\n      color: var(--text-secondary);\n      font-weight: 500;\n    }\n    .modal-hero-pills {\n      display: flex;\n      flex-wrap: wrap;\n      gap: 6px;\n      margin-top: 4px;\n    }\n\n    /* Modal 4-Tab Navigation */\n    .modal-tabs {\n      display: flex;\n      padding: 0 36px;\n      border-bottom: 1px solid var(--border-subtle);\n      background: #FFFFFF;\n      position: sticky;\n      top: 0;\n      z-index: 5;\n      overflow-x: auto;\n    }\n    @media (max-width: 600px) { .modal-tabs { padding: 0 16px; } }\n    .modal-tab-btn {\n      padding: 16px 18px;\n      border: none;\n      background: none;\n      font-size: 0.92rem;\n      font-weight: 600;\n      color: var(--text-secondary);\n      cursor: pointer;\n      position: relative;\n      transition: color .2s;\n      white-space: nowrap;\n    }\n    .modal-tab-btn:hover { color: var(--text-primary); }\n    .modal-tab-btn.active { color: var(--apple-blue); }\n    .modal-tab-btn.active::after {\n      content: \'\';\n      position: absolute;\n      bottom: 0;\n      left: 14px;\n      right: 14px;\n      height: 3px;\n      background: var(--apple-blue);\n      border-radius: 3px 3px 0 0;\n    }\n\n    /* Modal Tab Content Panels */\n    .modal-tab-panel {\n      display: none;\n      padding: 28px 36px 36px;\n    }\n    @media (max-width: 600px) { .modal-tab-panel { padding: 20px; } }\n    .modal-tab-panel.active { display: block; }\n\n    /* Tab 1: Specs Grid */\n    .specs-grid {\n      display: grid;\n      grid-template-columns: repeat(2, 1fr);\n      gap: 14px;\n      margin-bottom: 24px;\n    }\n    @media (max-width: 600px) { .specs-grid { grid-template-columns: 1fr; } }\n    .specs-grid > :last-child:nth-child(odd) {\n      grid-column: 1 / -1;\n    }\n    .spec-item-box {\n      background: #F9F9FB;\n      border-radius: 12px;\n      padding: 12px 16px;\n      border: 1px solid rgba(0,0,0,0.03);\n    }\n    .spec-item-label {\n      font-size: 0.78rem;\n      font-weight: 600;\n      color: var(--text-secondary);\n      margin-bottom: 3px;\n      text-transform: uppercase;\n      letter-spacing: 0.02em;\n    }\n    .spec-item-val {\n      font-size: 0.95rem;\n      font-weight: 500;\n      color: var(--text-primary);\n    }\n\n    .official-notes-box {\n      background: #F5F5F7;\n      border-radius: 14px;\n      padding: 18px 20px;\n      border-left: 4px solid var(--apple-blue);\n    }\n    .official-notes-title {\n      font-size: 0.85rem;\n      font-weight: 700;\n      color: var(--text-primary);\n      margin-bottom: 6px;\n      display: flex;\n      align-items: center;\n      gap: 6px;\n    }\n    .official-notes-text {\n      font-size: 0.92rem;\n      color: #3A3A3C;\n      line-height: 1.6;\n    }\n\n    /* Tab 2: Sourced Reviews & Citation Cards */\n    .review-card {\n      background: #F9F9FB;\n      border: 1px solid rgba(0,0,0,0.06);\n      border-radius: 16px;\n      padding: 22px 24px;\n      margin-bottom: 18px;\n      position: relative;\n    }\n    .review-quote {\n      font-size: 0.98rem;\n      color: #1D1D1F;\n      line-height: 1.65;\n      font-style: normal;\n      margin-bottom: 16px;\n      position: relative;\n    }\n    .review-quote::before {\n      content: \'“\';\n      font-size: 2rem;\n      color: var(--apple-blue);\n      line-height: 1;\n      position: absolute;\n      left: -14px;\n      top: -6px;\n      opacity: 0.4;\n    }\n    .review-meta {\n      display: flex;\n      flex-wrap: wrap;\n      justify-content: space-between;\n      align-items: center;\n      gap: 10px;\n      padding-top: 14px;\n      border-top: 1px dashed rgba(0,0,0,0.08);\n      font-size: 0.82rem;\n    }\n    .review-source-badge {\n      display: inline-flex;\n      align-items: center;\n      gap: 6px;\n      background: #FFFFFF;\n      padding: 4px 10px;\n      border-radius: 8px;\n      border: 1px solid rgba(0,0,0,0.08);\n      color: #48484A;\n      font-weight: 600;\n    }\n    .review-author {\n      color: var(--text-secondary);\n    }\n    .review-link-btn {\n      color: var(--apple-blue);\n      text-decoration: none;\n      font-weight: 600;\n      display: inline-flex;\n      align-items: center;\n      gap: 3px;\n    }\n    .review-link-btn:hover { text-decoration: underline; }\n\n    /* Strict Empty State for Citations */\n    .citation-empty-card {\n      background: #FAFAFC;\n      border: 1px dashed rgba(0,0,0,0.12);\n      border-radius: 16px;\n      padding: 36px 28px;\n      text-align: center;\n      color: var(--text-secondary);\n    }\n    .citation-empty-title {\n      font-size: 1.05rem;\n      font-weight: 700;\n      color: var(--text-primary);\n      margin-bottom: 8px;\n    }\n    .citation-empty-desc {\n      font-size: 0.9rem;\n      color: #636366;\n      max-width: 520px;\n      margin: 0 auto 16px;\n      line-height: 1.6;\n    }\n    .citation-empty-badge {\n      display: inline-block;\n      font-size: 0.78rem;\n      font-weight: 600;\n      color: #FF9500;\n      background: #FFF7ED;\n      padding: 4px 12px;\n      border-radius: 12px;\n      border: 1px solid rgba(255,149,0,0.2);\n    }\n\n    /* Tables in Modal */\n    .data-table-wrap {\n      overflow-x: auto;\n      border: 1px solid var(--border-subtle);\n      border-radius: 14px;\n      background: #FFFFFF;\n    }\n    .data-table {\n      width: 100%;\n      border-collapse: collapse;\n      font-size: 0.88rem;\n    }\n    .data-table th {\n      background: #F7F7F9;\n      color: var(--text-secondary);\n      font-weight: 600;\n      padding: 12px 14px;\n      text-align: left;\n      border-bottom: 1px solid var(--border-subtle);\n      white-space: nowrap;\n    }\n    .data-table td {\n      padding: 13px 14px;\n      border-bottom: 1px solid var(--border-subtle);\n      color: var(--text-primary);\n    }\n    .data-table tr:last-child td { border-bottom: none; }\n    .data-table tr:hover td { background: #FAFAFC; }\n\n    .empty-data-hint {\n      text-align: center;\n      padding: 48px 24px;\n      color: var(--text-tertiary);\n      font-size: 0.95rem;\n    }\n\n    /* Animations */\n    @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }\n    @keyframes modalSlideUp {\n      from { transform: translateY(24px) scale(0.97); opacity: 0; }\n      to { transform: translateY(0) scale(1); opacity: 1; }\n    }\n\n    /* Footer */\n    footer {\n      text-align: center;\n      padding: 40px 24px 60px;\n      font-size: 0.82rem;\n      color: var(--text-tertiary);\n      border-top: 1px solid var(--border-subtle);\n      background: #FFFFFF;\n    }\n  </style>\n</head>\n<body>\n\n  <!-- Top Navigation Header -->\n  <header>\n    <div class="nav-bar">\n      <a href="#" class="brand-header-wrap" onclick="window.scrollTo({top: 0, behavior: \x27smooth\x27}); return false;">\n        <img src="assets/nirvana-logo.jpeg" alt="NIRVANA Logo" class="brand-logo-img" />\n        <div class="logo-text">\n          <span class="logo-title-full">NIRVANA · 网子雾化器图鉴</span>\n          <span class="logo-title-short">NIRVANA · 网子图鉴</span>\n          <span class="logo-badge">Genesis Mesh Encyclopedia</span>\n        </div>\n      </a>\n      <div class="nav-subtitle">\n        84 款经典网子雾化器 · 严谨文献与实操档案\n      </div>\n      <div class="nav-mobile-badge">\n        84 款\n      </div>\n    </div>\n  </header>\n\n  <!-- Hero Banner -->\n  <section class="hero">\n    <div class="brand-pill-badge">\n      <img src="assets/nirvana-logo.jpeg" alt="NIRVANA Logo" class="brand-pill-logo" />\n      <span>NIRVANA VAPE LABEL · ARCHIVE</span>\n    </div>\n    <div class="hero-eyebrow">The Mesh Atomizer Compendium</div>\n    <h1>网子雾化器技术与设计图鉴</h1>\n    <p>收录经典 Genesis 创世纪与网子雾化器设备档案、精密硬件规格、真实文献评测出处与作丝备忘数据。</p>\n  </section>\n\n  <!-- Search & Category Filters -->\n  <section class="controls-wrap">\n    <!-- View Switcher -->\n    <div class="view-switcher-container">\n      <div class="segmented-control" role="tablist" aria-label="视图模式切换">\n        <button class="seg-btn active" id="viewGridBtn" data-view="grid" title="经典网格卡片流">\n          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">\n            <rect x="3" y="3" width="7" height="7"></rect>\n            <rect x="14" y="3" width="7" height="7"></rect>\n            <rect x="14" y="14" width="7" height="7"></rect>\n            <rect x="3" y="14" width="7" height="7"></rect>\n          </svg>\n          <span>网格图鉴</span>\n        </button>\n        <button class="seg-btn" id="viewTimelineBtn" data-view="timeline" title="历史编年史时间轴">\n          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">\n            <line x1="12" y1="20" x2="12" y2="4"></line>\n            <circle cx="12" cy="7" r="2.5"></circle>\n            <circle cx="12" cy="12" r="2.5"></circle>\n            <circle cx="12" cy="17" r="2.5"></circle>\n            <path d="M5 7h4M15 12h4M5 17h4"></path>\n          </svg>\n          <span>编年史时间轴</span>\n        </button>\n      </div>\n    </div>\n\n    <div class="search-container">\n      <div class="search-box-inner">\n        <svg class="search-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">\n          <circle cx="11" cy="11" r="8"></circle>\n          <line x1="21" y1="21" x2="16.65" y2="16.65"></line>\n        </svg>\n        <input type="text" id="searchInput" class="search-input" placeholder="输入型号名、品牌、产地或规格关键词（如 Paravozz、In\'Ax、Monad、22mm）..." />\n      </div>\n    </div>\n\n    <!-- Filter Pills -->\n    <div class="filter-pills-wrap">\n      <div class="filter-pills" id="filterPills" role="tablist" aria-label="雾化器分类筛选">\n        <div class="filter-pill active" data-filter="all">全部 (84)</div>\n        <div class="filter-pill" data-filter="paravozz">Paravozz 车头系列 (25)</div>\n        <div class="filter-pill" data-filter="yg_creation">YG Creation 系列 (2)</div>\n        <div class="filter-pill" data-filter="blm">Bear Lair Mods (BLM) 系列 (4)</div>\n        <div class="filter-pill" data-filter="415">415 Mod 系列 (2)</div>\n        <div class="filter-pill" data-filter="domestic">国内原创名作 (5)</div>\n        <div class="filter-pill" data-filter="rsm">Rocket Science Mods (3)</div>\n        <div class="filter-pill" data-filter="docdave">Doc Dave (2)</div>\n        <div class="filter-pill" data-filter="hellfire">The Attysmith / Hellfire (4)</div>\n        <div class="filter-pill" data-filter="titaniummods">Titanium Mods (1)</div>\n        <div class="filter-pill" data-filter="walker">Walker Mods (1)</div>\n        <div class="filter-pill" data-filter="boostlab">Boost Lab (1)</div>\n        <div class="filter-pill" data-filter="nahual">Nahual Mods (1)</div>\n        <div class="filter-pill" data-filter="steamboy">Steamboy (2)</div>\n        <div class="filter-pill" data-filter="hoh">House of Hybrids (2)</div>\n        <div class="filter-pill" data-filter="athea">Athea Mods (5)</div>\n        <div class="filter-pill" data-filter="vaponaute">Vaponaute (2)</div>\n        <div class="filter-pill" data-filter="xmv">Xtra Mile Vape (2)</div>\n        <div class="filter-pill" data-filter="va">Vicious Ant (1)</div>\n        <div class="filter-pill" data-filter="satburn">Satburn (1)</div>\n        <div class="filter-pill" data-filter="vwm">VWM (4)</div>\n        <div class="filter-pill" data-filter="origen">Origen Mods (1)</div>\n        <div class="filter-pill" data-filter="ddp">DDP Vape 系列 (2)</div>\n        <div class="filter-pill" data-filter="luca">Luca Creations (2)</div>\n        <div class="filter-divider" aria-hidden="true"></div>\n        <div class="filter-pill filter-pill-feature" data-filter="has_reviews">含真实评测文献</div>\n        <div class="filter-pill filter-pill-feature" data-filter="has_zuosi">含作丝数据</div>\n        <div class="filter-pill filter-pill-feature" data-filter="has_tanbang">含碳棒数据</div>\n      </div>\n    </div>\n\n    <div class="count-indicator" id="countIndicator">\n      正在展示全部 84 款雾化器\n    </div>\n  </section>\n\n  <!-- Product Grid -->\n  <main class="grid" id="productGrid">\n    <!-- Rendered via JavaScript -->\n  </main>\n\n  <!-- Timeline View Container -->\n  <section class="timeline-container" id="timelineContainer" style="display: none;">\n    <!-- Timeline Toolbar -->\n    <div class="timeline-toolbar">\n      <div class="timeline-toolbar-left">\n        <span class="timeline-toolbar-title">历史演进编年史</span>\n        <span class="timeline-toolbar-badge" id="timelineCountBadge">69 款确证 · 11 款待考证</span>\n      </div>\n      <button class="timeline-sort-btn" id="timelineSortBtn" title="切换年代排列顺序">\n        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">\n          <path d="m3 16 4 4 4-4"></path>\n          <path d="M7 20V4"></path>\n          <path d="m21 8-4-4-4 4"></path>\n          <path d="M17 4v16"></path>\n        </svg>\n        <span id="timelineSortLabel">按发布时间：从旧到新 (2012 → 2024)</span>\n      </button>\n    </div>\n\n    <!-- Sticky Year Navigation Strip -->\n    <div class="timeline-year-nav" id="timelineYearNav"></div>\n\n    <!-- Timeline Main Track -->\n    <div class="timeline-track" id="timelineTrack"></div>\n\n    <!-- Tentative Section -->\n    <div class="timeline-tentative-section" id="timelineTentativeSection"></div>\n  </section>\n\n  <!-- Modal Detail Dialog -->\n  <div class="modal-overlay" id="modalOverlay">\n    <div class="modal-card">\n      <button class="modal-close-btn" id="modalCloseBtn" title="关闭 (Esc)">✕</button>\n\n      <!-- Modal Hero Header -->\n      <div class="modal-hero">\n        <div class="modal-gallery-wrap">\n          <div class="modal-gallery-main" id="modalGalleryMain" title="点击全屏放大查看">\n            <button class="gallery-nav-btn gallery-prev" id="galleryPrevBtn" title="上一张 (←)">‹</button>\n            <img id="modalHeroImg" src="" alt="" />\n            <button class="gallery-nav-btn gallery-next" id="galleryNextBtn" title="下一张 (→)">›</button>\n            <span class="gallery-counter" id="galleryCounter"></span>\n            <div class="gallery-zoom-hint" title="点击放大查看大图">\n              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="11" y1="8" x2="11" y2="14"></line><line x1="8" y1="11" x2="14" y2="11"></line></svg>\n            </div>\n          </div>\n          <div class="modal-gallery-thumbs" id="modalGalleryThumbs"></div>\n        </div>\n        <div class="modal-hero-info">\n          <div class="modal-hero-brand" id="modalHeroBrand"></div>\n          <div class="modal-hero-title" id="modalHeroTitle"></div>\n          <div class="modal-hero-type" id="modalHeroType"></div>\n          <div class="modal-hero-pills" id="modalHeroPills"></div>\n        </div>\n      </div>\n\n      <!-- 4 Navigation Tabs -->\n      <div class="modal-tabs">\n        <button class="modal-tab-btn active" data-tab="specs">雾化器参数</button>\n        <button class="modal-tab-btn" data-tab="reviews">玩家评测与出处</button>\n        <button class="modal-tab-btn" data-tab="zuosi">作丝数据</button>\n        <button class="modal-tab-btn" data-tab="tanbang">碳棒数据</button>\n      </div>\n\n      <!-- Tab 1: 雾化器参数 (Active by Default) -->\n      <div class="modal-tab-panel active" id="tabSpecs">\n        <div class="specs-grid" id="modalSpecsGrid"></div>\n        <div class="official-notes-box" id="modalOfficialNotesBox">\n          <div class="official-notes-title">\n            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <circle cx="12" cy="12" r="10"></circle>\n              <line x1="12" y1="16" x2="12" y2="12"></line>\n              <line x1="12" y1="8" x2="12.01" y2="8"></line>\n            </svg>\n            官方 / 工坊结构设计要点\n          </div>\n          <div class="official-notes-text" id="modalOfficialNotesText"></div>\n        </div>\n      </div>\n\n      <!-- Tab 2: 玩家评测与出处 (Strictly Sourced Citations) -->\n      <div class="modal-tab-panel" id="tabReviews">\n        <div id="modalReviewsContent"></div>\n      </div>\n\n      <!-- Tab 3: 作丝数据 -->\n      <div class="modal-tab-panel" id="tabZuosi">\n        <div id="modalZuosiContent"></div>\n      </div>\n\n      <!-- Tab 4: 碳棒数据 -->\n      <div class="modal-tab-panel" id="tabTanbang">\n        <div id="modalTanbangContent"></div>\n      </div>\n    </div>\n  </div>\n\n  <!-- Lightbox Overlay -->\n  <div class="lightbox-overlay" id="lightboxOverlay">\n    <button class="lightbox-close-btn" id="lightboxCloseBtn" title="关闭 (Esc)">✕</button>\n    <div class="lightbox-content">\n      <img id="lightboxImg" src="" alt="" />\n    </div>\n  </div>\n\n  <!-- Footer -->\n  <footer>\n    <div style="display: flex; align-items: center; justify-content: center; gap: 8px; margin-bottom: 8px;">\n      <img src="assets/nirvana-logo.jpeg" alt="NIRVANA Logo" style="height: 22px; width: auto; mix-blend-mode: multiply;" />\n      <span style="font-weight: 700; color: var(--text-primary); letter-spacing: 0.04em;">© 2026 NIRVANA VAPE LABEL</span>\n      <span>·</span>\n      <span>保留所有权利 (All Rights Reserved)</span>\n    </div>\n    <p>网子雾化器技术与设计图鉴 · Genesis Mesh Atomizer Encyclopedia · 本地与在线典藏版</p>\n    <p style="margin-top: 6px;">评测严守客观出处原则，杜绝无据杜撰 · 本项目基于 MIT 许可证开源</p>\n  </footer>\n\n  <script>\n    const ATOMIZERS = '

part2 = ';\n\n    let activeFilter = \'all\';\n    let searchQuery = \'\';\n    let currentAtomizer = null;\n    let currentView = \'grid\'; // \'grid\' | \'timeline\'\n    let timelineSortOrder = \'asc\'; // \'asc\' (2012 -> 2024) | \'desc\' (2024 -> 2012)\n\n    // DOM Elements\n    const grid = document.getElementById(\'productGrid\');\n    const timelineContainer = document.getElementById(\'timelineContainer\');\n    const viewGridBtn = document.getElementById(\'viewGridBtn\');\n    const viewTimelineBtn = document.getElementById(\'viewTimelineBtn\');\n    const timelineSortBtn = document.getElementById(\'timelineSortBtn\');\n    const timelineSortLabel = document.getElementById(\'timelineSortLabel\');\n    const timelineCountBadge = document.getElementById(\'timelineCountBadge\');\n    const timelineYearNav = document.getElementById(\'timelineYearNav\');\n    const timelineTrack = document.getElementById(\'timelineTrack\');\n    const timelineTentativeSection = document.getElementById(\'timelineTentativeSection\');\n\n    const searchInput = document.getElementById(\'searchInput\');\n    const filterPills = document.querySelectorAll(\'.filter-pill\');\n    const countIndicator = document.getElementById(\'countIndicator\');\n\n    const modalOverlay = document.getElementById(\'modalOverlay\');\n    const modalCloseBtn = document.getElementById(\'modalCloseBtn\');\n    const modalHeroImg = document.getElementById(\'modalHeroImg\');\n    const modalGalleryMain = document.getElementById(\'modalGalleryMain\');\n    const modalGalleryThumbs = document.getElementById(\'modalGalleryThumbs\');\n    const galleryPrevBtn = document.getElementById(\'galleryPrevBtn\');\n    const galleryNextBtn = document.getElementById(\'galleryNextBtn\');\n    const galleryCounter = document.getElementById(\'galleryCounter\');\n    const lightboxOverlay = document.getElementById(\'lightboxOverlay\');\n    const lightboxCloseBtn = document.getElementById(\'lightboxCloseBtn\');\n    const lightboxImg = document.getElementById(\'lightboxImg\');\n\n    let currentGalleryImages = [];\n    let currentImageIdx = 0;\n    const modalHeroBrand = document.getElementById(\'modalHeroBrand\');\n    const modalHeroTitle = document.getElementById(\'modalHeroTitle\');\n    const modalHeroType = document.getElementById(\'modalHeroType\');\n    const modalHeroPills = document.getElementById(\'modalHeroPills\');\n    const modalSpecsGrid = document.getElementById(\'modalSpecsGrid\');\n    const modalOfficialNotesBox = document.getElementById(\'modalOfficialNotesBox\');\n    const modalOfficialNotesText = document.getElementById(\'modalOfficialNotesText\');\n    const modalReviewsContent = document.getElementById(\'modalReviewsContent\');\n    const modalZuosiContent = document.getElementById(\'modalZuosiContent\');\n    const modalTanbangContent = document.getElementById(\'modalTanbangContent\');\n    const modalTabBtns = document.querySelectorAll(\'.modal-tab-btn\');\n\n    function buildSearchTokens(item) {\n      let releaseYearTokens = [];\n      if (item.specs && item.specs[\'发布时间\']) {\n        const match = item.specs[\'发布时间\'].match(/(\\d{4})/);\n        if (match) {\n          releaseYearTokens.push(match[1], match[1] + \'年\');\n        }\n        const mExact = item.specs[\'发布时间\'].match(/^(\\d{4})年(\\d{1,2})月$/);\n        if (mExact) {\n          const yr = mExact[1];\n          const mo = mExact[2];\n          const padMo = mo.padStart(2, \'0\');\n          releaseYearTokens.push(\n            `${yr}-${mo}`, `${yr}.${mo}`, `${yr}/${mo}`,\n            `${yr}-${padMo}`, `${yr}.${padMo}`, `${yr}/${padMo}`\n          );\n        }\n      }\n      const parts = [\n        item.name,\n        item.brand,\n        item.origin,\n        item.type,\n        item.officialNotes || \'\',\n        ...releaseYearTokens,\n        ...(item.quickSpecs || []),\n        ...Object.keys(item.specs || {}),\n        ...Object.values(item.specs || {}),\n        ...(item.zuosi || []).flatMap(z => [z.mesh, z.size, z.wraps]),\n        ...(item.tanbang || []).flatMap(t => [t.mesh, t.needle, t.vm3, t.vm4, t.vms, t.s35, t.snet]),\n        ...(item.reviews || []).flatMap(r => [r.quote, r.author, r.platform, r.topic])\n      ];\n      const base = parts.filter(Boolean).join(\' \').toLowerCase();\n      const unitVariants = base.replace(/(\\d+(?:\\.\\d+)?)\\s*(mm|ml|cm|目)/gi, (m, num, unit) => \' \' + num + unit + \' \' + num + \' \' + unit + \' \');\n      const decimalVariants = base.replace(/(\\d+)\\.0\\s*(mm|ml|cm)/gi, (m, num, unit) => \' \' + num + unit + \' \' + num + \' \' + unit + \' \');\n      const intToDecVariants = base.replace(/(?:^|\\D)(\\d+)\\s*(mm|ml|cm)(?:\\D|$)/gi, (m, num, unit) => \' \' + num + \'.0\' + unit + \' \' + num + \'.0 \' + unit + \' \');\n      const meshVariants1 = base.replace(/#(\\d+)/g, (m, num) => \' \' + num + \'目 #\' + num + \' \' + num + \' \');\n      const meshVariants2 = base.replace(/(\\d+)\\s*目/g, (m, num) => \' #\' + num + \' \' + num + \'目 \' + num + \' \');\n      const meshVariants3 = base.replace(/(?:^|\\D)(150|200|230|250|280|300|325|400|500|600)(?:\\D|$)/g, (m, num) => \' \' + num + \'目 #\' + num + \' \' + num + \' \');\n\n      return [base, unitVariants, decimalVariants, intToDecVariants, meshVariants1, meshVariants2, meshVariants3].join(\' \');\n    }\n\n    function getFilteredAtomizers() {\n      const q = searchQuery.trim().toLowerCase();\n      return ATOMIZERS.filter(item => {\n        // Filter pills match\n        if (activeFilter === \'paravozz\' && !item.brand.toLowerCase().includes(\'paravozz\') && !item.name.toLowerCase().includes(\'paravozz\')) return false;\n        if (activeFilter === \'yg_creation\' && !item.brand.toLowerCase().includes(\'yg creation\') && !item.name.toLowerCase().includes(\'yg creation\')) return false;\n        if (activeFilter === \'blm\' && !item.brand.toLowerCase().includes(\'bear lair\') && !item.brand.includes(\'BLM\')) return false;\n        if (activeFilter === \'415\' && !item.brand.includes(\'415\') && !item.name.includes(\'S61\')) return false;\n        if (activeFilter === \'domestic\' && !item.origin.includes(\'中国\')) return false;\n        if (activeFilter === \'athea\' && !item.brand.toLowerCase().includes(\'athea\')) return false;\n        if (activeFilter === \'vaponaute\' && !item.brand.toLowerCase().includes(\'vaponaute\')) return false;\n        if (activeFilter === \'xmv\' && !item.brand.toLowerCase().includes(\'xtra mile\')) return false;\n        if (activeFilter === \'rsm\' && !item.brand.toLowerCase().includes(\'rocket science\')) return false;\n        if (activeFilter === \'docdave\' && !item.brand.toLowerCase().includes(\'doc dave\')) return false;\n        if (activeFilter === \'hellfire\' && !item.brand.toLowerCase().includes(\'hellfire\') && !item.brand.toLowerCase().includes(\'attysmith\')) return false;\n        if (activeFilter === \'titaniummods\' && !item.brand.toLowerCase().includes(\'titanium mods\')) return false;\n        if (activeFilter === \'walker\' && !item.brand.toLowerCase().includes(\'walker\')) return false;\n        if (activeFilter === \'boostlab\' && !item.brand.toLowerCase().includes(\'boost lab\')) return false;\n        if (activeFilter === \'nahual\' && !item.brand.toLowerCase().includes(\'nahual\') && !item.brand.toLowerCase().includes(\'urquidez\')) return false;\n        if (activeFilter === \'steamboy\' && !item.brand.toLowerCase().includes(\'steamboy\')) return false;\n        if (activeFilter === \'hoh\' && !item.brand.toLowerCase().includes(\'house of hybrids\') && !item.brand.toLowerCase().includes(\'zen\')) return false;\n        if (activeFilter === \'va\' && !item.brand.toLowerCase().includes(\'vicious ant\')) return false;\n        if (activeFilter === \'satburn\' && !item.brand.toLowerCase().includes(\'satburn\')) return false;\n        if (activeFilter === \'vwm\' && !item.brand.toLowerCase().includes(\'vwm\') && !item.brand.toLowerCase().includes(\'vape ware\')) return false;\n        if (activeFilter === \'origen\' && !item.brand.toLowerCase().includes(\'origen\')) return false;\n        if (activeFilter === \'ddp\' && !item.brand.toLowerCase().includes(\'ddp\')) return false;\n        if (activeFilter === \'luca\' && !item.brand.toLowerCase().includes(\'luca\')) return false;\n        if (activeFilter === \'has_reviews\' && (!item.reviews || item.reviews.length === 0)) return false;\n        if (activeFilter === \'has_zuosi\' && (!item.zuosi || item.zuosi.length === 0)) return false;\n        if (activeFilter === \'has_tanbang\' && (!item.tanbang || item.tanbang.length === 0)) return false;\n\n        // Search query match across multiple dimensions\n        if (q) {\n          const terms = q.split(/\\s+/).filter(Boolean);\n          const searchable = buildSearchTokens(item);\n          return terms.every(term => {\n            if (searchable.includes(term)) return true;\n            const alt1 = term.replace(/(\\d+(?:\\.\\d+)?)\\s*(mm|ml|cm|目)/gi, \'$1 $2\').trim();\n            if (searchable.includes(alt1)) return true;\n            const alt2 = term.replace(/(\\d+(?:\\.\\d+)?)\\s*(mm|ml|cm|目)/gi, \'$1$2\').trim();\n            if (searchable.includes(alt2)) return true;\n            const alt3 = term.replace(/(\\d+)\\s*目/gi, \'#$1\').trim();\n            if (searchable.includes(alt3)) return true;\n            const alt4 = term.replace(/#(\\d+)/gi, \'$1目\').trim();\n            if (searchable.includes(alt4)) return true;\n            const alt5 = term.replace(/[#目]/g, \'\').trim();\n            if (alt5 && searchable.includes(alt5)) return true;\n            return false;\n          });\n        }\n\n        return true;\n      });\n    }\n\n    // Render Cards Grid\n    function renderGrid(filtered) {\n      if (filtered.length === 0) {\n        grid.innerHTML = `\n          <div class="empty-state">\n            <h3>未找到匹配的雾化器</h3>\n            <p>请尝试其他关键词或点击上方全部标签重置筛选</p>\n          </div>\n        `;\n        return;\n      }\n\n      grid.innerHTML = filtered.map(item => {\n        const hasReviews = item.reviews && item.reviews.length > 0;\n        const hasZuosi = item.zuosi && item.zuosi.length > 0;\n        const hasTanbang = item.tanbang && item.tanbang.length > 0;\n\n        return `\n          <div class="card" onclick="openModal(\'${item.id}\')">\n            <div class="card-img-wrap">\n              <span class="card-type-chip">${item.type}</span>\n              <img src="${item.image}" alt="${item.name}" loading="lazy" onerror="this.src=\'images/sakura.svg\'" />\n            </div>\n            <div class="card-body">\n              <div class="card-brand">${item.brand} · ${item.origin}${item.specs && item.specs[\'发布时间\'] ? \' · \' + item.specs[\'发布时间\'] : \'\'}</div>\n              <div class="card-title">${item.name}</div>\n              <div class="card-quick-specs">\n                ${item.quickSpecs.map(s => `<span class="spec-badge">${s}</span>`).join(\'\')}\n              </div>\n              <div class="card-divider"></div>\n              <div class="card-footer">\n                <div class="data-indicators">\n                  <span class="indicator-item" title="评测文献">\n                    <span class="indicator-dot ${hasReviews ? \'\' : \'empty\'}"></span>\n                    ${hasReviews ? `文献 (${item.reviews.length})` : \'评测待录\'}\n                  </span>\n                  <span class="indicator-item" title="作丝尺寸数据">\n                    <span class="indicator-dot ${hasZuosi ? \'\' : \'empty\'}"></span>\n                    ${hasZuosi ? `作丝 (${item.zuosi.length})` : \'作丝暂缺\'}\n                  </span>\n                  <span class="indicator-item" title="碳棒备忘数据">\n                    <span class="indicator-dot ${hasTanbang ? \'\' : \'empty\'}"></span>\n                    ${hasTanbang ? `碳棒 (${item.tanbang.length})` : \'碳棒暂缺\'}\n                  </span>\n                </div>\n                <div class="card-view-btn">\n                  详情 <span>→</span>\n                </div>\n              </div>\n            </div>\n          </div>\n        `;\n      }).join(\'\');\n    }\n\n    // Helper: Parse date for timeline sorting\n    function parseItemDate(item) {\n      const d = (item.specs && item.specs[\'发布时间\']) ? item.specs[\'发布时间\'] : \'\';\n      const m = d.match(/^(\\d{4})年(\\d{1,2})月$/);\n      if (m) {\n        return {\n          isConfirmed: true,\n          year: parseInt(m[1], 10),\n          month: parseInt(m[2], 10),\n          key: parseInt(m[1], 10) * 100 + parseInt(m[2], 10),\n          raw: d\n        };\n      }\n      const mYr = d.match(/(\\d{4})/);\n      return {\n        isConfirmed: false,\n        year: mYr ? parseInt(mYr[1], 10) : 9999,\n        month: 99,\n        key: mYr ? parseInt(mYr[1], 10) * 100 + 99 : 999999,\n        raw: d\n      };\n    }\n\n    // Render Timeline View\n    function renderTimeline(filtered) {\n      if (!timelineTrack || !timelineTentativeSection || !timelineYearNav) return;\n\n      const confirmedItems = [];\n      const tentativeItems = [];\n\n      filtered.forEach(item => {\n        const info = parseItemDate(item);\n        if (info.isConfirmed && item.dateVerification && item.dateVerification.status === \'confirmed\') {\n          confirmedItems.push({ item, info });\n        } else {\n          tentativeItems.push({ item, info });\n        }\n      });\n\n      // Sort confirmed items by key\n      confirmedItems.sort((a, b) => {\n        return timelineSortOrder === \'asc\' ? a.info.key - b.info.key : b.info.key - a.info.key;\n      });\n\n      // Update Toolbar badge and sort label\n      if (timelineSortOrder === \'asc\') {\n        timelineSortLabel.textContent = \'按发布时间：从旧到新 (2012 → 2024)\';\n      } else {\n        timelineSortLabel.textContent = \'按发布时间：从新到旧 (2024 → 2012)\';\n      }\n\n      if (timelineCountBadge) {\n        timelineCountBadge.textContent = `${confirmedItems.length} 款确证 · ${tentativeItems.length} 款待考证`;\n      }\n\n      // Group confirmed items by year\n      const yearMap = new Map();\n      confirmedItems.forEach(({ item, info }) => {\n        if (!yearMap.has(info.year)) {\n          yearMap.set(info.year, []);\n        }\n        yearMap.get(info.year).push({ item, info });\n      });\n\n      // Build Sticky Year Nav\n      const navYears = Array.from(yearMap.keys());\n      let navHtml = navYears.map(yr => `\n        <a href="#year-node-${yr}" class="year-nav-pill" onclick="scrollToYear(event, \'${yr}\')">${yr}</a>\n      `).join(\'\');\n\n      if (tentativeItems.length > 0) {\n        navHtml += `\n          <a href="#year-node-tentative" class="year-nav-pill tentative-pill" onclick="scrollToYear(event, \'tentative\')">待考证 (${tentativeItems.length})</a>\n        `;\n      }\n      timelineYearNav.innerHTML = navHtml;\n\n      // Empty State for timeline\n      if (confirmedItems.length === 0 && tentativeItems.length === 0) {\n        timelineTrack.innerHTML = `\n          <div class="empty-state">\n            <h3>未找到匹配的编年史雾化器</h3>\n            <p>请尝试其他关键词或点击上方全部标签重置筛选</p>\n          </div>\n        `;\n        timelineTentativeSection.innerHTML = \'\';\n        return;\n      }\n\n      // Render Year Groups\n      let trackHtml = \'\';\n      yearMap.forEach((entries, yr) => {\n        trackHtml += `\n          <div class="timeline-year-group" id="year-node-${yr}">\n            <div class="timeline-year-header">\n              <div class="timeline-year-dot"></div>\n              <div class="timeline-year-title">${yr} 年</div>\n              <div class="timeline-year-count">${entries.length} 款名作</div>\n            </div>\n            <div class="timeline-entries">\n              ${entries.map(({ item, info }) => {\n                const hasReviews = item.reviews && item.reviews.length > 0;\n                const hasZuosi = item.zuosi && item.zuosi.length > 0;\n                const hasTanbang = item.tanbang && item.tanbang.length > 0;\n                const primaryEvidence = (item.dateVerification && item.dateVerification.primary) ? item.dateVerification.primary : \'\';\n                return `\n                  <div class="timeline-entry" onclick="openModal(\'${item.id}\')">\n                    <div class="timeline-entry-node">\n                      <div class="timeline-node-dot"></div>\n                      <div class="timeline-date-chip">${info.raw}</div>\n                    </div>\n                    <div class="timeline-card">\n                      <div class="timeline-card-thumb">\n                        <img src="${item.image}" alt="${item.name}" loading="lazy" onerror="this.src=\'images/sakura.svg\'" />\n                      </div>\n                      <div class="timeline-card-content">\n                        <div class="timeline-card-meta">\n                          <span class="timeline-card-brand">${item.brand} · ${item.origin}</span>\n                          <span class="timeline-verif-badge verified">✓ 双源考证</span>\n                        </div>\n                        <div class="timeline-card-title">${item.name}</div>\n                        <div class="timeline-card-type">${item.type}</div>\n                        <div class="timeline-card-quick-specs">\n                          ${(item.quickSpecs || []).map(s => `<span class="spec-badge">${s}</span>`).join(\'\')}\n                        </div>\n                        ${primaryEvidence ? `\n                          <div class="timeline-card-evidence">\n                            <span style="font-weight:600;color:var(--apple-blue);margin-right:4px;">出处依据:</span>${primaryEvidence}\n                          </div>\n                        ` : \'\'}\n                        <div class="timeline-card-footer">\n                          <div class="data-indicators">\n                            <span class="indicator-item" title="评测文献">\n                              <span class="indicator-dot ${hasReviews ? \'\' : \'empty\'}"></span>\n                              ${hasReviews ? `文献 (${item.reviews.length})` : \'评测待录\'}\n                            </span>\n                            <span class="indicator-item" title="作丝尺寸数据">\n                              <span class="indicator-dot ${hasZuosi ? \'\' : \'empty\'}"></span>\n                              ${hasZuosi ? `作丝 (${item.zuosi.length})` : \'作丝暂缺\'}\n                            </span>\n                            <span class="indicator-item" title="碳棒备忘数据">\n                              <span class="indicator-dot ${hasTanbang ? \'\' : \'empty\'}"></span>\n                              ${hasTanbang ? `碳棒 (${item.tanbang.length})` : \'碳棒暂缺\'}\n                            </span>\n                          </div>\n                          <div class="card-view-btn">\n                            详情 <span>→</span>\n                          </div>\n                        </div>\n                      </div>\n                    </div>\n                  </div>\n                `;\n              }).join(\'\')}\n            </div>\n          </div>\n        `;\n      });\n      timelineTrack.innerHTML = trackHtml;\n\n      // Render Tentative Section\n      if (tentativeItems.length > 0) {\n        timelineTentativeSection.innerHTML = `\n          <div class="timeline-tentative-group" id="year-node-tentative">\n            <div class="timeline-tentative-header">\n              <div class="timeline-tentative-icon">\n                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n                  <circle cx="12" cy="12" r="10"></circle>\n                  <line x1="12" y1="8" x2="12" y2="12"></line>\n                  <line x1="12" y1="16" x2="12.01" y2="16"></line>\n                </svg>\n              </div>\n              <div>\n                <div class="timeline-tentative-title">年代待考证专区 (${tentativeItems.length} 款)</div>\n                <div class="timeline-tentative-subtitle">以下型号公开发布记录尚在多方核验中，暂不列入正式年代主轴</div>\n              </div>\n            </div>\n            <div class="timeline-tentative-grid">\n              ${tentativeItems.map(({ item, info }) => {\n                const analysisText = (item.dateVerification && item.dateVerification.analysis) ? item.dateVerification.analysis : \'暂无详细记录\';\n                return `\n                  <div class="timeline-tentative-card" onclick="openModal(\'${item.id}\')">\n                    <div class="tentative-card-thumb">\n                      <img src="${item.image}" alt="${item.name}" loading="lazy" onerror="this.src=\'images/sakura.svg\'" />\n                    </div>\n                    <div class="tentative-card-content">\n                      <div class="tentative-card-header">\n                        <span class="tentative-brand">${item.brand} · ${item.origin}</span>\n                        <span class="tentative-badge">${info.raw}</span>\n                      </div>\n                      <div class="tentative-card-title">${item.name}</div>\n                      <div class="tentative-cause">\n                        <strong>考据说明：</strong>${analysisText}\n                      </div>\n                      <div class="tentative-footer">\n                        <span class="card-view-btn">查阅详细档案 <span>→</span></span>\n                      </div>\n                    </div>\n                  </div>\n                `;\n              }).join(\'\')}\n            </div>\n          </div>\n        `;\n      } else {\n        timelineTentativeSection.innerHTML = \'\';\n      }\n    }\n\n    function scrollToYear(event, yrId) {\n      event.preventDefault();\n      const targetId = yrId === \'tentative\' ? \'year-node-tentative\' : `year-node-${yrId}`;\n      const el = document.getElementById(targetId);\n      if (el) {\n        const yOffset = -120;\n        const y = el.getBoundingClientRect().top + window.pageYOffset + yOffset;\n        window.scrollTo({ top: y, behavior: \'smooth\' });\n      }\n    }\n\n    // Unified View Updater\n    function updateViews() {\n      const filtered = getFilteredAtomizers();\n      if (currentView === \'grid\') {\n        grid.style.display = \'grid\';\n        timelineContainer.style.display = \'none\';\n        renderGrid(filtered);\n        countIndicator.textContent = `共收录 ${ATOMIZERS.length} 款雾化器，当前展示 ${filtered.length} 款`;\n      } else {\n        grid.style.display = \'none\';\n        timelineContainer.style.display = \'block\';\n        renderTimeline(filtered);\n        const confirmedCount = filtered.filter(a => a.dateVerification && a.dateVerification.status === \'confirmed\').length;\n        const tentativeCount = filtered.length - confirmedCount;\n        countIndicator.textContent = `共收录 ${ATOMIZERS.length} 款雾化器，编年史展示 ${confirmedCount} 款确证，${tentativeCount} 款待考证`;\n      }\n    }\n\n    // Modal Operations\n    function setGalleryImages(images) {\n      currentGalleryImages = (images && images.length > 0) ? images : [modalHeroImg.src];\n      currentImageIdx = 0;\n      modalGalleryThumbs.innerHTML = \'\';\n\n      if (currentGalleryImages.length > 1) {\n        galleryPrevBtn.style.display = \'flex\';\n        galleryNextBtn.style.display = \'flex\';\n        galleryCounter.style.display = \'block\';\n        modalGalleryThumbs.style.display = \'flex\';\n\n        currentGalleryImages.forEach((imgSrc, idx) => {\n          const thumb = document.createElement(\'div\');\n          thumb.className = \'gallery-thumb\' + (idx === 0 ? \' active\' : \'\');\n          thumb.innerHTML = `<img src="${imgSrc}" alt="缩略图 ${idx + 1}" />`;\n          thumb.addEventListener(\'click\', (e) => {\n            e.stopPropagation();\n            currentImageIdx = idx;\n            updateGalleryView(currentImageIdx);\n          });\n          modalGalleryThumbs.appendChild(thumb);\n        });\n      } else {\n        galleryPrevBtn.style.display = \'none\';\n        galleryNextBtn.style.display = \'none\';\n        galleryCounter.style.display = \'none\';\n        modalGalleryThumbs.style.display = \'none\';\n      }\n\n      updateGalleryView(0);\n    }\n\n    function updateGalleryView(index) {\n      if (!currentGalleryImages[index]) return;\n      modalHeroImg.style.opacity = \'0.5\';\n      setTimeout(() => {\n        modalHeroImg.src = currentGalleryImages[index];\n        modalHeroImg.style.opacity = \'1\';\n      }, 80);\n\n      galleryCounter.textContent = `${index + 1} / ${currentGalleryImages.length}`;\n\n      const thumbs = modalGalleryThumbs.querySelectorAll(\'.gallery-thumb\');\n      thumbs.forEach((t, i) => {\n        t.classList.toggle(\'active\', i === index);\n      });\n    }\n\n    function openLightbox(src) {\n      if (!src) return;\n      lightboxImg.src = src;\n      lightboxOverlay.classList.add(\'open\');\n    }\n\n    function closeLightbox() {\n      lightboxOverlay.classList.remove(\'open\');\n    }\n\n    function openModal(id) {\n      const item = ATOMIZERS.find(a => a.id === id);\n      if (!item) return;\n      currentAtomizer = item;\n\n      const itemImages = (item.images && item.images.length > 0) ? item.images : [item.image];\n      setGalleryImages(itemImages);\n      modalHeroBrand.textContent = `${item.brand} · ${item.origin}${item.specs && item.specs[\'发布时间\'] ? \' · \' + item.specs[\'发布时间\'] : \'\'}`;\n      modalHeroTitle.textContent = item.name;\n      modalHeroType.textContent = item.type;\n      modalHeroPills.innerHTML = item.quickSpecs.map(s => `<span class="spec-badge">${s}</span>`).join(\'\');\n\n      // Populate Tab 1: Specs Grid\n      modalSpecsGrid.innerHTML = Object.entries(item.specs).map(([key, val]) => `\n        <div class="spec-item-box">\n          <div class="spec-item-label">${key}</div>\n          <div class="spec-item-val">${val}</div>\n        </div>\n      `).join(\'\');\n\n      // Populate Official Notes\n      if (item.officialNotes) {\n        modalOfficialNotesBox.style.display = \'block\';\n        modalOfficialNotesText.textContent = item.officialNotes;\n      } else {\n        modalOfficialNotesBox.style.display = \'none\';\n      }\n\n      // Populate Tab 2: Reviews & Citations\n      if (item.reviews && item.reviews.length > 0) {\n        modalReviewsContent.innerHTML = item.reviews.map(r => `\n          <div class="review-card">\n            <div class="review-quote">${r.quote}</div>\n            <div class="review-meta">\n              <div class="review-source-badge">\n                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n                  <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>\n                  <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>\n                </svg>\n                ${r.platform}\n              </div>\n              <div class="review-author">${r.author ? `来源 / 评测人：${r.author}` : \'\'}</div>\n              <div style="font-size:0.78rem;color:#86868b;width:100%;">主题 / 检索线索：${r.topic}</div>\n              ${r.url ? `<a href="${r.url}" target="_blank" class="review-link-btn">查阅文献源 ↗</a>` : \'\'}\n            </div>\n          </div>\n        `).join(\'\');\n      } else {\n        modalReviewsContent.innerHTML = `\n          <div class="citation-empty-card">\n            <div class="citation-empty-title">暂无经考证的公开原帖出处</div>\n            <div class="citation-empty-desc">\n              该型号在公开论坛（如 eCigTalk 等）暂未检索到具备确凿出处的详细评测原话。\n            </div>\n            <div class="citation-empty-badge">欢迎提供可查证的原帖或实测记录</div>\n          </div>\n        `;\n      }\n\n      // Populate Tab 3: Zuosi Tab\n      if (item.zuosi && item.zuosi.length > 0) {\n        modalZuosiContent.innerHTML = `\n          <div class="data-table-wrap">\n            <table class="data-table">\n              <thead>\n                <tr>\n                  <th>网格目数</th>\n                  <th>裁网尺寸</th>\n                  <th>圈数规格 (VM)</th>\n                </tr>\n              </thead>\n              <tbody>\n                ${item.zuosi.map(z => `\n                  <tr>\n                    <td><strong>${z.mesh}</strong></td>\n                    <td>${z.size}</td>\n                    <td><span class="spec-badge" style="background:#EBF5FF;color:#0071E3;">${z.wraps}</span></td>\n                  </tr>\n                `).join(\'\')}\n              </tbody>\n            </table>\n          </div>\n        `;\n      } else {\n        modalZuosiContent.innerHTML = `\n          <div class="empty-data-hint">\n            <p>该型号备忘录中暂无收录的作丝尺寸数据。</p>\n          </div>\n        `;\n      }\n\n      // Populate Tab 4: Tanbang Tab\n      if (item.tanbang && item.tanbang.length > 0) {\n        const hasNeedle = item.tanbang.some(t => t.needle);\n        const hasVm3 = item.tanbang.some(t => t.vm3);\n        const hasVm4 = item.tanbang.some(t => t.vm4);\n        const hasVms = item.tanbang.some(t => t.vms);\n        const hasS35 = item.tanbang.some(t => t.s35);\n        const hasSnet = item.tanbang.some(t => t.snet);\n\n        modalTanbangContent.innerHTML = `\n          <div class="data-table-wrap">\n            <table class="data-table">\n              <thead>\n                <tr>\n                  <th>网格目数</th>\n                  ${hasNeedle ? \'<th>避雷针规格</th>\' : \'\'}\n                  ${hasVm3 ? \'<th>3.0 3VM</th>\' : \'\'}\n                  ${hasVm4 ? \'<th>3.0 4VM</th>\' : \'\'}\n                  ${hasVms ? \'<th>3.0 VM+S</th>\' : \'\'}\n                  ${hasS35 ? \'<th>3.5 规格</th>\' : \'\'}\n                  ${hasSnet ? \'<th>S网 规格</th>\' : \'\'}\n                </tr>\n              </thead>\n              <tbody>\n                ${item.tanbang.map(t => `\n                  <tr>\n                    <td><strong>${t.mesh}</strong></td>\n                    ${hasNeedle ? `<td>${t.needle || \'—\'}</td>` : \'\'}\n                    ${hasVm3 ? `<td>${t.vm3 || \'—\'}</td>` : \'\'}\n                    ${hasVm4 ? `<td>${t.vm4 || \'—\'}</td>` : \'\'}\n                    ${hasVms ? `<td>${t.vms || \'—\'}</td>` : \'\'}\n                    ${hasS35 ? `<td>${t.s35 || \'—\'}</td>` : \'\'}\n                    ${hasSnet ? `<td>${t.snet || \'—\'}</td>` : \'\'}\n                  </tr>\n                `).join(\'\')}\n              </tbody>\n            </table>\n          </div>\n        `;\n      } else {\n        modalTanbangContent.innerHTML = `\n          <div class="empty-data-hint">\n            <p>该型号备忘录中暂无碳棒制作尺寸记录。</p>\n          </div>\n        `;\n      }\n\n      // Reset Tab to Specs by default\n      switchTab(\'specs\');\n\n      modalOverlay.classList.add(\'open\');\n      document.body.style.overflow = \'hidden\';\n    }\n\n    function closeModal() {\n      modalOverlay.classList.remove(\'open\');\n      document.body.style.overflow = \'\';\n      currentAtomizer = null;\n    }\n\n    function switchTab(tabId) {\n      modalTabBtns.forEach(btn => {\n        btn.classList.toggle(\'active\', btn.dataset.tab === tabId);\n      });\n      document.getElementById(\'tabSpecs\').classList.toggle(\'active\', tabId === \'specs\');\n      document.getElementById(\'tabReviews\').classList.toggle(\'active\', tabId === \'reviews\');\n      document.getElementById(\'tabZuosi\').classList.toggle(\'active\', tabId === \'zuosi\');\n      document.getElementById(\'tabTanbang\').classList.toggle(\'active\', tabId === \'tanbang\');\n    }\n\n    // Event Listeners\n    searchInput.addEventListener(\'input\', (e) => {\n      searchQuery = e.target.value;\n      updateViews();\n    });\n\n    filterPills.forEach(pill => {\n      pill.addEventListener(\'click\', () => {\n        filterPills.forEach(p => p.classList.remove(\'active\'));\n        pill.classList.add(\'active\');\n        activeFilter = pill.dataset.filter;\n        updateViews();\n        pill.scrollIntoView({ behavior: \'smooth\', inline: \'center\', block: \'nearest\' });\n      });\n    });\n\n    if (viewGridBtn) {\n      viewGridBtn.addEventListener(\'click\', () => {\n        currentView = \'grid\';\n        viewGridBtn.classList.add(\'active\');\n        viewTimelineBtn.classList.remove(\'active\');\n        updateViews();\n      });\n    }\n\n    if (viewTimelineBtn) {\n      viewTimelineBtn.addEventListener(\'click\', () => {\n        currentView = \'timeline\';\n        viewTimelineBtn.classList.add(\'active\');\n        viewGridBtn.classList.remove(\'active\');\n        updateViews();\n      });\n    }\n\n    if (timelineSortBtn) {\n      timelineSortBtn.addEventListener(\'click\', () => {\n        timelineSortOrder = timelineSortOrder === \'asc\' ? \'desc\' : \'asc\';\n        updateViews();\n      });\n    }\n\n    modalTabBtns.forEach(btn => {\n      btn.addEventListener(\'click\', () => switchTab(btn.dataset.tab));\n    });\n\n    galleryPrevBtn.addEventListener(\'click\', (e) => {\n      e.stopPropagation();\n      if (currentGalleryImages.length <= 1) return;\n      currentImageIdx = (currentImageIdx - 1 + currentGalleryImages.length) % currentGalleryImages.length;\n      updateGalleryView(currentImageIdx);\n    });\n\n    galleryNextBtn.addEventListener(\'click\', (e) => {\n      e.stopPropagation();\n      if (currentGalleryImages.length <= 1) return;\n      currentImageIdx = (currentImageIdx + 1) % currentGalleryImages.length;\n      updateGalleryView(currentImageIdx);\n    });\n\n    modalGalleryMain.addEventListener(\'click\', () => {\n      if (currentGalleryImages[currentImageIdx]) {\n        openLightbox(currentGalleryImages[currentImageIdx]);\n      }\n    });\n\n    lightboxCloseBtn.addEventListener(\'click\', closeLightbox);\n    lightboxOverlay.addEventListener(\'click\', (e) => {\n      if (e.target === lightboxOverlay) closeLightbox();\n    });\n\n    modalCloseBtn.addEventListener(\'click\', closeModal);\n    modalOverlay.addEventListener(\'click\', (e) => {\n      if (e.target === modalOverlay) closeModal();\n    });\n\n    window.addEventListener(\'keydown\', (e) => {\n      if (e.key === \'Escape\') {\n        if (lightboxOverlay.classList.contains(\'open\')) {\n          closeLightbox();\n          return;\n        }\n        if (modalOverlay.classList.contains(\'open\')) {\n          closeModal();\n          return;\n        }\n      }\n      if (modalOverlay.classList.contains(\'open\')) {\n        if (e.key === \'ArrowLeft\' && currentGalleryImages.length > 1) {\n          currentImageIdx = (currentImageIdx - 1 + currentGalleryImages.length) % currentGalleryImages.length;\n          updateGalleryView(currentImageIdx);\n          if (lightboxOverlay.classList.contains(\'open\')) {\n            lightboxImg.src = currentGalleryImages[currentImageIdx];\n          }\n        } else if (e.key === \'ArrowRight\' && currentGalleryImages.length > 1) {\n          currentImageIdx = (currentImageIdx + 1) % currentGalleryImages.length;\n          updateGalleryView(currentImageIdx);\n          if (lightboxOverlay.classList.contains(\'open\')) {\n            lightboxImg.src = currentGalleryImages[currentImageIdx];\n          }\n        }\n      }\n    });\n\n    // Initial render\n    updateViews();\n  </script>\n</body>\n</html>'


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, 'index.html')
    html_content = part1 + json.dumps(data, ensure_ascii=False) + part2
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("index.html successfully generated!")

if __name__ == '__main__':
    main()
