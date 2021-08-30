from ...models import Persona, Plugin
from . import example, example_with_args


plugin = Plugin(
    name="rsserpent-plugin-builtin",
    author=Persona(
        name="queensferryme",
        link="https://github.com/queensferryme",
        email="queensferry.me@gmail.com",
    ),
    repository="https://github.com/RSSerpent/RSSerpent",
    prefix="/_",
    routers={
        example.path: example.provider,
        example_with_args.path: example_with_args.provider,
    },
)