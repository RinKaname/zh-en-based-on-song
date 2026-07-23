import json

# Dataset containing the translated pairs for the Lyria3 song and the missing GPU lines
lyria3_dataset = [
    {"source": "风起 吹散了边关的黄沙", "target": "The wind rises, scattering the yellow dust of the frontier."},
    {"source": "卸下 重铠换上红色的纱", "target": "Shedding my heavy armor, I don red silk."},
    {"source": "千军万马 曾踏破这天涯", "target": "A million troops once trampled across the ends of the earth."},
    {"source": "如今 烛火代替了厮杀", "target": "Now, candlelight has replaced the clash of battle."},
    {"source": "帷幄之中 看星辰起落", "target": "Within the command tent, I watch the stars rise and fall."},
    {"source": "策谋清明 敌军皆勘破", "target": "With clear strategies, I see through all the enemy's moves."},
    {"source": "今夜不谈烽火 且把酒斟满", "target": "Tonight we speak not of beacon fires, let us fill our cups with wine."},
    {"source": "听战鼓 化作心跳的狂澜", "target": "Hear the war drums transform into the wild surging of our heartbeats."},
    {"source": "且看吾 执神策 破阵踏破长空", "target": "Just watch me wield divine strategies, breaking through formations and trampling the vast sky."},
    {"source": "山河万里 定乾坤 握在我的手中", "target": "Ten thousand miles of mountains and rivers, I stabilize the world, holding it in my hands."},
    {"source": "仲春十二 生辰乐 举杯敬苍穹", "target": "On the twelfth day of mid-spring, celebrating my birthday, I raise my cup to the heavens."},
    {"source": "一手擎天 万事兴 唯我气贯长虹", "target": "With one hand I hold up the sky, all things prosper, my spirit alone pierces the heavens like a rainbow."},
    {"source": "回首 忆当年峥嵘的岁月", "target": "Looking back, I recall the extraordinary years of the past."},
    {"source": "长枪 刻下不屈的誓约", "target": "My long spear carves an unyielding oath."},
    {"source": "百战千回 换今日的无缺", "target": "After a hundred battles and a thousand campaigns, I have earned today's flawless glory."},
    {"source": "笑看 九州四海齐朝谒", "target": "Smiling, I watch the Nine Provinces and Four Seas pay their homage together."},
    {"source": "不需要 谁来加冕这荣耀", "target": "I need no one to crown this glory."},
    {"source": "我自己 铺就封神的步道", "target": "I alone pave the path to godhood."},
    {"source": "千杯不醉 听三军的高啸", "target": "Unfazed by a thousand cups of wine, I hear the triumphant roars of the three armies."},
    {"source": "万岁千秋 刻下我的记号", "target": "Carving my mark for ten thousand ages."},
    {"source": "千军万马忆峥嵘", "target": "A million troops recall the extraordinary years."},
    {"source": "山河万里定乾坤", "target": "Ten thousand miles of mountains and rivers, I stabilize the world."},
    {"source": "仲春生辰 满城春风", "target": "On my mid-spring birthday, a spring breeze fills the city."},
    {"source": "天下 尽在吾手中", "target": "The entire world is right here in my hands."},
    {"source": "(天下 尽在吾手中)", "target": "(The entire world is right here in my hands.)"},
    {"source": "(喘不过气，速度太快了！)", "target": "(Out of breath, it's too fast!)"},
    {"source": "(120 TeraFLOPs!)", "target": "(120 TeraFLOPs!)"},
    {"source": "(准备好了吗？Warp 排列... Tile 部署... 准备... 冲啊！)", "target": "(Ready? Warp aligned... Tile deployed... Ready... Charge!)"},
    {"source": "呜呜 (CUDA 骏马！)", "target": "Woo-woo (CUDA steed!)"},
    {"source": "呜呜 (Matrix Pyoi Matrix Pyoi!)", "target": "Woo-woo (Matrix Pyoi Matrix Pyoi!)"},
    {"source": "呜呜 (喜欢骏马！)", "target": "Woo-woo (Love the steed!)"},
    {"source": "呜呜 (Fused Multiply-Add!)", "target": "Woo-woo (Fused Multiply-Add!)"},
    {"source": "Matrix! Tile! Warp Sync! (3, 2, 1, 计算开始！)", "target": "Matrix! Tile! Warp Sync! (3, 2, 1, Computation start!)"},
    {"source": "矩阵骏马！", "target": "Matrix steed!"},
    {"source": "Matrix Pyoi Matrix Pyoi!", "target": "Matrix Pyoi Matrix Pyoi!"},
    {"source": "呜呜 (喂！)", "target": "Woo-woo (Hey!)"},
    {"source": "呜呜 (喂，CUDA 激流！)", "target": "Woo-woo (Hey, CUDA torrent!)"},
    {"source": "咻嗒卡嗒-嗒嗒嗒... (3, 2, 1, 部署成功！)", "target": "Swish-clack-tatata... (3, 2, 1, Deployment successful!)"}
]

# Save dataset to a JSONL file
with open("lyria3_dataset.jsonl", "w", encoding="utf-8") as f:
    for item in lyria3_dataset:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

print(f"Successfully created dataset with {len(lyria3_dataset)} samples.")
