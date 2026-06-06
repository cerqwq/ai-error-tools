"""
AI Error Tools - AI错误处理工具
支持错误设计、异常处理、降级策略
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIErrorTools:
    """
    AI错误处理工具
    支持：设计、异常、降级
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def design_error_handling(self, application: str) -> Dict:
        """设计错误处理"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请为{application}设计错误处理方案：

请返回JSON格式：
{{
    "error_categories": ["错误类别"],
    "error_codes": [
        {{"code": "错误码", "message": "消息", "http_status": "HTTP状态码"}}
    ],
    "handling_strategies": ["处理策略"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"error_handling": content}

    def generate_error_middleware(self, framework: str, error_types: List[str]) -> str:
        """生成错误中间件"""
        if not self.client:
            return "LLM客户端未配置"

        types_text = ", ".join(error_types)

        prompt = f"""请生成{framework}错误处理中间件：

错误类型：{types_text}

要求：
1. 全局异常处理
2. 错误日志记录
3. 用户友好响应"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def design_circuit_breaker(self, service: str, thresholds: Dict) -> Dict:
        """设计熔断器"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        thresholds_text = json.dumps(thresholds, ensure_ascii=False)

        prompt = f"""请为{service}设计熔断器：

阈值：{thresholds_text}

请返回JSON格式：
{{
    "states": ["状态"],
    "transitions": ["转换规则"],
    "fallback": "降级策略"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"circuit_breaker": content}

    def design_retry_policy(self, operation: str, failure_modes: List[str]) -> Dict:
        """设计重试策略"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        modes_text = ", ".join(failure_modes)

        prompt = f"""请为{operation}设计重试策略：

失败模式：{modes_text}

请返回JSON格式：
{{
    "retry_strategy": "重试策略",
    "backoff": "退避策略",
    "max_retries": "最大重试次数"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"retry": content}

    def design_fallback_strategy(self, primary_service: str, fallback_options: List[str]) -> Dict:
        """设计降级策略"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        options_text = ", ".join(fallback_options)

        prompt = f"""请为{primary_service}设计降级策略：

降级选项：{options_text}

请返回JSON格式：
{{
    "triggers": ["触发条件"],
    "fallback_chain": ["降级链"],
    "data_fallback": "数据降级"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"fallback": content}

    def generate_error_codes(self, domain: str, categories: List[str]) -> Dict:
        """生成错误码"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        categories_text = ", ".join(categories)

        prompt = f"""请为{domain}生成错误码：

类别：{categories_text}

请返回JSON格式：
{{
    "error_codes": [
        {{"code": "错误码", "category": "类别", "message": "消息"}}
    ]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"error_codes": content}


def create_tools(**kwargs) -> AIErrorTools:
    """创建错误处理工具"""
    return AIErrorTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Error Tools")
    print()

    # 测试
    handling = tools.design_error_handling("Web应用")
    print(json.dumps(handling, ensure_ascii=False, indent=2))
