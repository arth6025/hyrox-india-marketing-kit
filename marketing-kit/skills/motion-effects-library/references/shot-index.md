# Shot and effect index

Lookup table for `motion-effects-library`. Paths are relative to the plugin root. Shotcraft cards are written in Chinese (Apache-2.0, re-implemented from scratch by the author, see `engines/shotcraft/references/shots/ATTRIBUTION.md`); the one-line summary and duration are copied from each card's frontmatter and Claude translates on read. Every card is a Remotion recipe (React) and needs a local agent to render; the **Sloosh approximation** column says what the MCP alone can do.

## How to read a card

Each shotcraft card has: `一句话` (one line: what moves), `适用` (when to use), `时长` (length, frames@fps), `能量` (energy), then `## 意图` (intent), the timing table and the demo source path under `engines/shotcraft/assets/`. Charlie effects live in one file with start state, end state, timing and the premium detail. Cinetic techniques carry a seed line and the measured curve.

## Shotcraft · Opening and brand (11 cards)

| Card | One line (zh) | Length | Path |
|---|---|---|---|
| `brand-ink-open` | 墨线十字准星描画→字标逐字压印→打字机副标→满一秒静止再上浮消散 | 约 2.8s（83f） | `engines/shotcraft/references/shots/opening/brand-ink-open.md` |
| `crane-rise-reveal` | 升降臂拉升揭示——开场怼在一行数据特写，相机沿 Y 轴减速升起后拉，行行涌入直到整面 dashboard 铺满全幅 | 5.5s（165f：特写 hold 24f + 拉升 102f + 落定/余波/ | `engines/shotcraft/references/shots/opening/crane-rise-reveal.md` |
| `dataviz-landscape-open` | 暗场支流线束地景开场——多条流线汇入主干、虚构 ID 标签浮在线上、相机重景深低速飞越 | 5–8s（开场氛围段，一支片 ≤1 次；demo 180f） | `engines/shotcraft/references/shots/opening/dataviz-landscape-open.md` |
| `fracture` | 5×5 瓦片从 3D 碎片态按中心波纹逐圈聚合成整面海报，停一拍亮字，随后全部碎片背离中心加速旋转飞出画面 | 约 5.2s（156f@30fps；聚合 0–2.6s · hold 1s ·  | `engines/shotcraft/references/shots/opening/fracture.md` |
| `icon-field-colorize` | 灰阶小图标点阵错峰浮现铺满全屏，停一拍后多道品牌色横带波纹极快向下扫翻全场——"功能全景先摆满，品牌一瞬间点亮"的开场/收束卡 | 浮现 ~45f 错峰 + 静置 ~10f + 翻色 12–45f + 终态静置； | `engines/shotcraft/references/shots/opening/icon-field-colorize.md` |
| `letterspace-materialize` | 大字距字标全字符并行连续描画结晶——所有字母同帧起笔、笔画像手写一样连续生长、同帧齐收成词；氛围底景上的品牌字标显影 | 静置 ~15f + 描画 ~50f + 终态静置 ≥30f；全段 3–4s | `engines/shotcraft/references/shots/opening/letterspace-materialize.md` |
| `magician-card-flourish` | 午夜蓝暗场上蓝色星芒闪现 0.3s（X 形针状光束旋转 90°+中心辉光放射小光芒），卡片从闪光点弹射而出——极速自旋弧线飞向镜头、自旋随靠近衰减、瞬间硬定格（卡高 86% 画高）、光脉冲 + sheen 扫光，右侧文案 | 156f（闪光 0.3s + 飞行 1.6s + 定格/扫光/文案揭示 + ho | `engines/shotcraft/references/shots/opening/magician-card-flourish.md` |
| `orbit-ring-title-open` | 石墨暗场上八张 16:9 暗色内容卡按 45° 均布在 720×380 椭圆上匀速公转（卡身永不倾斜，纵深只由 sin θ 给出 ±12% 缩放、z 序与远处压暗失焦），环撑开期间卡内容冻结首帧、f24 之后八张一起开播 | 150f（5s@30fps；马克块 f64 落定后 2.9s 稳态巡回 + 极缓 | `engines/shotcraft/references/shots/opening/orbit-ring-title-open.md` |
| `spotlight-hero-card` | 关灯的剧场里一束钨丝聚光（带体积光柱）扫过页面锁定一张卡，斜侧推进后卡片弹起悬浮、香槟色光束沿轮廓两圈、连同 3D 注记一起贴回原位 | 172f（约 5.7s；锁定 f34 → 触地 f142 → 30f 真静止 h | `engines/shotcraft/references/shots/opening/spotlight-hero-card.md` |
| `stroke-segment-build` | 断笔成字——标题拆成十几段互不相连的笔画乱序逐段点亮，前 70% 不可读，末段落位瞬间语义"啪"地成立 | 165f（5.5s；揭晓 f105 后 hold 2s） | `engines/shotcraft/references/shots/opening/stroke-segment-build.md` |
| `text-as-mask` | 文字视频遮罩——瓷白舞台上切出超粗大标题字，字内部透出缓慢平移的暗色实时产品面板，结尾吸一口气后字形指数冲入放大 46 倍溢出、内部画面接管全屏 | 165f（入场 18f + 字内漂移 78f + 吸气 8f + 冲入接管 24 | `engines/shotcraft/references/shots/opening/text-as-mask.md` |

## Shotcraft · Camera (10 cards)

| Card | One line (zh) | Length | Path |
|---|---|---|---|
| `basic-3d-scene` | impress.js 式空间演示：卡片以不同位置/旋转/缩放散布 3D 空间，相机取各步姿态之逆依次飞行对齐，末步拉到 OVERVIEW 总览 | 约 7.5s（225f@30fps；四站，三段飞行 28/32/32f，每站停留 | `engines/shotcraft/references/shots/camera/basic-3d-scene.md` |
| `crash-zoom-punch` | 全景一拍急推到目标特写（6f），落位二选一——过冲回弹（弹性）或撞停震屏（重量） | 约 0.5s 动作 + 前后 hold（动作 6–11f，前 hold ≥30f | `engines/shotcraft/references/shots/camera/crash-zoom-punch.md` |
| `cursor-flyover` | 整页俯瞰后，相机依次飞到四个功能区 zoom-in 特写，SVG 光标先一步到位指点、点击留下涟漪并触发界面响应，最后拉回俯瞰 | 约 8.0s（240f@30fps；俯瞰 22f · 四站各 44f（飞行 20 | `engines/shotcraft/references/shots/camera/cursor-flyover.md` |
| `depth-layer-moves` | 分层深度运镜——多层视差滑轨：3 层速度梯度横移出纵深，滑轨落定时主角浮起 | 4–5.5s 持续（demo 165f） | `engines/shotcraft/references/shots/camera/depth-layer-moves.md` |
| `graze-face-tour` | 大倾角贴面游走特写——镜头贴着 UI 表面低飞掠过（侧栏树/顶栏/列表当地形），页面文字初始悬浮在界面上空带同形软影，随镜头行进先后加速贴落回界面 | 单段 4–5s；可多段接力延长 | `engines/shotcraft/references/shots/camera/graze-face-tour.md` |
| `overhead-camera-moves` | 俯拍揭示两式——tilt-reveal 俯仰抬正揭示、overhead-tabletop-drop 桌面卡阵横滑骤降扎入 | A 120f（4s）/ B 140f（4.7s） | `engines/shotcraft/references/shots/camera/overhead-camera-moves.md` |
| `space-camera-moves` | 3D 空间化运镜两式——exploded-view 爆炸分解（构件沿 Z 炸开再合体）、drone-dive-landing 无人机俯冲降落 | A 170f（5.7s，炸开-悬停-合体-收尾标题全程）；C 105f（3.5s | `engines/shotcraft/references/shots/camera/space-camera-moves.md` |
| `steep-tilt-glide` | 固定镜头下直立页面以 60° 强透视侧立（右近左远），页面自身沿其 3D 横面方向滑移掠过镜头（物动镜不动），滑移带速度重影、文字组件悬空贴落、由暗揭亮 | 4s（120f）单镜；页面越宽越可拉长 | `engines/shotcraft/references/shots/camera/steep-tilt-glide.md` |
| `tension-camera-moves` | 情绪运镜两式——bullet-time 冻结环绕、pull-back 拉远孤立，相机替观众"感受"而非"看" | 单式 5–6s（150–170f）；全片合计 ≤2 式（各 ≤1 次） | `engines/shotcraft/references/shots/camera/tension-camera-moves.md` |
| `terminal-3d` | 三个终端窗散布 3D 空间，相机窗间飞行、途中正弦拉远，每到一窗打字机敲命令、结果逐行滑出——命令执行的空间叙事流 | 约 8.2s（246f@30fps；三站各约 2–3s 停留 + 两段 30f  | `engines/shotcraft/references/shots/camera/terminal-3d.md` |

## Shotcraft · Transitions (15 cards)

| Card | One line (zh) | Length | Path |
|---|---|---|---|
| `bottom-push-stack-wipe` | 底边上推换章——新场景连底色整屏从底边向上推入，把旧场景物理顶出画外，连推数章各配一种饱和底色，内容钉死在各自色底坐标系里随底色走 | demo 三连推 170f（~5.7s）；单次推入 26f + 章内 hold  | `engines/shotcraft/references/shots/transition/bottom-push-stack-wipe.md` |
| `card-flip-reveal` | 功能卡 3D 翻面揭示——卡片沿 Y 轴翻 180°，正面 UI 翻到侧棱最薄处掠过一道随角度移动的受光，背面揭出大号结论数字，逐张错峰扫过整排 | 全程 150f（~5s，含 hold）；单卡 4f 预备 + 16f 翻 + ~ | `engines/shotcraft/references/shots/transition/card-flip-reveal.md` |
| `card-flock-tumble` | 三张 UI 页卡从侧棱薄边 3D 翻飞成阶梯站定（全程清晰、样条连续丝滑），站定后保持慢转不停，快速收束吸入中心，炸出单个湍流烟雾环扩散，巨字横贯收场 | 翻飞 ~1.5s + 慢转展示 ~0.3s + 收束 0.3s + 烟环+巨字  | `engines/shotcraft/references/shots/transition/card-flock-tumble.md` |
| `circle-match-iris` | 圆心匹配光圈切——光圈从页面上圆形元素的圆心炸开，圈内新页的圆形图表接在同一个圆上；匹配剪辑给光圈一个语义锚点 | 5.5s / 165f（入场+定睛 40f + 蓄力 7f + 接圆开圈 37f | `engines/shotcraft/references/shots/transition/circle-match-iris.md` |
| `gradient-transition` | 背景在 linear、radial、conic 三类 CSS 渐变间平滑过渡——角度、色标、中心、半径逐参数插值，段间交叉淡化换类型 | 约 6.7s（200f@30fps；linear 0–2.3s · radial | `engines/shotcraft/references/shots/transition/gradient-transition.md` |
| `line-carry-transition` | 线条接力横移转场——场景 A 的进度条延伸出画，镜头跟线横移，线在移动中拐角围出场景 B 的卡框，全程无剪切 | ~6.3s / 190f（进度条走满 36f + 冲出 10f + 横移 56f | `engines/shotcraft/references/shots/transition/line-carry-transition.md` |
| `mosaic-reframe` | 12 张瓦片在规则网格、feature mosaic、对角瀑布串三种排版间连续变形，位置宽高各自插值、逐片微错峰，段间留 hold | 约 7.1s（214f@30fps；浮现 0–22f · hold A · A→ | `engines/shotcraft/references/shots/transition/mosaic-reframe.md` |
| `page-turn-transitions` | 整页体块转场——barn-door-split 对开门裂幕（旧页裂两半滑出、新页迎上） | 单式 150f（前态建立 30–40f + 转场 24–40f + 跟随与收尾  | `engines/shotcraft/references/shots/transition/page-turn-transitions.md` |
| `print-texture-transitions` | 印刷质感转场——ink-bleed-reveal 墨渗揭示（须状渗边洇开吃掉旧景） | 4–4.5s（洇开段 55–80f + 静止收尾 ≥30f） | `engines/shotcraft/references/shots/transition/print-texture-transitions.md` |
| `shot-transitions` | 镜头交棒三式——推进流白、whip-pan 甩镜（急刹款）、mask-wipe 穿窗（纵深款），按能量落差与接缝语义选型 | n/a（技法卡；各式占用帧数见参数表，从相邻镜头预算里划） | `engines/shotcraft/references/shots/transition/shot-transitions.md` |
| `tear-streak-transitions` | 撕裂转场——glitch-displace 噪声撕裂（16 横条错位抖动中硬切），数字故障语义的条带级撕裂 | 前态 ≥40f + 撕裂 16–24f + 收尾 ≥40f，约 4.5s（135 | `engines/shotcraft/references/shots/transition/tear-streak-transitions.md` |
| `transition-hidden-cut` | 藏切点转场三式——前景遮挡隐形切、对撞开屏、暖色漏光，硬切藏进遮挡/撞击/光峰的 1-3 帧里，观众看不见剪刀 | n/a（技法卡；各式占用帧数见参数表，从相邻镜头预算里划） | `engines/shotcraft/references/shots/transition/transition-hidden-cut.md` |
| `transition-travel` | 穿越式转场——字腔穿越：巨型章节标题的字形就是一扇窗，镜头钻进字形笔画完成换景 | n/a（技法卡；demo 150f，主推动作段 52f，前后 hold 另计，帧 | `engines/shotcraft/references/shots/transition/transition-travel.md` |
| `white-flash-logo-simplify-cut` | 液态金属质感的彩色词标静置流光，蓄力后从字心炸出一记白闪过曝，曝光回落时同一位置已是扁平版字标——一次闪白完成质感降维 | 约 4s（120f@30fps；演出 0–34f · 蓄力 34–46f · 冲 | `engines/shotcraft/references/shots/transition/white-flash-logo-simplify-cut.md` |
| `wipe-transitions` | 几何擦除转场——blinds-slice 百叶窗切条（12 根 3D 叶片错峰翻面成波，波扫过后整页由 A 换成 B） | 前态 ≥20f + 擦除 ~56f + 收尾 ≥40f，约 4.4s（132f） | `engines/shotcraft/references/shots/transition/wipe-transitions.md` |

## Shotcraft · Typography (22 cards)

| Card | One line (zh) | Length | Path |
|---|---|---|---|
| `blur-slide` | 标题逐词入场，y 0.38em→0 + blur 18→0 + opacity 0→1 三通道走同一条 ease-out 同步收敛，词间隔约 4f；副标题在标题收完前就错峰跟进 | 约 4.0s（120f@30fps） | `engines/shotcraft/references/shots/typography/blur-slide.md` |
| `brace-expand` | 一对紧贴的小花括号先在正中出现，随即带一次过冲向左右弹开并放大到标题级，文字 clip 宽度严格绑括号内缘、像被拉开幕布般从中间揭示，落定后字距再细微松弛 | 约 4s（120f@30fps：光标 0–6f → 6f 小括号硬切 → 14f | `engines/shotcraft/references/shots/typography/brace-expand.md` |
| `countdown-arc-scatter` | 纸面表盘 9 个等大数字沿大弧切向排布，整盘扫过 96° 后减速急停，"5" 停在弧顶随即平移落位成标题首字符，其余数字带 blur 原地散去，标题逐词模糊淡入、末词转强调色 | 约 3.3s（100f@30fps：扫动 ~30f + 落位 20f + 标题成 | `engines/shotcraft/references/shots/typography/countdown-arc-scatter.md` |
| `document-typewriter-reveal` | 悬浮在暗场里的整页真排版文档窗口在光标后自己"写"出来、侧栏跟进、历史条目逐个落入轨道，相机从斜侧标题特写一路后撤到全窗 | 150f（约 5s，含 history-list-stack 尾段与标语 hol | `engines/shotcraft/references/shots/typography/document-typewriter-reveal.md` |
| `flying-words` | 22 个关键词按黄金角铺在扁椭圆截面上，沿 z 轴从远处飞到相机前擦身而过，透明度走 [0,1,0.5,0.2,0] 生命曲线，跑满 2 整圈首尾无缝 | 约 6.0s（180f@30fps，2 个完整循环，可无缝接续） | `engines/shotcraft/references/shots/typography/flying-words.md` |
| `glitch-cycle` | 同一行等宽槽位循环轮播 4 条状态短语，每条头尾按概率关键帧 [1,0,0,0.1,0,0,1] 全乱码、中段偶发单字抖动，切换瞬间叠 RGB 分离与整行位移；末条概率收 0 保证收尾干净 | 约 5.6s（168f@30fps；demo 每条短语 38f，末条延续到片尾作 | `engines/shotcraft/references/shots/typography/glitch-cycle.md` |
| `gradient-word-sweep` | 黑底标语里关键词被渐变彩光从左到右快速扫过"充能"——波前字符辉光最强向后衰减，填满后字符间勾连细紫红闪电、整词稳态泛光呼吸 | 扫充 ~15–20f（要快）+ 稳态闪电呼吸 1–2s；全段 2.5–3.5s | `engines/shotcraft/references/shots/typography/gradient-word-sweep.md` |
| `lead-word-zoom-assemble` | 首词以 2.3 倍字号占据画面中央、hold 期间继续推近 6%，随后一条曲线同时完成「缩回终字号」与「整行左滑归位」，后续词各自从槽位右侧 0.5em 被推进来；支点横向钉首词中心、纵向钉基线（挂载时实测），整行上移的 | 约 2.8s（84f@30fps；组句 f36 完成、上移与副行 f32–46、 | `engines/shotcraft/references/shots/typography/lead-word-zoom-assemble.md` |
| `marker-underline-title` | 大标题落定后，关键词下方马克笔下划线从左到右快速描画——变宽笔形、毛糙边缘、微上斜跟随斜体字势，贴着字底 | 标题落定 +4~8f 后起笔，划线 8–12f，总 1–1.5s | `engines/shotcraft/references/shots/typography/marker-underline-title.md` |
| `outline-word-fill` | 空心词（细暖灰描边、500 字重）从 3.2 倍急缓收缩落位，虚线大圆随后从 2.8 倍收到字周围并缓慢自转，左右水平虚线从画框边缘内伸；描边先微微增亮，实心白热字在一帧内硬切点亮，一闪辉光即定格 | 约 3.0s（90f@30fps，短促单拍 + 36f 落定） | `engines/shotcraft/references/shots/typography/outline-word-fill.md` |
| `paper-title-card` | 一句话逐词压印上纸、一个词标强调色斜体、短划线收束 | 1.7–1.8s（50–55f） | `engines/shotcraft/references/shots/typography/paper-title-card.md` |
| `pill-chip-slot-cycle-handled` | 白底句式 "Your `chip` Handled" 里深色胶囊内词竖向滚轮轮换，胶囊宽度按预量文本宽插值平滑伸缩、两侧文字被自然挤开收拢，胶囊上下露出 13% 透明度的灰色幽灵项 | 约 5.0s（150f@30fps：静置 → 3 次切换（0.25/0.47/0 | `engines/shotcraft/references/shots/typography/pill-chip-slot-cycle-handled.md` |
| `pill-slot-cycle` | 句中词槽轮换——固定句干钉死不动，句尾 pill 徽章每 ~0.7s 老虎机滚一格（旧的上飞加速淡出、新的从下带模糊滑入），连换 N 个功能词后落成完整句子收束 | 入场 12f + 每拍 21f × 词数 + 收束 14f + hold；6 词 | `engines/shotcraft/references/shots/typography/pill-slot-cycle.md` |
| `text-column-converge` | 双词对峙合拢——左"NEW"右特性词钉死在等屏边距两侧硬切轮换、全程零收缩，换到最后一词才唯一一次 ease-in-out 滑到居中咬合成短语，下方小字近乎硬切浮现；收尾揭晓型文字卡 | 轮换 7–16f/词 × 8–9 词 + 合拢 ~36f + 小字后静置；全段约 | `engines/shotcraft/references/shots/typography/text-column-converge.md` |
| `title-demote-to-label` | 大标题降格为节标签两式——A 大标题居中显影站稳一拍后连续缩小 0.3x 平移到左上角落成小节标签、内容区在其下生长；B 同套路但登场时带文本选中态高亮块扫入再撤掉 | A ~3.7s（112f）/ B ~4.5s（134f）；demo 两式串播 2 | `engines/shotcraft/references/shots/typography/title-demote-to-label.md` |
| `type-assembly-moves` | 文字集结三式——split-text-stagger 逐字裂升、letterform-drift-assembly 漂移合拢、text-on-path 沿线流入 | 单式 4–5.5s（动作段 A ~56f / B ~104f / C ~110f | `engines/shotcraft/references/shots/typography/type-assembly-moves.md` |
| `type-entrance-moves` | 标题文字入场一式——letter-drop-physics 字符坠落（重力砸落、弹跳、歪斜站定，最后一拍集体立正归位） | 单式 5s（含 hold 与静止收尾；动作段 ~116f，demo 150f） | `engines/shotcraft/references/shots/typography/type-entrance-moves.md` |
| `type-rhythm-sync` | 文字随声同步两式——font-weight-pump 字重脉冲（笔画随鼓点变粗弹回）与 karaoke-fill-sync 卡拉OK填色（词随旁白逐个点亮） | A FontWeightPump 165f / B KaraokeFillSyn | `engines/shotcraft/references/shots/typography/type-rhythm-sync.md` |
| `typewriter-moves` | 打字机 error-retype——误删重打的"改口"三幕剧：打出平庸词 → 犹豫 → 退格删掉 → 更快打出卖点词 | ~5.3s（160f） | `engines/shotcraft/references/shots/typography/typewriter-moves.md` |
| `vertical-word-roll-blur-cycle` | 句尾词换成竖向滚轮，3 次换词各 0.55s（outQuint 七成 + outBack 三成，前快后极慢带微过冲），相邻行按距离上垂直 blur 与灰度，中心词落定瞬间从灰染成强调色 | 约 5.0s（150f@30fps：静置 → 3 次换词 → 尾部整组淡出） | `engines/shotcraft/references/shots/typography/vertical-word-roll-blur-cycle.md` |
| `word-relay-filmstrip` | 左列黑白相间等高页面卡步进滚动（焦点卡全亮、邻卡离焦压暗）、右侧衬线大词原位接力（名词恒定+动词轮换）——切词瞬间才滚动一格，词块垂直中心与当前页面卡中点精确对齐 | 每词期 ~1.5–2s × 3–4 词；demo 180f（6s） | `engines/shotcraft/references/shots/typography/word-relay-filmstrip.md` |
| `word-relay-geometry` | 三个利益词各带一套专属几何接力——虚线大圆减速自转 + 彗星弧飞跑 → 三实线圆 trim 依次生长后收拢咬紧 → 镀铬金属 sheen 扫过后一拍收成纯白；旧词缩到 0.86 淡出，新词描边→填充揭示 | 约 6.0s（180f@30fps：三段各 ≈60f，段间重叠 6f） | `engines/shotcraft/references/shots/typography/word-relay-geometry.md` |

## Shotcraft · UI entrance (21 cards)

| Card | One line (zh) | Length | Path |
|---|---|---|---|
| `avatar-bracket-carousel` | "Your ___ agent" 填空排版，四角对焦框钉在句中不动，头像队列在框内垂直 spring 轮换三次，入框放大清晰、出框按距离缩小淡化模糊，角色标签同步更换，切换瞬间对焦框呼吸 7% | 约 5.2s（156f@30fps） | `engines/shotcraft/references/shots/ui-entrance/avatar-bracket-carousel.md` |
| `bezier-source-converge-merge` | 左侧四个来源节点各有一条细贝塞尔曲线连向右侧同一汇聚点，曲线先错峰由左向右 draw-on，节点沿自己的曲线滑向汇聚点并三段式加速缩小到消失，强调色数据包全程沿路径滑行，吞并完成后曲线从左端反向擦除只留品牌标志（demo | 约 5.6s（168f@30fps） | `engines/shotcraft/references/shots/ui-entrance/bezier-source-converge-merge.md` |
| `card-stack` | 一组模板卡（demo 9 张）从屏幕下方逐张 spring 弹入、越落越快叠成一摞，全员落位后整摞一次性展成扇面——每张按序号偏转 6.5°、横移 138px，最后中心卡被抽出 | 约 5.0s（150f@30fps） | `engines/shotcraft/references/shots/ui-entrance/card-stack.md` |
| `carousel-3d` | 8 张卡排成圆环整环自转一圈（匀速底 + 每 45° 一次停靠的分步），每卡只绕 Y 公转、自身 billboard 朝外，正反两层同向贴图配 backface-visibility:hidden 保证任何时刻都正立不倒 | 约 5.6s（168f@30fps） | `engines/shotcraft/references/shots/ui-entrance/carousel-3d.md` |
| `cloner-depth-echo` | 克隆纵队——主卡瞬间"复印"出 7 个半透明分身沿斜向纵深排开成队，停一拍后全体加速吸回本体合一+弹跳 | 138f（约 4.6s） | `engines/shotcraft/references/shots/ui-entrance/cloner-depth-echo.md` |
| `deck-deal-flyin` | 暗色石墨桌面上的实体牌堆特写环绕开局，灯从牌堆亮到旁边的页面板，一摞卡像发牌一样硬加速甩进网格，相机追着发牌升起后仰、落在整块满板的跑道式俯瞰上定格 | 150f（约 5s：0–36 牌堆特写 + 预备，36–~101 发牌，108– | `engines/shotcraft/references/shots/ui-entrance/deck-deal-flyin.md` |
| `doc-park-left-pill-deal` | 文档不淡出而是向左滑出只露约 35% 宽并微缩到 0.92，右侧按旁白节奏慢速发牌三张白底描边药丸（outBack 弹入），每张落定后其下方字幕逐词加深、下一张到来前整句淡出，左侧文档全程极缓慢自动滚动保持"正在被读" | 约 5.8s（174f@30fps） | `engines/shotcraft/references/shots/ui-entrance/doc-park-left-pill-deal.md` |
| `draw-svg-trace` | 描边生长圈注——一条带笔头的墨线沿元素轮廓跑一圈把它"画"出来，闭合瞬间闪黑交棒、内容淡入；同套路可给标题画下划线 | 132f（预告 10f + 描边 40f + 闪黑交棒 16f + 下划线 18 | `engines/shotcraft/references/shots/ui-entrance/draw-svg-trace.md` |
| `element-body-moves` | 元素身体感——contact-shadow-lift 接触阴影离面抬升：卡抬起时桌上的阴影同步放大变淡，纸片离桌被阴影证明 | A 150f 5s | `engines/shotcraft/references/shots/ui-entrance/element-body-moves.md` |
| `integration-hub-map` | 旧页面一次性快翻 180°（侧棱瞬间亮闪）落成新中枢页，五个集成 app 图标同帧弹现、随即五条彩虹光管同帧齐连，光管内输送脉冲持续流动——"翻开新一页，生态一齐接入" | 前摇 ~0.5s + 快翻 ~1.2s + 图标齐现 → 光管齐连两拍 ~0.7 | `engines/shotcraft/references/shots/ui-entrance/integration-hub-map.md` |
| `list-reveal` | 垂直菜单 6 项按 10f 的间隔依次 scale 找位、软 back 轻微过冲落定，同时整个列表容器全程匀速上移——逐项入场与整体漂移是两层不相干的运动 | 约 4s（120f@30fps） | `engines/shotcraft/references/shots/ui-entrance/list-reveal.md` |
| `list-stack-press` | 列表卡从画面底部逐张飞上摞起，每张落地压弹整摞、计数器同步跳一格 | 约 3s（18–88f） | `engines/shotcraft/references/shots/ui-entrance/list-stack-press.md` |
| `neon-frame-forerun` | 强透视直角霓虹框自左缘两头奔画先行成型，页面在框内由暗转亮，同时框内组件/文字从 3D 上空带同形软影错峰贴落、随页面点亮同步完成贴合，背景霓虹群（demo 为同形框纵深回声隧道）终段熄灭让位 | 框奔画 ~0.7s + 点亮&贴落 ~2.7s + 背景熄灭收束 ~1s；全段  | `engines/shotcraft/references/shots/ui-entrance/neon-frame-forerun.md` |
| `neon-frame-orbit-drop` | 霓虹框先行描框后，镜头绕页面左→右弧线旋转，页面全部组件/文字**同帧**从空中往下贴合（同形软影同步收敛）——整体登场式的框内安放 | 描框 ~0.5s + 旋转&同时贴落 ~2.5s + 落定 ~1s；全段 ~4. | `engines/shotcraft/references/shots/ui-entrance/neon-frame-orbit-drop.md` |
| `page-waterfall-wall` | 页面瀑布墙——真实页面截图切成 3–4 列在 3D 后仰墙面上差速反向无限滚动，视差 + 镜头缓推做"内容多到流不完"的一览 | 4–6s（无限循环体，时长由段落需要裁） | `engines/shotcraft/references/shots/ui-entrance/page-waterfall-wall.md` |
| `product-card-progressive-assemble` | 详情卡像被逐字段抓取般自建——一枚"填充光标"领先跳格，图→标题→分类 pill 依次 pop→原价出现后被划线降级、强调色新价 spring 跳出→正文逐行揭示且高亮块由左向右刷过→色卡点亮→按钮填满，整卡全程极慢 s | 约 5.7s（172f@30fps） | `engines/shotcraft/references/shots/ui-entrance/product-card-progressive-assemble.md` |
| `radial-wave` | 17×9 圆点阵列按到波源的欧氏距离错峰点亮，每点 scale 过冲到 1.5 再落回常亮，第一道波扫完后第二道亮蓝脉冲从外圈反向收拢回中心 | 约 3.8s（114f@30fps） | `engines/shotcraft/references/shots/ui-entrance/radial-wave.md` |
| `research-card-stack-scroll` | 深色论文卡每 12 帧一张沿右下轴线飞入中心叠压，落位带 1 帧压缩，只有最上一张全清晰渲染标题+作者+摘要，下方卡按堆积深度递增模糊变暗只露标题条，背景横向 grid 同步下移做速度参照 | 约 4.8s（144f@30fps） | `engines/shotcraft/references/shots/ui-entrance/research-card-stack-scroll.md` |
| `row-embed` | 内容行像卡片一样从空中降下、rotateX 收平、嵌入瞬间底边亮一道强调色的缝 | 约 2s（12–68f） | `engines/shotcraft/references/shots/ui-entrance/row-embed.md` |
| `value-stagger-gradient` | 16 根柱入场时 delay 是时间错峰，同时高度/色相/位移/模糊四个属性各自铺成从首到末的数值梯度；第二拍把错峰原点换成中心，脉冲幅度以中心为最大重新铺开 | 约 5.0s（150f@30fps） | `engines/shotcraft/references/shots/ui-entrance/value-stagger-gradient.md` |
| `wall-reveal-moves` | 整墙批量入场两式——bento 逐格点亮、蓝图描线成形，全部原位显形不位移，与 deck-deal-flyin 的飞入位移型互补成品类矩阵 | 单式约 5s（A 150f / B 150f @30fps，含建立 hold 与 | `engines/shotcraft/references/shots/ui-entrance/wall-reveal-moves.md` |

## Shotcraft · Interaction (11 cards)

| Card | One line (zh) | Length | Path |
|---|---|---|---|
| `autolayout-gap-dial` | 间距拨盘驱动布局——一排链接块带框选描边+缝隙间距标注，徽章数字逐格跳动、块被参数实时推开再弹簧回弹归位；"参数驱动布局"的可视化 | ~5s（150f：框选入场 + 预备回收 10f + 拉松 34f + 屏息 h | `engines/shotcraft/references/shots/interaction/autolayout-gap-dial.md` |
| `canvas-materialize-moves` | 内容"物化上画布"两式——panel-to-canvas 行倒卡（面板表格行沿弧线飞出、跨容器变形成画布卡片）与 diagram-cascade 级联生成树（prompt 打字后节点逐层弹出、连线先于节点生长） | A ~5s（150f）/ B ~6s（180f） | `engines/shotcraft/references/shots/interaction/canvas-materialize-moves.md` |
| `chip-grid-single-select-blackout` | 五个选项 chip 以 3+2 居中排布逐个淡入；选中帧先插一帧灰色按压块，紧接数帧内底色变墨黑、文字变白并做 1→1.04→1 极轻回弹，其余 chip 淡到 18% 但位置锁死；随后余项归零，黑 chip 上移收窄， | 约5.5s（165f@30fps） | `engines/shotcraft/references/shots/interaction/chip-grid-single-select-blackout.md` |
| `collab-cursor-moves` | 协作光标当演员——cast-ensemble 五光标群演氛围层（错峰飞入+正弦漂移+打字 cameo+聚拢围观） | A ~5.2s（156f） | `engines/shotcraft/references/shots/interaction/collab-cursor-moves.md` |
| `glass-pill-dictation-typing` | 一条定宽玻璃胶囊以约 1.25 倍略大弹出后缓落到位，内部自左淡到右浓铺一层强调色暖光；光标先行、随后匀速打出听写句，光（连同胶囊背后的环境光）随打字进度渐渐退去，收尾成一条中性的磨砂玻璃条 | 约3.3s（100f@30fps） | `engines/shotcraft/references/shots/interaction/glass-pill-dictation-typing.md` |
| `hashtag-to-pill-materialize` | 话题词打字实体化——居中打出 "#word"（红实心光标恒亮），1 帧硬切变成宽大胶囊标签，hold 后缩小左移落到页面标签位，再 1 帧硬切揭示成品页；"两次硬切一次滑动"的节奏骨架 | 120f（4s）——打字 ~40f + 硬切胶囊 hold ~18f + 缩移  | `engines/shotcraft/references/shots/interaction/hashtag-to-pill-materialize.md` |
| `picker-carousel-feature-cycle` | 移动端风竖向选择器——焦点药丸不动、内容穿过它，每项带明显 outQuint 减速吸附后完全静止，按到中心距离分层控制透明度/字号/灰度，落定时药丸做 scaleY 极轻呼吸 | 约3.6s（108f@30fps） | `engines/shotcraft/references/shots/interaction/picker-carousel-feature-cycle.md` |
| `segmented-thumb-hero` | 分段控件 thumb 位移当主角特写——超大胶囊 segmented control 弹簧浮入，描边箭头光标画外滑入按下，白 thumb 8f ease-out 滑到另一段，到位瞬间新图标 spring 弹出、旧图标收起 | ~3.5s（demo 110f：浮入 18f + 光标 24f + 点击 + 滑 | `engines/shotcraft/references/shots/interaction/segmented-thumb-hero.md` |
| `theme-switch-moves` | 主题切换两式——theme-sweep 斜向扫场（边界扫过处就地换肤）与 palette-ripple 组合款（⌘K 面板收缩成点、涟漪从点荡开换肤） | A 140f（4.7s）/ B 156f（5.2s） | `engines/shotcraft/references/shots/interaction/theme-switch-moves.md` |
| `type-and-filter` | 真实 UI 上打字搜索、网格自己收敛成一张卡、点击穿透进详情页 | 约 2.5s（118–190f） | `engines/shotcraft/references/shots/interaction/type-and-filter.md` |
| `voice-waveform-live` | 录音胶囊实时声纹——64 根细竖条随"说话"起伏，说话时中部高耸、停顿缩成点线，波形从右往左滚动；说→停→说→提交塌缩的完整表演 | 172f（~5.7s：入场 14f + 说 1.4s + 停 0.8s + 说  | `engines/shotcraft/references/shots/interaction/voice-waveform-live.md` |

## Shotcraft · Effects (15 cards)

| Card | One line (zh) | Length | Path |
|---|---|---|---|
| `assemble-then-type-flyin` | 空的暗底网格上，无文字的组件骨架先从四面八方飞入贴合；随后各处文字逐字从 3D 空间旋转着飞来落位，先大标题后小标注，全部落位后页面成形 | 约5.6s（168f@30fps） | `engines/shotcraft/references/shots/effects/assemble-then-type-flyin.md` |
| `aurora-bloom-bg-flip` | 浅灰底从底部升起紫橙柔焦 blob，随后整个底色在约 0.36s 内压暗到近黑、blob 压成余晖；文案同步 blur-out 换句 blur-in，换句间留空档不 cross-fade | 约5.2s（156f@30fps） | `engines/shotcraft/references/shots/effects/aurora-bloom-bg-flip.md` |
| `brand-frame-snap` | 品牌色画框语法——一圈粗纯色画框先于内容长出包住全屏，录屏窗口落进框内；模式切换时整圈画框同帧硬翻色+窗内布局同帧换，一个 borderColor 干完章节导航/状态提示/品牌露出三件事 | 单次翻色 ~4.7s（140f）；画框本身可全片驻场 | `engines/shotcraft/references/shots/effects/brand-frame-snap.md` |
| `fui-hud-moves` | FUI/HUD 准星咬合——reticle-lock-on 四个 L 形角标组成的取景框从画外飞入、超调回弹后咬合锁定目标 | 2–3s（demo 90f） | `engines/shotcraft/references/shots/effects/fui-hud-moves.md` |
| `glow-flyline-moves` | 暗场光斑与飞线三式——glow-orb-ambient 光斑底噪、flyline-arc 飞线连接、orb-flyline-relay 同帧共振组合 | A 170f（~5.7s）/ B 140f（~4.7s）/ C 165f（5.5 | `engines/shotcraft/references/shots/effects/glow-flyline-moves.md` |
| `icon-performance-moves` | 图标表演——attention-bounce 求关注弹跳（图标连跳递增+落地压扁+镜头被吸引） | 156f（5.2s） | `engines/shotcraft/references/shots/effects/icon-performance-moves.md` |
| `impact-feedback` | 命中反馈两式——hit-counter 连招计数（顿帧+伤害数字+combo 跳字）、anime-impact 动漫打击帧（负片+集中线+色散） | n/a（元素级技法，寄生在落位动作上；各式占用帧数见参数表） | `engines/shotcraft/references/shots/effects/impact-feedback.md` |
| `light-play-moves` | 光效两式——spotlight-sweep 聚光扫字、sheen 单点扫光 | A 170f ~5.7s / B 150f ~5s | `engines/shotcraft/references/shots/effects/light-play-moves.md` |
| `radial-ripple-phone-chips` | 暖沙底四层同心圆错相呼吸如水波，中央手机 mockup 屏内 feed 自动缓滚，两侧白色 chip 先后 spring pop 入场并悬浮 | 约5.6s（168f@30fps） | `engines/shotcraft/references/shots/effects/radial-ripple-phone-chips.md` |
| `riso-print-hits` | 套印错位冲击帧——riso-misregistration-hit 单发：标题撞停瞬间裂成双色 riso 印版，抖两下"啪"地套准 | 4s（120f，单发） | `engines/shotcraft/references/shots/effects/riso-print-hits.md` |
| `scan-bracket-sweep` | 文档弹到中央，四角落下 L 形取景括号，一条扫描光带拖着渐变尾迹在文档上往复扫 5 趟——文档全程静止，只有光在读它 | 约5.0s（150f@30fps） | `engines/shotcraft/references/shots/effects/scan-bracket-sweep.md` |
| `scanline-annotate-focus` | 一条扫描线自上而下匀速掠过已存在的页面，越过哪块区块的下缘，哪块就被四角取景框从外扩处弹簧收拢对准（一次过冲），随后贴出一枚逐字打出的机器标签，顶部状态行同步计数 00/06→06/06 | 约5s（150f@30fps） | `engines/shotcraft/references/shots/effects/scanline-annotate-focus.md` |
| `scanline-assemble-flyin` | 页面开场是一张只有网格与虚线槽位的蓝图画板，一条亮扫描线自上而下掠过；扫到每个槽位，该处组件就从画外飞入过冲贴合，带方向性残影模糊与落位咬合角标——扫完整页恰好装配完成 | 约5.2s（156f@30fps） | `engines/shotcraft/references/shots/effects/scanline-assemble-flyin.md` |
| `slam-entrance-moves` | 高能砸入三式——kanada-perspective-snap 金田透视急停、score-slam 比分砸落、impact-burst-kit 落点冲击套件（波及邻卡） | 单式动作段 6–22f + 冲击余波 ~16f + hold ≥45f（demo | `engines/shotcraft/references/shots/effects/slam-entrance-moves.md` |
| `spotlight-sweep-moves` | 暗场聚光显影三式——A 醒睡扫过（光到即亮光走即暗）、B 贴边泛光横摇（紫光贴 UI 边缘渗入+聚光匀速右移）、C 角落匀速显影（径向聚光从角落匀速扩张点亮全屏）；黑场里"光即叙事"的 UI 展示 | 单式 3.5–4.5s；A/B 可串联成巡礼段 | `engines/shotcraft/references/shots/effects/spotlight-sweep-moves.md` |

## Shotcraft · Data (5 cards)

| Card | One line (zh) | Length | Path |
|---|---|---|---|
| `before-after-slider-scrub` | 前后对比拉杆——"处理前/后"两版叠放，分割杆先猛甩后慢扫，杆过处新版"显影"揭出 | 4–5s | `engines/shotcraft/references/shots/data/before-after-slider-scrub.md` |
| `chart-live-moves` | 活体图表三式——oscilloscope-stream 示波流线（曲线右端实时写入+突发尖峰）、unit-dot-swarm-regroup 点阵重组（点群三幕迁徙聚成数字）、axis-rescale-shock 轴爆表 | 各 165–192f（5.5–6.4s） | `engines/shotcraft/references/shots/data/chart-live-moves.md` |
| `gauge-readout-moves` | 仪表读数两式——needle-sweep-selftest 满弧扫针（点火自检指针甩满全弧再回落真值）与 tape-scroll-fixed-pointer 滚带定针（针不动刻度带滚过+冲刺刹车） | A 140f（4.7s）/ B 150f（5s） | `engines/shotcraft/references/shots/data/gauge-readout-moves.md` |
| `scroll-brake-moves` | 长卷急刹两式——changelog-scroll-brake 基本款（高速长卷指数减速精准停位+目标抬升）与 brake-reticle-lock 组合款（急刹帧同帧准星咬合） | A 4–5s / B 5s | `engines/shotcraft/references/shots/data/scroll-brake-moves.md` |
| `timeline-travel` | 时间轴横移——镜头沿水平刻度轴加速掠过版本刻度，每过一格卡片弹立短停，末刻度急停推近 | 4–5s | `engines/shotcraft/references/shots/data/timeline-travel.md` |

## Shotcraft · Rhythm (8 cards)

| Card | One line (zh) | Length | Path |
|---|---|---|---|
| `beat-cut-moves` | 硬切当节拍乐器——连闪定格：三次白闪各硬切同一画面的一个裁切（全景→卡片→特写），快门余韵沉降后停在特写收束 | 全程 140f ≈4.7s（活素材 30f + 三闪 + hold 70f） | `engines/shotcraft/references/shots/rhythm/beat-cut-moves.md` |
| `beat-step-list-theme-cycle` | 三通道节拍器——深色场形容词列表逐拍上移一行，视口中央固定胶囊"接住"下一个词并换色，整场底色同拍跟换；行、色、场三通道锁死同一拍点 | 铺垫 30f + 每拍 18f × 拍数 + 收尾 hold；4 拍约 4.7s | `engines/shotcraft/references/shots/rhythm/beat-step-list-theme-cycle.md` |
| `panel-grid-moves` | 分格节奏——comic-panel-split 漫画斜格劈出同一主体的三个机位，咔咔咔三格定格后末格斜边吃屏成海报 | 156f ≈5.2s（全屏侧拍 20f + 三刀分格定格 + 吃屏 + 海报 h | `engines/shotcraft/references/shots/rhythm/panel-grid-moves.md` |
| `quad-split-parallel-scenes` | 画面硬切 2×2 四宫格，四个象限并行跑各自的微场景（打字、急推、逐词、交互链），关键节拍错开 3–6 帧制造信息轰炸 | 90f（3s@30fps：0–62f 并行轰炸 + 28f 终态 hold，全程 | `engines/shotcraft/references/shots/rhythm/quad-split-parallel-scenes.md` |
| `rhythm-interrupt-moves` | 打断节奏——jump-cut-punch-in 三级跳切推近：同构图三次无补间硬跳放大，逐级逼近目标 | A 135f ≈4.5s | `engines/shotcraft/references/shots/rhythm/rhythm-interrupt-moves.md` |
| `sakuga-timing-shift` | 一拍三转一拍一——元素先以每 3 帧一步的手翻书顿挫移动，高潮瞬间切成逐帧丝滑冲刺，帧率量化的突变本身就是看点 | 150f（5s） | `engines/shotcraft/references/shots/rhythm/sakuga-timing-shift.md` |
| `speed-ramp-freeze` | 帧号非线性 remap 的节奏手法——定格标注（流动→定格圈注→解冻） | 定格标注全程 158f（≈5.3s，定格段 67f ≥45f） | `engines/shotcraft/references/shots/rhythm/speed-ramp-freeze.md` |
| `trailer-grammar-moves` | 预告片语法一式——trailer-bumper 前置速剪钩子：三镜 9f 速剪 + 黑场静默一拍，再开场标题 | A ~4.7s（140f） | `engines/shotcraft/references/shots/rhythm/trailer-grammar-moves.md` |

## Shotcraft · Outro (6 cards)

| Card | One line (zh) | Length | Path |
|---|---|---|---|
| `grain-dissolve` | 整行字爆裂成沸腾颗粒噪点并浮现斜纹选区框，噪点云急速凝聚成更大号发光短字标，位移衰减归零定格 | 约 2.0s（60f@30fps；砂化 0.26–0.56s · 凝聚 1.2– | `engines/shotcraft/references/shots/outro/grain-dissolve.md` |
| `logo-shrink-wordmark-lockup` | 霓虹切口大环快速收束成中央实心小白 O、过冲刹车时换成 video-shotcraft 标志，图标左移让位，字标字母逐个滑入完成 lockup，强调色标语收尾 | 约 4.4s（132f@30fps；收束 0.1–1.2s · 让位 1.5–2 | `engines/shotcraft/references/shots/outro/logo-shrink-wordmark-lockup.md` |
| `neon-triple-marquee` | 三行对向霓虹跑马灯 recap——三连词空心霓虹灯管巨字上中下排满一面斜拍的砖墙，奇偶行反向匀速无限横滚，三行按 1/3 相位轮流点亮，结尾逐行断电 | 4–5s（demo 150f：18f 逐行点火上电 + 循环体 + 18f 逐行 | `engines/shotcraft/references/shots/outro/neon-triple-marquee.md` |
| `outro-group-photo-launch` | 全片元素从四面八方飞来围住字标合影，crane 落机位+舞台光+金尘做成发布会收场 | 约 4.8s（145f） | `engines/shotcraft/references/shots/outro/outro-group-photo-launch.md` |
| `ui-strip-away-outro` | 减法式收尾——点击 Publish 后整个编辑器 UI 从外围到中心层层错峰蒸发，黑场上只剩那颗按钮滑到屏心放大，按钮再淡出交棒字标定版 | ~4.8s（144f：光标就位 34f → 蒸发 ~40f → 按钮独占 → 字 | `engines/shotcraft/references/shots/outro/ui-strip-away-outro.md` |
| `ui-to-brand-morph` | UI 变品牌两式——icon-flip-bloom 图标 Y 轴翻扁成竖线、从竖线撑开成品牌标志（琥珀斜切随后划入）+ wordmark 逐字落定，与 input-morph-assemble 输入框收缩成取景框竖笔、三 | A ~4.3s（130f）/ B ~5.6s（168f） | `engines/shotcraft/references/shots/outro/ui-to-brand-morph.md` |

Shotcraft total: 124 cards. Sequence recipe: `engines/shotcraft/references/sequences/promo-energy-arc.md`. Template film: `engines/shotcraft/template/`.

## Charlie motion-effects (16, MIT)

All in `engines/charlie-motion/skills/motion-effects/references/effects.md`; recipe skill `engines/charlie-motion/skills/motion-effects/ENGINE.md`. One 8 s looping HTML file with `window.seek(seconds)`.

| # | Effect | Group | Sloosh approximation |
|---|---|---|---|
| 01 | Button → player | Interfaces | none; code only |
| 02 | Search → results | Interfaces | none; code only |
| 03 | Card → workspace | Interfaces | none; code only |
| 04 | Tabs → panels | Interfaces | none; code only |
| 05 | Chart morph | Data | static plate via `sensenova-u1-infographic`, no motion |
| 06 | Dashboard zoom | Data | `kling-o3` start/end frame push-in on two stills |
| 07 | Spring stack | Data | none; code only |
| 08 | Magnetic dock | Data | none; code only |
| 09 | Masked type | Type | `kling-o3` morph between two GPT Image 2.5 text frames (≤ 4 words) |
| 10 | Elastic type | Type | same as 09; glyphs may wobble |
| 11 | Text → layout | Type | none; code only |
| 12 | Image reveal | Type | Space `tear-away-reveal`; or `image-to-video` with a reveal prompt |
| 13 | Perspective shift | Systems | `image-to-video` on a layered plate from `motion-plates` |
| 14 | Glass focus | Systems | none; code only |
| 15 | Flowing paths | Systems | none; code only |
| 16 | Particle logo | Systems | Space `3d-logo-animation` (chrome reveal, not particles) |

## Cinetic technique library (MIT)

`engines/cinetic/references/technique-library.md` (measured techniques, `scripts/pick.py` draws them per format) and `engines/cinetic/references/transitions.md` (seam catalogue 4.1–4.12). Headings:

- **Contents**
- **Opening hooks**
  - Problem pile-up, freeze, turn
  - Sparse intro, drop on the first hard cut
  - A click starts the film
  - Cursor into a field, two-stage push, typed provocation
  - Cut in mid-sentence, pull back to the line
  - Finished result first, then rewind
  - Mark builds, then is thrown into a macro of itself
  - Four live cells from frame 2
  - Macro number scramble, one-frame snap-out
  - Oversize line flies through, restarts small
- **Transitions**
  - Anchored overlay, background swap
  - Angle change on a shared drift
  - Conveyor line swap
  - Motion-masked swap
  - Path relay
  - Product surface cover wipe
  - Reveal by subtraction
  - Shape match cut
  - Tip-back exit
  - Velocity handoff cut
  - Band wipe
  - Defocus cut
  - Envelope-matched type cut
  - Horizon rise
  - Iris from a glyph
  - Polarity flip cut
  - Select and retype swap
  - Stepped column fill
  - Collapse to a dot relay
  - Giant word punch-out
  - Portal zoom with aspect morph
  - Scale-through cut
- **Camera**
  - Breathing zoom between interactions
  - Detail first, then pull back
  - Fit-to-content follow
  - Follow the lead dot
  - Isolating push into one item
  - Layered parallax truck
  - Living hold creep
  - Pull-back that lands an event
  - Punch-in insert on the same render
  - Reactive reframe
  - Seamless loop drift
  - Zoom-out hop between areas
  - Crane down with a delayed push
  - Cursor-led whip orbit
  - Directional impact kick
  - Extrude then crash in
  - Push-in with a roll swing
  - Dolly surge with a foreground pass
  - Fly-through of a depth field
  - Hero push with a 3D turn
  - Off-frame whip relay
  - Pull out from inside the object
- **Typography in motion**
  - Animated line re-break
  - Blur-swap rescale
  - Blur-to-focus word rise
  - Centre-out line unmask
  - In-place word light-up on beats
  - Masked baseline rise
  - Re-centring line build
  - Reading-order word exit
  - Staggered word roll
  - Time-boxed eased type-on
  - Vertical word stack
  - Words spill out from behind a mark
  - Hard-step edits that act out the copy
  - Multi-direction slam assembly
  - Scaled-echo extrusion
  - Scramble decode
  - Shared-letter morph
  - Slice glitch into a speed streak
  - Slice-band glyph assembly
  - Travelling front restyles a word
  - One-word slam sequence
  - Oversize word slide-in
  - Phrase clamp at a junction
  - Quiet type swells on the drop
  - Slot roller beside a fixed phrase
- **UI choreography**
  - Cards dealt or dropped into a grid
  - Container morph into its next role
  - Container resizes, content reflows
  - Drag to reorder, siblings make way
  - Lens list scroll
  - Progress spine leads the steps
  - Push-aside with bound layout
  - Row cascade
  - Shell first, then contents, then the action
  - Spawn from the anchor point
  - Top insert pushes the list down
  - Clutter pile-up, then strip to one
  - Genie launch from an icon
  - Path fractures into a fan, then re-converges
  - Stalled state by dimming
  - Fanned stack resolves into slots
  - Orbit gather and merge
  - Outline-led insert and spawn
  - Toss into a bin with one rebound
- **Data and numbers**
  - Constant-speed bar sweep with lit caps
  - Ease-out count-up from a near-final value
  - Flag cascade, then one chosen
  - Line chart draws with a tracking head
  - Mechanical digit reel
  - Mini bar-chart answer card
  - One control drives several live numbers
  - Ring gauge filling with its centre number
  - Area-true ratio comparison
  - Before-to-after with a delta chip
  - Companion glyph swaps mid-count
  - Process-status pill with ring progress
  - Top-to-bottom row refresh
  - Tucked unit under the last digits
  - Unit grid that fills to the count
  - Hero bar in close-up, then pull back
  - Metric as the first statement
- **Product demo**
  - Agent status beat, then streamed answer
  - Change applied as a visible diff
  - Command runs, output prints in bursts
  - Device rises already moving
  - Edit with the product's own UI
  - Fast prompt at true scale
  - Flick scroll lands the target
  - Ghost suggestion accepted with a key
  - Hard swap on the cause frame
  - List narrows with each keystroke
  - One native control as the demo
  - Scrub a chart with a live readout
  - Before/after drag divider
  - Drag assets in, skeletons fill
  - Generated view resolves from soft
  - Long page flown like a runway
  - Mark docks into the app
  - Pin field pull-back
  - Several people at work at once
  - Headline becomes the product input
  - Shared element survives the page change
  - Tilted product plane flattens
- **Logo and end card**
  - End card replays the opening
  - Lockup keeps building through the hold
  - Mark slides aside, name follows
  - Seed build with stroke draw-on
  - Story object becomes the mark
  - The product clears the stage
  - Accent icon cools to its neutral mark
  - Card shrinks to a pill, words close in
  - CTA line closes its gaps
  - Device keeps time inside the lockup
  - Mark turns through a key light
  - Name types backwards, group stays centred
  - Staircase echo shape morph
  - Stop-motion brand strobe
  - Words part, URL types into the gap
  - Dark slam, spin and brighten
  - Liquid blob resolves into the mark
  - Pull out of the mark, undershoot, breathe
- **Colour and light**
  - Accent on the newest arrival
  - Drain the stage, keep the hero
  - Ink resolve on arrival
  - Key-light edge hairline
  - Monochrome world, one accent
  - Now, was, next tone ladder
  - One-hue light ramp
  - Palette shift as context cue
  - Specular sweep
  - Accent hit envelope
  - Brightness rides the move
  - Duotone until featured
  - Graphic softens into the stage
  - Living gradient stage
  - Rim streak on card edges
  - Rising colour wash carrier
  - Shadows tinted by the stage
  - Tilt-linked sheen
  - Travelling tone band fill
  - Type solidity arc
  - Accent ground for claims only
  - Light swell bridge into the hero
  - Rolling band flood
  - Single inversion card
  - Theme flip mid-move
- **Texture and finish**
  - Feathered edge mask
  - Fog floor
  - Global frame-keyed grain
  - Gobo-lit studio backdrop
  - Hairline edge and key shadow
  - Low-luma photo plate
  - Micro-tick UI sound
  - One grade across mixed media
  - Speed-gated motion blur
  - Brushed micro-streaks
  - Faint dot-matrix silhouette
  - Glyph-grid shock pulse
  - Halftone shading
  - Stepped cadence on twos
  - Stepped mosaic resolve
  - Stipple only in lit ramps
  - Intersecting ring field
  - Locked-state mosaic
  - Scanline transmutation
  - Wireframe-to-product scan
- **Layout and composition**
  - Caption in the subject's negative space
  - Live cause-and-effect split
  - One huge centred subject
  - Subtract to the one
  - Vertical clear-band stack
  - Words part for an inserted object
  - Centre object with mirrored flanks
  - Headline over a ghost of the UI
  - Hero icon becomes the inline glyph
  - Hub-and-spoke concept diagram
  - Icon-led ragged word stack
  - Mark set as a word
  - Opposite-corner caption relay
  - Arc carousel
  - Bento cell takes over the frame
  - Swarm, cluster and burst reveal
- **Pacing and structure**
  - Breath envelope per card
  - Camera locks, the interface performs
  - Each repeat runs faster
  - Fixed-length ask, variable answer
  - Hard stop into a silent sign-off
  - Image act, then type act
  - Light and dark as chapters
  - Long-tailed beat lengths
  - Loop seam hidden at a motion peak
  - Machine on the grid, hands off it
  - Music hole, then slam on the cut
  - One screen direction per act
  - Phrase chunks on the beat
  - Silent UI over a steady bed
  - Spectacle, diagram, walkthrough, sign-off
  - Accelerando into the climax
  - Empty ground after a cut
  - The one long hold
  - One camera journey across one surface
  - Oner through a morph chain
  - Score arranged to the acts
  - Silence as the default bed
  - Travelling thread object
- **Micro-interactions**
  - Chip bloom around content
  - Click to focus: I-beam, ring, caret
  - Cursor glyph follows context
  - Drag, lift and seat
  - Guide cursor: arrive, hover, press
  - Send as a ghosted handoff
  - Shared highlight walks the menu
  - Spinner resolves to a check
  - Two-beat confirm cascade
  - Badge count bump
  - Drag-select snaps glyph by glyph
  - Focus ring: pop on click, trim to point
  - In-place character rewrite
  - Launch hop that never lands
  - One-element tell before the event
  - Radial dash burst around a word
  - Anticipation dip before an unlock
  - Shape handoff: pill becomes the icon
  - Stretchy tab indicator
  - Velocity-stretch dot
- **Depth and 3D**
  - 3D flip that swaps state
  - Product on a thick extruded slab
  - Tilted object on a spotlit ground
  - Cube turn to a blank face
  - Depth orbit ring that collapses into the mark
  - Edge-on sliver snaps face-on
  - Exploded layer stack
  - Folded channel that unfolds flat
  - Peek, hover, launch and recede
  - Pinned label over a swapping world
  - Press tilt that hides a swap
  - Card fan that buries, then scatters
  - Icon lifts out of its row into a 3D hero
  - Impact morph with stretch and floor ripple

Seam catalogue (`transitions.md`):

- 4.1 Relay handoff
- 4.2 Shared-element container morph
- 4.3 Iris or flood from the device
- 4.4 Implosion into the device, then silence, then the drop
- 4.5 Shutter collapse
- 4.6 Split on a seam
- 4.7 Velocity-matched cut
- 4.8 Zoom-through
- 4.9 Partial slide cut
- 4.10 Word waterfall
- 4.11 An exit that reverses its entrance
- 4.12 Words become the mark

## Motionmaxxing (Apache-2.0)

`engines/motionmaxxing/references/transitions.md`, `type.md`, `motion.md` (12 measured eases), `ui-demo.md`, `close.md`; precedent lookup `python3 engines/motionmaxxing/scripts/precedent.py query --beat <hook|proof|close> --content <ui|type|photo> --text "..."` over `library/moments.jsonl` (M913–M974).

## Sloosh-only motion (no code renderer)

| Need | Sloosh route | Status |
|---|---|---|
| Logo reveal | Space `3d-logo-animation`; `textured-logo` still → `image-to-video` | ready-space |
| Product reveal, tear, splash, float, unbox, squish, cake | Spaces in `product-animation` | ready-space |
| Orbit with feature labels | Space `feature-callout-orbit` | ready-space |
| Exploded view | Space `exploded-view-animation` | ready-space |
| A → B morph (scene, pose, colour, day → dusk) | `kling-o3` / `kling-v3-omni-video` / `seedance-2.5` with `start_frame` + `end_frame` | needs-validation |
| Push-in, orbit, rack focus on a still | `image-to-video` (`kling-3.0`, `seedance-2.5`) | ready |
| Text on screen | GPT Image 2.5 frames + morph; unreliable past 4 words | needs-validation |
| Captions | Space `add-captions`; canvas `video-subtitle` | ready-space |
| Music, voice, lipsync | `soundtrack-and-voice` | ready-space / canvas |
| Restyle a rendered film | `quote_generation` mode `video_edit` (`gemini-omni-1.1-flash`, `seedance-2.5`) | ready |
| Join clips, trim, extract frame, mux | canvas nodes only (`video-concat`, `video-trim`, `video-frame-extract`, `merge-audio-video`) | canvas |
| Reframe or re-encode a finished video | not available; local ffmpeg (`reel-export`) | gap |
