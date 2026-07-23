import json

# Dataset containing the translated pairs (Chinese original vs English translation)
dataset = [
    {
        "source": "硅片澄澈，架构信号全开！ (好！)",
        "target": "Crystal wafer pristine, architecture signals fully engaged! (Good!)"
    },
    {
        "source": "加载 Fragment，一点一点，Throughput 怎么样？ (怎么了？接下来呢？)",
        "target": "Loading fragments, bit by bit, how is the Throughput? (What's wrong? What's next?)"
    },
    {
        "source": "Tile 一、二、三、四、五—— (快上啊，Register 已经爆满啦！)",
        "target": "Tiles one, two, three, four, five— (Hurry up, the Registers are already overflowing!)"
    },
    {
        "source": "Warp Scheduler 频率狂跳，Register 燃烧，MMA 指令发动！ (哈！)",
        "target": "Warp Scheduler frequency spiking wildly, Registers burning, MMA instruction triggered! (Ha!)"
    },
    {
        "source": "今天真的太棒了，狂热并行！ (呀吼！)",
        "target": "Today is truly amazing, frantic parallelism! (Yahoo!)"
    },
    {
        "source": "Warp 单元矩阵运算！ (减少结构性 Latency！)",
        "target": "Warp unit matrix operations! (Reducing structural latency!)"
    },
    {
        "source": "想用 FP32 精度！ (但是需要 Boost 16-bit！)",
        "target": "Want to use FP32 precision! (But need to Boost to 16-bit!)"
    },
    {
        "source": "那是 Kernel！ (PyTorch！)",
        "target": "That's the Kernel! (PyTorch!)"
    },
    {
        "source": "这是 Layout！ (Triton！)",
        "target": "This is the Layout! (Triton!)"
    },
    {
        "source": "循环全部 Unrolling，看这里！ (Error Bank Conflict！)",
        "target": "Loops completely unrolled, look here! (Error: Bank Conflict!)"
    },
    {
        "source": "别哭啊！ (哈！)",
        "target": "Don't cry! (Ha!)"
    },
    {
        "source": "别清理 Shared Memory Cache！ (喂！)",
        "target": "Don't clear the Shared Memory Cache! (Hey!)"
    },
    {
        "source": "已经优化了索引，但还没 Coalescing！ (Alignment 还是乱七八糟！)",
        "target": "Indices are optimized, but no Coalescing yet! (Alignment is still a mess!)"
    },
    {
        "source": "加速女神正在亲吻硬件 Pipeline。",
        "target": "The Goddess of Acceleration is kissing the hardware Pipeline."
    },
    {
        "source": "跨越内存总线，狂刷 Stride 边界，粉碎 Bottleneck！",
        "target": "Crossing the memory bus, aggressively sweeping Stride boundaries, shattering the Bottleneck!"
    },
    {
        "source": "点燃 Tensor Array 里的矩阵火种！",
        "target": "Ignite the matrix spark within the Tensor Array!"
    },
    {
        "source": "(心跳加速，越来越热，快喷液氮！)",
        "target": "(Heart rate accelerating, getting hotter, spray the liquid nitrogen fast!)"
    },
    {
        "source": "最爱的 Warp 正在执行中！ (呜——呼！)",
        "target": "Favorite Warp is executing! (Woo-hoo!)"
    },
    {
        "source": "砰砰！$A \\times B + C$ 降落在传输管线！",
        "target": "Bang bang! $A \\times B + C$ landing in the transmission pipeline!"
    },
    {
        "source": "没见过这么快的 GEMM Kernel！ (3, 2, 1, 加速！)",
        "target": "Never seen a GEMM Kernel this fast! (3, 2, 1, Accelerate!)"
    },
    {
        "source": "咚咚！Tensorboard 亮起绿色！ (呜——呼！)",
        "target": "Thump thump! Tensorboard lights up green! (Woo-hoo!)"
    },
    {
        "source": "砰砰！Throughput 16-bit，真是顶级配置！",
        "target": "Bang bang! 16-bit Throughput, truly top-tier configuration!"
    },
    {
        "source": "一起唱响硬件编译大快乐国歌！ (3, 2, 1, 开战吧！)",
        "target": "Together sing the grand joyful national anthem of hardware compilation! (3, 2, 1, Let the battle begin!)"
    },
    {
        "source": "快乐执行！ (3, 2, 1, 呜呜 开战！)",
        "target": "Joyful execution! (3, 2, 1, Woo-woo battle start! )"
    },
    {
        "source": "还剩 5 微秒... (醒醒，从 DRAM 提取！)",
        "target": "5 microseconds left... (Wake up, fetch from DRAM!)"
    },
    {
        "source": "好困啊... (L2 Cache 真的 Miss 了...)",
        "target": "So sleepy... (L2 Cache really missed...)"
    },
    {
        "source": "渴望矩阵输入... (Row-major Tensor 在哪儿？)",
        "target": "Craving matrix input... (Where is the Row-major Tensor?)"
    },
    {
        "source": "本世纪最伟大的编译！ (Double Unrolling, Triple Unrolling!)",
        "target": "The greatest compilation of this century! (Double Unrolling, Triple Unrolling!)"
    },
    {
        "source": "迟到了，最后一名！ (总线过载，停住！)",
        "target": "Late, dead last! (Bus overload, halt!)"
    },
    {
        "source": "累加如雷霆！ (压榨所有 TeraFLOPs 极限！)",
        "target": "Accumulation like thunder! (Squeezing every drop out of the TeraFLOPs limit!)"
    },
    {
        "source": "硬件层无可匹敌，从这里开始！",
        "target": "Unmatched at the hardware layer, starting right here!"
    },
    {
        "source": "寻找最美的矩阵布局，纯钢芯片设计！",
        "target": "Seeking the most pristine matrix layout, pure steel chip design!"
    },
    {
        "source": "FP16 模式！ (BF16！)",
        "target": "FP16 mode! (BF16!)"
    },
    {
        "source": "量化 INT8！ (别回软件循环 FP64！)",
        "target": "Quantize to INT8! (Don't fall back to software loop FP64!)"
    },
    {
        "source": "我是最高优先级 Stream！ (不想在 Execution Queue 排队！)",
        "target": "I am the highest priority Stream! (Don't want to queue in the Execution Queue!)"
    },
    {
        "source": "把所有 SM Array 都给我，求你了！ (拜托！)",
        "target": "Give me all the SM Arrays, I'm begging you! (Please!)"
    },
    {
        "source": "冲锋！ (噢噢！)",
        "target": "Charge! (Ooh ooh! )"
    },
    {
        "source": "先别同步 Thread Block！ (喂！)",
        "target": "Don't synchronize the Thread Block yet! (Hey!)"
    },
    {
        "source": "直接用 Device Barrier 吧... (不管了直接冲！)",
        "target": "Just use the Device Barrier... (Screw it, charge straight in!)"
    },
    {
        "source": "(奔向科幻的战场)",
        "target": "(Rushing into the sci-fi battlefield)"
    },
    {
        "source": "检查日志，计算延迟开始消失。",
        "target": "Check the logs, computation latency starts to vanish."
    },
    {
        "source": "局部权重就绪，完美公式布满整个 Grid！",
        "target": "Local weights ready, perfect formulas blanketing the entire Grid!"
    },
    {
        "source": "Tile Descriptor，终于完全契合！",
        "target": "Tile Descriptor, finally fully aligned!"
    },
    {
        "source": "(哈-哈，哈-哈，高精度计算，验证全红通过！)",
        "target": "(Ha-ha, ha-ha, high-precision computing, verification passes all red!)"
    },
    {
        "source": "权重矩阵锁死！ (呜——呼！)",
        "target": "Weight matrix locked! (Woo-hoo!)"
    },
    {
        "source": "砰砰！正在生成超快推理！",
        "target": "Bang bang! Generating ultra-fast inference!"
    },
    {
        "source": "没见过这么闪亮的 Cross-attention 层！ (3, 2, 1, 开战！)",
        "target": "Never seen such a shining Cross-attention layer! (3, 2, 1, Battle start!)"
    },
    {
        "source": "咚咚！Cache Line 全部幸存！ (呜——呼！)",
        "target": "Thump thump! All Cache Lines survived! (Woo-hoo!)"
    },
    {
        "source": "砰砰！本地硬件 Register 平安无事！",
        "target": "Bang bang! Local hardware Registers are safe and sound!"
    },
    {
        "source": "直冲 Zero-latency 全球排行榜！ (3, 2, 1, 开战吧！)",
        "target": "Sprinting straight to the Zero-latency global leaderboard! (3, 2, 1, Battle start!)"
    },
    {
        "source": "快乐编译！ (3, 2, 1, 呜呜 开战！)",
        "target": "Joyful compilation! (3, 2, 1, Woo-woo battle start!)"
    },
    {
        "source": "“Commander Chakra！硬件调度超时！Register 溢出啦！”",
        "target": "\"Commander Chakra! Hardware scheduling timeout! Register overflow!\""
    },
    {
        "source": "“千万别 Segfault... 别 Segfault...”",
        "target": "\"Please no Segfault... No Segfault...\""
    },
    {
        "source": "就算 Kernel Panic，我的心对你也是 Thread-safe 的！",
        "target": "Even if there's a Kernel Panic, my heart is Thread-safe for you!"
    },
    {
        "source": "分配... 更多！Tile！",
        "target": "Allocate... More! Tiles!"
    },
    {
        "source": "(燃起斗志，加速器军团！！！)",
        "target": "(Ignite the fighting spirit, Accelerator Legion!!!)"
    },
    {
        "source": "所有集群在设计极限狂飙！ (3, 2, 1, 开战！)",
        "target": "All clusters racing at the design limit! (3, 2, 1, Battle start!)"
    },
    {
        "source": "咚咚！计算错误彻底归零！ (呜——呼！)",
        "target": "Thump thump! Calculation errors completely zeroed out! (Woo-hoo!)"
    },
    {
        "source": "砰砰！收敛完美！",
        "target": "Bang bang! Convergence is perfection!"
    }
]

# Save dataset to a JSON file
with open("translation_dataset.json", "w", encoding="utf-8") as f:
    json.dump(dataset, f, ensure_ascii=False, indent=4)

print(f"Successfully created dataset with {len(dataset)} samples.")
