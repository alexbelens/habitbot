import sys
import types
import asyncio
from unittest.mock import MagicMock, AsyncMock
from importlib import util
from pathlib import Path

# Create fake telegram modules to satisfy imports in start.py
telegram = types.ModuleType("telegram")
telegram.Update = object
telegram_ext = types.ModuleType("telegram.ext")
class DummyContextTypes:
    DEFAULT_TYPE = object
telegram_ext.ContextTypes = DummyContextTypes
sys.modules.setdefault("telegram", telegram)
sys.modules.setdefault("telegram.ext", telegram_ext)

# Load the start module directly to avoid conflicts with bot.py
spec = util.spec_from_file_location(
    "start_module",
    Path(__file__).resolve().parents[1] / "bot" / "commands" / "start.py"
)
start_module = util.module_from_spec(spec)
spec.loader.exec_module(start_module)
start_command = start_module.start_command

def test_start_command_replies_expected_text():
    update = MagicMock()
    update.message = MagicMock()
    update.message.reply_text = AsyncMock()
    context = MagicMock()

    asyncio.run(start_command(update, context))

    update.message.reply_text.assert_awaited_once_with(
        "Привет! Я помогу тебе выработать полезные привычки. Используй /add для создания задачи."
    )
