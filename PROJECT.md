# Project: 网子雾化器图鉴全维度深度核查与质量审计

## Architecture
- **Data Source & Compiler**: `/Users/kali/Documents/网子图鉴/generate_html.py`
  - Defines `data = [...]` containing 108 Pure Genesis atomizers, their 12 standardized parameters, image paths, and date verification dual-source evidence.
  - Compiles the dataset into static `/Users/kali/Documents/网子图鉴/index.html`.
- **Presentation Layer**: `/Users/kali/Documents/网子图鉴/index.html`
  - Interactive web catalog with brand filter capsules, school tabs, search bar, timeline, and image modal galleries.
- **Visual Assets**: `/Users/kali/Documents/网子图鉴/images/`
  - 404 high-resolution macro optical photographs (>5KB, 0 SVG/CAD, 0 MD5 collision).
- **Automated Verification Test Suite**: `/Users/kali/Documents/网子图鉴/scratch/verify_and_audit_catalog.py`
  - 45 existing test suites, expanding to 50 comprehensive tests covering R1-R5 and Acceptance Criteria 1-5.
- **Audit Memory & Ledger**:
  - `/Users/kali/Documents/网子图鉴/scratch/purged_non_genesis_memo.json`: 14 blacklisted non-Genesis models defense record.
  - `/Users/kali/Documents/网子图鉴/AUDIT_LEDGER.md`: Comprehensive 108-model audit ledger report.

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| F1 | 12项标准化技术规格全量核验 | 108款雾化器12项标准规格键100%存在且非空，无缺失与估算歧义 | M1, M2 | Survey Explorer 1 |
| F2 | 纯血创世纪物理机制与黑名单防御 | 100%立式微孔网管/陶瓷棒加热，0网片，0棉花台，14款非网子黑名单0回流 | M1, M2 | Survey Explorer 1 |
| F3 | 零克隆与反抄袭规范 | 全馆108款及代码中“精工”克隆词检出率为0% | M1, M2 | Survey Explorer 1 |
| F4 | 导油介质纯度规范化提纯 | 将kraken、le_zephyr等4款导油介质中的玩家棉花历史实验说明移至officialNotes | M2 | Survey Explorer 1, 3 |
| F5 | 404张实拍图真机对版与完整性 | 404张实拍物理存在、>5KB、100%真机实拍（0 SVG/CAD） | M1 | Survey Explorer 2 |
| F6 | 零MD5碰撞与防伪审计 | 404张实拍MD5完全唯一（0碰撞），0批发商水印，0克隆标 | M1 | Survey Explorer 2 |
| F7 | 单款高分辨率微距覆盖度 | 108款模型100%配备>=3张微距实拍（证件照、底座微距、拆解图等） | M1 | Survey Explorer 2 |
| F8 | 编年史双源证据链核查 | 97款确证模型YYYY年M月标准格式及一手原厂+二手评测双源互证 | M1, M3 | Survey Explorer 3 |
| F9 | 待考证模型历史断代成因核查 | 11款待考证模型标注约YYYY年(暂定)并详述历史阻断成因 | M1, M3 | Survey Explorer 3 |
| F10 | 时间轴连续性与历史断代自洽 | 2012-2024年编年时间轴连续单调递增，2019/2022断代真实合理 | M1, M3 | Survey Explorer 3 |
| F11 | Luca Creations筛选胶囊匹配缺陷修复 | 修正generate_html.py中luca过滤条件，杜绝gbell误匹配，确保显示2款 | M2 | Survey Explorer 3 |
| F12 | index.html全量重新编译同步 | 重新编译前端，确保筛选胶囊、时间轴、搜索、模态框数据100%一致 | M2 | Survey Explorer 3 |
| F13 | 自动化测试套件扩充至50大项 | 扩充胶囊过滤、图片魔数、规格正则、介质纯度、信源资质等测试 | M1 | Survey Explorer 3 |
| F14 | 全量测试100% PASS回归 | 执行python3 scratch/verify_and_audit_catalog.py实现0 Failure, 0 Error | M3 | Survey Explorer 3 |
| F15 | 全馆逐款全息审计总账报告 | 输出覆盖108款逐款审计结论、物理参数、历史证据与修正记录的AUDIT_LEDGER.md | M3 | All Explorers |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | E2E Testing Suite Expansion | 在`scratch/verify_and_audit_catalog.py`中扩充Test 46-50，发布`TEST_READY.md` | Survey Complete | DONE (`483c48d1-19d5-405b-ac21-4e0c131dc647`) |
| M2 | Data & Frontend Rectification | 修复`generate_html.py`中Luca胶囊过滤Bug，纯化导油介质，重新编译`index.html` | M1 | DONE (`82931437-89d7-4b47-a44b-1a07b5a442f3`) |
| M3 | Final Regression & Audit Ledger | 全量回归50项测试(100% PASS)，生成全馆108款全息审计总账报告`AUDIT_LEDGER.md`，执行Forensic Audit与Gate验收 | M1, M2 | DONE (`c51be77b-ba23-483e-8081-d03b91306189`, `c1d2fbac-2fd3-4c3b-addf-7b438966cbc0`) |

## Interface Contracts
### Data Schema (`generate_html.py` -> `index.html`)
- Each item in `data`:
  - `id`: unique string identifier matching image filename prefix (e.g. `paravozz_v1`)
  - `name`: official atomizer model name
  - `brand`: official manufacturer / workshop / modder name
  - `school`: one of Eastern European (`'东欧车头/俄系'`), Western (`'欧美拓荒与殿堂名作'`), East Asian/China (`'东亚日韩与国创先锋'`)
  - `year`: integer year (2012 - 2024)
  - `specs`: dictionary with exactly 12 keys:
    `['设备类型', '品牌产地', '发布时间', '外形直径', '本体高度', '油仓容量', '主体材质', '电极平台', '导油孔径', '导油介质', '进气规格', '接口规格']`
  - `images`: list of >= 3 image paths under `images/`
  - `dateVerification`: dictionary with keys:
    - `status`: `'confirmed'` or `'tentative'`
    - `primary`: primary archive evidence URL / statement
    - `secondary`: secondary review / forum thread archive URL / statement
    - `analysis`: detailed historical analysis / blocking reasons
  - `officialNotes`: historical modder notes, design context, and player experiments

### Test Runner Contract (`scratch/verify_and_audit_catalog.py`)
- Invocation: `python3 scratch/verify_and_audit_catalog.py`
- Exit code: 0 on 100% PASS (0 failure, 0 error).

## Code Layout
- `generate_html.py`: Master dataset and HTML generator
- `index.html`: Compiled static application
- `images/`: Image gallery (404 JPEG images)
- `scratch/verify_and_audit_catalog.py`: Python unittest suite (50 tests)
- `scratch/purged_non_genesis_memo.json`: Non-Genesis blacklist definitions
- `AUDIT_LEDGER.md`: Comprehensive 108-model audit ledger report
