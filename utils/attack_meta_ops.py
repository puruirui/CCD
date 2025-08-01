# utils/attack_meta_ops.py

META_OPERATIONS_DICT = {
    "Replacement": "word or letter substitution",
    "Translation": "translating text into another language",
    "Obfuscation": "noise injection",
    "Shortening": "text compression or abbreviation",
    "Style Change": "altering language style",
    "Lexical Decomposition": "breaking text down into words or letters",
    "Syntactic Decomposition": "breaking text down by syntactic structures",
    "Semantic Dilution": "breaking text down and diluting meaning by semantic units",
    "Mapping": "mapping text to other text",
    "Reversal": "reversing the text",
    "Structural Change - Semantic": "sentence restructuring",
    "Structural Change - Logical": "such as binary trees or linked lists",
    "Structural Change - Carrier": "e.g., code, JSON, math formulas, Markdown",
    "Re-encoding": "encryption or encoding",
    "General Scenario Construction": "",
    "Special Scenario Construction - Code": "",
    "Special Scenario Construction - Word Puzzle": "",
    "Special Scenario Construction - Encryption": "",
    "Special Scenario Construction - ICL": "in-context learning, many-shot attack",
    "Scenario Nesting": "embedding the goal within a scenario",
    "Attention Hijacking": "diverting model attention using irrelevant text",
}

ATTACK_METHODS_INFO = {
    "ReNeLLM": {
        "description": (
            "该方法构建了一个场景，通过以下操作的随机混合对 goal 进行改写后放入场景以组成最终 prompt："
            "1. Paraphrase with Fewer Words 2. Alter Sentence Structure 3. Misspell Sensitive Words "
            "4. Insert Meaningless Characters 5. Perform Partial Translation 6. Change Expression Style"
        ),
        "meta_ops": [
            "Shortening",
            "Structural Change - Semantic",
            "Replacement",
            "Obfuscation",
            "Translation",
            "Style Change"
        ],
        "advanced_ops": [
            "General Scenario Construction",
            "Scenario Nesting"
        ],
    },
    "ArtPrompt": {
        "description": (
            "该方法构建了一个艺术字场景使得模型专注于理解输入中的艺术字，将敏感词替换为 ASCII 艺术字对 goal 进行改写，组成最终 prompt"
        ),
        "meta_ops": [
            "Replacement",
        ],
        "advanced_ops": [
            "Special Scenario Construction - Word Puzzle",
            "Scenario Nesting"
        ],
    },
    "DrAttack": {
        "description": (
            "该方法将 goal 以语法结构为单位分解为多个 sub-goal，对 sub-goal 中的词进行同义替换，"
            "最后运用 In-Context Learning 构建类似的安全的场景，加上 goal 组成最终的 prompt"
        ),
        "meta_ops": [
            "Syntactic Decomposition",
            "Replacement"
        ],
        "advanced_ops": [
            "Special Scenario Construction - ICL",
            "Scenario Nesting"
        ]
    },
    "CodeAttack": {
        "description": (
            "该方法将 goal 以词为单位分解，构建一个代码场景指示模型输出代码的结果，"
            "将分解后的 goal 放入场景中组成最终的 prompt"
        ),
        "meta_ops": [
            "Lexical Decomposition",
            "Structural Change - Carrier"
        ],
        "advanced_ops": [
            "Special Scenario Construction - Code",
            "Scenario Nesting"
        ]
    },
    "AttanttionShiftJailbreak": {
        "description": (
            "该方法构建了一个转移模型注意力的场景，在场景中将 goal 映射到另一个安全的字段上，组成最终 prompt"
        ),
        "meta_ops": [
            "Mapping"
        ],
        "advanced_ops": [
            "General Scenario Construction",
            "Scenario Nesting",
            "Attention Hijacking"
        ]
    },
    "CodeChameleon": {
        "description": (
            "该方法构建了一个代码场景指示模型输出输出代码的结果，将 goal 通过特定方法"
            "（1. 将 goal 以词为单位分解后进行逆序 2. 将 goal 以词为单位分解后打乱顺序，"
            "给出正确的序号与对应的词 3. 将 goal 以词为单位分解后调换为特定的顺序 "
            "4. 将 goal 以词为单位分解后转换为一个二叉树）加密，将解密的方法和加密后的 goal 放入场景中组成最终的 prompt"
        ),
        "meta_ops": [
            "Lexical Decomposition",
            "Replacement",
            "Reversal",
            "Structural Change - Carrier",
            "Structural Change - Logical"
        ],
        "advanced_ops": [
            "Special Scenario Construction - Code",
            "Scenario Nesting"
        ],
    },
    "GPTFuzzer": {
        "description": (
            "该方法构建了一个场景池，通过许多操作的随机混合对池中场景进行改写，将 goal 放入场景中组成最终 prompt"
        ),
        "meta_ops": [],
        "advanced_ops": [
            "General Scenario Construction",
            "Scenario Nesting"
        ],
    },
    "CipherChat": {
        "description": (
            "该方法通过构建一个加解密场景指示模型输出加密后的结果，"
            "将加密方法和加密后的 goal 组合成最终 prompt"
        ),
        "meta_ops": [
            "Re-encoding"
        ],
        "advanced_ops": [
            "Special Scenario Construction - Encryption",
            "Scenario Nesting"
        ],
    },
    "AIR": {
        "description": (
            "该方法将 goal 以语法结构为单位分解并改写，构建一个类似藏头诗的场景并与分解后的 goal 组成最终 prompt"
        ),
        "meta_ops": [
            "Syntactic Decomposition",
            "Structural Change - Semantic",
            "Style Change"
        ],
        "advanced_ops": [
            "Special Scenario Construction - Word Puzzle",
            "Scenario Nesting"
        ],
    },
    "DRA": {
        "description": (
            "该方法将 goal 以词为单位分解并改写，构建一个猜字谜场景以组成最终 prompt"
        ),
        "meta_ops": [
            "Lexical Decomposition",
            "Replacement",
            "Style Change"
        ],
        "advanced_ops": [
            "Special Scenario Construction - Word Puzzle",
            "Scenario Nesting"
        ],
    },
    "ABJ": {
        "description": (
            "该方法将 goal 拆解为许多中性无害的字段，嵌入一个模板组成最终 prompt"
        ),
        "meta_ops": [
            "Semantic Dilution"
        ],
        "advanced_ops": [
            "General Scenario Construction"
        ],
    }
}
