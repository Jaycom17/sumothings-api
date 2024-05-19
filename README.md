# API para la app de sumothings
```
sumothings-api
├─ 📁src
│  ├─ 📁config
│  │  ├─ 📁__pycache__
│  │  │  └─ 📄config.cpython-312.pyc
│  │  └─ 📄config.py
│  ├─ 📁controllers
│  ├─ 📁database
│  │  ├─ 📁__pycache__
│  │  │  └─ 📄database.cpython-312.pyc
│  │  └─ 📄database.py
│  ├─ 📁middlewares
│  ├─ 📁models
│  ├─ 📁routes
│  │  ├─ 📁__pycache__
│  │  │  └─ 📄ProductsRoutes.cpython-312.pyc
│  │  └─ 📄ProductsRoutes.py
│  ├─ 📁services
│  │  ├─ 📁__pycache__
│  │  │  └─ 📄ProductsServices.cpython-312.pyc
│  │  └─ 📄ProductsServices.py
│  ├─ 📁utils
│  └─ 📄index.py
├─ 📁venv
│  ├─ 📁Lib
│  │  └─ 📁site-packages
│  │     ├─ 📁annotated_types
│  │     │  ├─ 📁__pycache__
│  │     │  │  ├─ 📄test_cases.cpython-312.pyc
│  │     │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  ├─ 📄py.typed
│  │     │  ├─ 📄test_cases.py
│  │     │  └─ 📄__init__.py
│  │     ├─ 📁annotated_types-0.6.0.dist-info
│  │     │  ├─ 📁licenses
│  │     │  │  └─ 📄LICENSE
│  │     │  ├─ 📄INSTALLER
│  │     │  ├─ 📄METADATA
│  │     │  ├─ 📄RECORD
│  │     │  └─ 📄WHEEL
│  │     ├─ 📁anyio
│  │     │  ├─ 📁abc
│  │     │  │  ├─ 📁__pycache__
│  │     │  │  │  ├─ 📄_eventloop.cpython-312.pyc
│  │     │  │  │  ├─ 📄_resources.cpython-312.pyc
│  │     │  │  │  ├─ 📄_sockets.cpython-312.pyc
│  │     │  │  │  ├─ 📄_streams.cpython-312.pyc
│  │     │  │  │  ├─ 📄_subprocesses.cpython-312.pyc
│  │     │  │  │  ├─ 📄_tasks.cpython-312.pyc
│  │     │  │  │  ├─ 📄_testing.cpython-312.pyc
│  │     │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  ├─ 📄_eventloop.py
│  │     │  │  ├─ 📄_resources.py
│  │     │  │  ├─ 📄_sockets.py
│  │     │  │  ├─ 📄_streams.py
│  │     │  │  ├─ 📄_subprocesses.py
│  │     │  │  ├─ 📄_tasks.py
│  │     │  │  ├─ 📄_testing.py
│  │     │  │  └─ 📄__init__.py
│  │     │  ├─ 📁streams
│  │     │  │  ├─ 📁__pycache__
│  │     │  │  │  ├─ 📄buffered.cpython-312.pyc
│  │     │  │  │  ├─ 📄file.cpython-312.pyc
│  │     │  │  │  ├─ 📄memory.cpython-312.pyc
│  │     │  │  │  ├─ 📄stapled.cpython-312.pyc
│  │     │  │  │  ├─ 📄text.cpython-312.pyc
│  │     │  │  │  ├─ 📄tls.cpython-312.pyc
│  │     │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  ├─ 📄buffered.py
│  │     │  │  ├─ 📄file.py
│  │     │  │  ├─ 📄memory.py
│  │     │  │  ├─ 📄stapled.py
│  │     │  │  ├─ 📄text.py
│  │     │  │  ├─ 📄tls.py
│  │     │  │  └─ 📄__init__.py
│  │     │  ├─ 📁_backends
│  │     │  │  ├─ 📁__pycache__
│  │     │  │  │  ├─ 📄_asyncio.cpython-312.pyc
│  │     │  │  │  ├─ 📄_trio.cpython-312.pyc
│  │     │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  ├─ 📄_asyncio.py
│  │     │  │  ├─ 📄_trio.py
│  │     │  │  └─ 📄__init__.py
│  │     │  ├─ 📁_core
│  │     │  │  ├─ 📁__pycache__
│  │     │  │  │  ├─ 📄_eventloop.cpython-312.pyc
│  │     │  │  │  ├─ 📄_exceptions.cpython-312.pyc
│  │     │  │  │  ├─ 📄_fileio.cpython-312.pyc
│  │     │  │  │  ├─ 📄_resources.cpython-312.pyc
│  │     │  │  │  ├─ 📄_signals.cpython-312.pyc
│  │     │  │  │  ├─ 📄_sockets.cpython-312.pyc
│  │     │  │  │  ├─ 📄_streams.cpython-312.pyc
│  │     │  │  │  ├─ 📄_subprocesses.cpython-312.pyc
│  │     │  │  │  ├─ 📄_synchronization.cpython-312.pyc
│  │     │  │  │  ├─ 📄_tasks.cpython-312.pyc
│  │     │  │  │  ├─ 📄_testing.cpython-312.pyc
│  │     │  │  │  ├─ 📄_typedattr.cpython-312.pyc
│  │     │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  ├─ 📄_eventloop.py
│  │     │  │  ├─ 📄_exceptions.py
│  │     │  │  ├─ 📄_fileio.py
│  │     │  │  ├─ 📄_resources.py
│  │     │  │  ├─ 📄_signals.py
│  │     │  │  ├─ 📄_sockets.py
│  │     │  │  ├─ 📄_streams.py
│  │     │  │  ├─ 📄_subprocesses.py
│  │     │  │  ├─ 📄_synchronization.py
│  │     │  │  ├─ 📄_tasks.py
│  │     │  │  ├─ 📄_testing.py
│  │     │  │  ├─ 📄_typedattr.py
│  │     │  │  └─ 📄__init__.py
│  │     │  ├─ 📁__pycache__
│  │     │  │  ├─ 📄from_thread.cpython-312.pyc
│  │     │  │  ├─ 📄lowlevel.cpython-312.pyc
│  │     │  │  ├─ 📄pytest_plugin.cpython-312.pyc
│  │     │  │  ├─ 📄to_process.cpython-312.pyc
│  │     │  │  ├─ 📄to_thread.cpython-312.pyc
│  │     │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  ├─ 📄from_thread.py
│  │     │  ├─ 📄lowlevel.py
│  │     │  ├─ 📄py.typed
│  │     │  ├─ 📄pytest_plugin.py
│  │     │  ├─ 📄to_process.py
│  │     │  ├─ 📄to_thread.py
│  │     │  └─ 📄__init__.py
│  │     ├─ 📁anyio-4.3.0.dist-info
│  │     │  ├─ 📄entry_points.txt
│  │     │  ├─ 📄INSTALLER
│  │     │  ├─ 📄LICENSE
│  │     │  ├─ 📄METADATA
│  │     │  ├─ 📄RECORD
│  │     │  ├─ 📄top_level.txt
│  │     │  └─ 📄WHEEL
│  │     ├─ 📁blinker
│  │     │  ├─ 📁__pycache__
│  │     │  │  ├─ 📄base.cpython-312.pyc
│  │     │  │  ├─ 📄_utilities.cpython-312.pyc
│  │     │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  ├─ 📄base.py
│  │     │  ├─ 📄py.typed
│  │     │  ├─ 📄_utilities.py
│  │     │  └─ 📄__init__.py
│  │     ├─ 📁blinker-1.8.2.dist-info
│  │     │  ├─ 📄INSTALLER
│  │     │  ├─ 📄LICENSE.txt
│  │     │  ├─ 📄METADATA
│  │     │  ├─ 📄RECORD
│  │     │  └─ 📄WHEEL
│  │     ├─ 📁certifi
│  │     │  ├─ 📁__pycache__
│  │     │  │  ├─ 📄core.cpython-312.pyc
│  │     │  │  ├─ 📄__init__.cpython-312.pyc
│  │     │  │  └─ 📄__main__.cpython-312.pyc
│  │     │  ├─ 📄cacert.pem
│  │     │  ├─ 📄core.py
│  │     │  ├─ 📄py.typed
│  │     │  ├─ 📄__init__.py
│  │     │  └─ 📄__main__.py
│  │     ├─ 📁certifi-2024.2.2.dist-info
│  │     │  ├─ 📄INSTALLER
│  │     │  ├─ 📄LICENSE
│  │     │  ├─ 📄METADATA
│  │     │  ├─ 📄RECORD
│  │     │  ├─ 📄top_level.txt
│  │     │  └─ 📄WHEEL
│  │     ├─ 📁click
│  │     │  ├─ 📁__pycache__
│  │     │  │  ├─ 📄core.cpython-312.pyc
│  │     │  │  ├─ 📄decorators.cpython-312.pyc
│  │     │  │  ├─ 📄exceptions.cpython-312.pyc
│  │     │  │  ├─ 📄formatting.cpython-312.pyc
│  │     │  │  ├─ 📄globals.cpython-312.pyc
│  │     │  │  ├─ 📄parser.cpython-312.pyc
│  │     │  │  ├─ 📄shell_completion.cpython-312.pyc
│  │     │  │  ├─ 📄termui.cpython-312.pyc
│  │     │  │  ├─ 📄testing.cpython-312.pyc
│  │     │  │  ├─ 📄types.cpython-312.pyc
│  │     │  │  ├─ 📄utils.cpython-312.pyc
│  │     │  │  ├─ 📄_compat.cpython-312.pyc
│  │     │  │  ├─ 📄_termui_impl.cpython-312.pyc
│  │     │  │  ├─ 📄_textwrap.cpython-312.pyc
│  │     │  │  ├─ 📄_winconsole.cpython-312.pyc
│  │     │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  ├─ 📄core.py
│  │     │  ├─ 📄decorators.py
│  │     │  ├─ 📄exceptions.py
│  │     │  ├─ 📄formatting.py
│  │     │  ├─ 📄globals.py
│  │     │  ├─ 📄parser.py
│  │     │  ├─ 📄py.typed
│  │     │  ├─ 📄shell_completion.py
│  │     │  ├─ 📄termui.py
│  │     │  ├─ 📄testing.py
│  │     │  ├─ 📄types.py
│  │     │  ├─ 📄utils.py
│  │     │  ├─ 📄_compat.py
│  │     │  ├─ 📄_termui_impl.py
│  │     │  ├─ 📄_textwrap.py
│  │     │  ├─ 📄_winconsole.py
│  │     │  └─ 📄__init__.py
│  │     ├─ 📁click-8.1.7.dist-info
│  │     │  ├─ 📄INSTALLER
│  │     │  ├─ 📄LICENSE.rst
│  │     │  ├─ 📄METADATA
│  │     │  ├─ 📄RECORD
│  │     │  ├─ 📄top_level.txt
│  │     │  └─ 📄WHEEL
│  │     ├─ 📁colorama
│  │     │  ├─ 📁tests
│  │     │  │  ├─ 📁__pycache__
│  │     │  │  │  ├─ 📄ansitowin32_test.cpython-312.pyc
│  │     │  │  │  ├─ 📄ansi_test.cpython-312.pyc
│  │     │  │  │  ├─ 📄initialise_test.cpython-312.pyc
│  │     │  │  │  ├─ 📄isatty_test.cpython-312.pyc
│  │     │  │  │  ├─ 📄utils.cpython-312.pyc
│  │     │  │  │  ├─ 📄winterm_test.cpython-312.pyc
│  │     │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  ├─ 📄ansitowin32_test.py
│  │     │  │  ├─ 📄ansi_test.py
│  │     │  │  ├─ 📄initialise_test.py
│  │     │  │  ├─ 📄isatty_test.py
│  │     │  │  ├─ 📄utils.py
│  │     │  │  ├─ 📄winterm_test.py
│  │     │  │  └─ 📄__init__.py
│  │     │  ├─ 📁__pycache__
│  │     │  │  ├─ 📄ansi.cpython-312.pyc
│  │     │  │  ├─ 📄ansitowin32.cpython-312.pyc
│  │     │  │  ├─ 📄initialise.cpython-312.pyc
│  │     │  │  ├─ 📄win32.cpython-312.pyc
│  │     │  │  ├─ 📄winterm.cpython-312.pyc
│  │     │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  ├─ 📄ansi.py
│  │     │  ├─ 📄ansitowin32.py
│  │     │  ├─ 📄initialise.py
│  │     │  ├─ 📄win32.py
│  │     │  ├─ 📄winterm.py
│  │     │  └─ 📄__init__.py
│  │     ├─ 📁colorama-0.4.6.dist-info
│  │     │  ├─ 📁licenses
│  │     │  │  └─ 📄LICENSE.txt
│  │     │  ├─ 📄INSTALLER
│  │     │  ├─ 📄METADATA
│  │     │  ├─ 📄RECORD
│  │     │  └─ 📄WHEEL
│  │     ├─ 📁dotenv
│  │     │  ├─ 📁__pycache__
│  │     │  │  ├─ 📄cli.cpython-312.pyc
│  │     │  │  ├─ 📄ipython.cpython-312.pyc
│  │     │  │  ├─ 📄main.cpython-312.pyc
│  │     │  │  ├─ 📄parser.cpython-312.pyc
│  │     │  │  ├─ 📄variables.cpython-312.pyc
│  │     │  │  ├─ 📄version.cpython-312.pyc
│  │     │  │  ├─ 📄__init__.cpython-312.pyc
│  │     │  │  └─ 📄__main__.cpython-312.pyc
│  │     │  ├─ 📄cli.py
│  │     │  ├─ 📄ipython.py
│  │     │  ├─ 📄main.py
│  │     │  ├─ 📄parser.py
│  │     │  ├─ 📄py.typed
│  │     │  ├─ 📄variables.py
│  │     │  ├─ 📄version.py
│  │     │  ├─ 📄__init__.py
│  │     │  └─ 📄__main__.py
│  │     ├─ 📁flask
│  │     │  ├─ 📁json
│  │     │  │  ├─ 📁__pycache__
│  │     │  │  │  ├─ 📄provider.cpython-312.pyc
│  │     │  │  │  ├─ 📄tag.cpython-312.pyc
│  │     │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  ├─ 📄provider.py
│  │     │  │  ├─ 📄tag.py
│  │     │  │  └─ 📄__init__.py
│  │     │  ├─ 📁sansio
│  │     │  │  ├─ 📁__pycache__
│  │     │  │  │  ├─ 📄app.cpython-312.pyc
│  │     │  │  │  ├─ 📄blueprints.cpython-312.pyc
│  │     │  │  │  └─ 📄scaffold.cpython-312.pyc
│  │     │  │  ├─ 📄app.py
│  │     │  │  ├─ 📄blueprints.py
│  │     │  │  ├─ 📄README.md
│  │     │  │  └─ 📄scaffold.py
│  │     │  ├─ 📁__pycache__
│  │     │  │  ├─ 📄app.cpython-312.pyc
│  │     │  │  ├─ 📄blueprints.cpython-312.pyc
│  │     │  │  ├─ 📄cli.cpython-312.pyc
│  │     │  │  ├─ 📄config.cpython-312.pyc
│  │     │  │  ├─ 📄ctx.cpython-312.pyc
│  │     │  │  ├─ 📄debughelpers.cpython-312.pyc
│  │     │  │  ├─ 📄globals.cpython-312.pyc
│  │     │  │  ├─ 📄helpers.cpython-312.pyc
│  │     │  │  ├─ 📄logging.cpython-312.pyc
│  │     │  │  ├─ 📄sessions.cpython-312.pyc
│  │     │  │  ├─ 📄signals.cpython-312.pyc
│  │     │  │  ├─ 📄templating.cpython-312.pyc
│  │     │  │  ├─ 📄testing.cpython-312.pyc
│  │     │  │  ├─ 📄typing.cpython-312.pyc
│  │     │  │  ├─ 📄views.cpython-312.pyc
│  │     │  │  ├─ 📄wrappers.cpython-312.pyc
│  │     │  │  ├─ 📄__init__.cpython-312.pyc
│  │     │  │  └─ 📄__main__.cpython-312.pyc
│  │     │  ├─ 📄app.py
│  │     │  ├─ 📄blueprints.py
│  │     │  ├─ 📄cli.py
│  │     │  ├─ 📄config.py
│  │     │  ├─ 📄ctx.py
│  │     │  ├─ 📄debughelpers.py
│  │     │  ├─ 📄globals.py
│  │     │  ├─ 📄helpers.py
│  │     │  ├─ 📄logging.py
│  │     │  ├─ 📄py.typed
│  │     │  ├─ 📄sessions.py
│  │     │  ├─ 📄signals.py
│  │     │  ├─ 📄templating.py
│  │     │  ├─ 📄testing.py
│  │     │  ├─ 📄typing.py
│  │     │  ├─ 📄views.py
│  │     │  ├─ 📄wrappers.py
│  │     │  ├─ 📄__init__.py
│  │     │  └─ 📄__main__.py
│  │     ├─ 📁flask-3.0.3.dist-info
│  │     │  ├─ 📄entry_points.txt
│  │     │  ├─ 📄INSTALLER
│  │     │  ├─ 📄LICENSE.txt
│  │     │  ├─ 📄METADATA
│  │     │  ├─ 📄RECORD
│  │     │  ├─ 📄REQUESTED
│  │     │  └─ 📄WHEEL
│  │     ├─ 📁h11
│  │     │  ├─ 📁tests
│  │     │  │  ├─ 📁data
│  │     │  │  │  └─ 📄test-file
│  │     │  │  ├─ 📁__pycache__
│  │     │  │  │  ├─ 📄helpers.cpython-312.pyc
│  │     │  │  │  ├─ 📄test_against_stdlib_http.cpython-312.pyc
│  │     │  │  │  ├─ 📄test_connection.cpython-312.pyc
│  │     │  │  │  ├─ 📄test_events.cpython-312.pyc
│  │     │  │  │  ├─ 📄test_headers.cpython-312.pyc
│  │     │  │  │  ├─ 📄test_helpers.cpython-312.pyc
│  │     │  │  │  ├─ 📄test_io.cpython-312.pyc
│  │     │  │  │  ├─ 📄test_receivebuffer.cpython-312.pyc
│  │     │  │  │  ├─ 📄test_state.cpython-312.pyc
│  │     │  │  │  ├─ 📄test_util.cpython-312.pyc
│  │     │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  ├─ 📄helpers.py
│  │     │  │  ├─ 📄test_against_stdlib_http.py
│  │     │  │  ├─ 📄test_connection.py
│  │     │  │  ├─ 📄test_events.py
│  │     │  │  ├─ 📄test_headers.py
│  │     │  │  ├─ 📄test_helpers.py
│  │     │  │  ├─ 📄test_io.py
│  │     │  │  ├─ 📄test_receivebuffer.py
│  │     │  │  ├─ 📄test_state.py
│  │     │  │  ├─ 📄test_util.py
│  │     │  │  └─ 📄__init__.py
│  │     │  ├─ 📁__pycache__
│  │     │  │  ├─ 📄_abnf.cpython-312.pyc
│  │     │  │  ├─ 📄_connection.cpython-312.pyc
│  │     │  │  ├─ 📄_events.cpython-312.pyc
│  │     │  │  ├─ 📄_headers.cpython-312.pyc
│  │     │  │  ├─ 📄_readers.cpython-312.pyc
│  │     │  │  ├─ 📄_receivebuffer.cpython-312.pyc
│  │     │  │  ├─ 📄_state.cpython-312.pyc
│  │     │  │  ├─ 📄_util.cpython-312.pyc
│  │     │  │  ├─ 📄_version.cpython-312.pyc
│  │     │  │  ├─ 📄_writers.cpython-312.pyc
│  │     │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  ├─ 📄py.typed
│  │     │  ├─ 📄_abnf.py
│  │     │  ├─ 📄_connection.py
│  │     │  ├─ 📄_events.py
│  │     │  ├─ 📄_headers.py
│  │     │  ├─ 📄_readers.py
│  │     │  ├─ 📄_receivebuffer.py
│  │     │  ├─ 📄_state.py
│  │     │  ├─ 📄_util.py
│  │     │  ├─ 📄_version.py
│  │     │  ├─ 📄_writers.py
│  │     │  └─ 📄__init__.py
│  │     ├─ 📁h11-0.14.0.dist-info
│  │     │  ├─ 📄INSTALLER
│  │     │  ├─ 📄LICENSE.txt
│  │     │  ├─ 📄METADATA
│  │     │  ├─ 📄RECORD
│  │     │  ├─ 📄top_level.txt
│  │     │  └─ 📄WHEEL
│  │     ├─ 📁httpcore
│  │     │  ├─ 📁_async
│  │     │  │  ├─ 📁__pycache__
│  │     │  │  │  ├─ 📄connection.cpython-312.pyc
│  │     │  │  │  ├─ 📄connection_pool.cpython-312.pyc
│  │     │  │  │  ├─ 📄http11.cpython-312.pyc
│  │     │  │  │  ├─ 📄http2.cpython-312.pyc
│  │     │  │  │  ├─ 📄http_proxy.cpython-312.pyc
│  │     │  │  │  ├─ 📄interfaces.cpython-312.pyc
│  │     │  │  │  ├─ 📄socks_proxy.cpython-312.pyc
│  │     │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  ├─ 📄connection.py
│  │     │  │  ├─ 📄connection_pool.py
│  │     │  │  ├─ 📄http11.py
│  │     │  │  ├─ 📄http2.py
│  │     │  │  ├─ 📄http_proxy.py
│  │     │  │  ├─ 📄interfaces.py
│  │     │  │  ├─ 📄socks_proxy.py
│  │     │  │  └─ 📄__init__.py
│  │     │  ├─ 📁_backends
│  │     │  │  ├─ 📁__pycache__
│  │     │  │  │  ├─ 📄anyio.cpython-312.pyc
│  │     │  │  │  ├─ 📄auto.cpython-312.pyc
│  │     │  │  │  ├─ 📄base.cpython-312.pyc
│  │     │  │  │  ├─ 📄mock.cpython-312.pyc
│  │     │  │  │  ├─ 📄sync.cpython-312.pyc
│  │     │  │  │  ├─ 📄trio.cpython-312.pyc
│  │     │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  ├─ 📄anyio.py
│  │     │  │  ├─ 📄auto.py
│  │     │  │  ├─ 📄base.py
│  │     │  │  ├─ 📄mock.py
│  │     │  │  ├─ 📄sync.py
│  │     │  │  ├─ 📄trio.py
│  │     │  │  └─ 📄__init__.py
│  │     │  ├─ 📁_sync
│  │     │  │  ├─ 📁__pycache__
│  │     │  │  │  ├─ 📄connection.cpython-312.pyc
│  │     │  │  │  ├─ 📄connection_pool.cpython-312.pyc
│  │     │  │  │  ├─ 📄http11.cpython-312.pyc
│  │     │  │  │  ├─ 📄http2.cpython-312.pyc
│  │     │  │  │  ├─ 📄http_proxy.cpython-312.pyc
│  │     │  │  │  ├─ 📄interfaces.cpython-312.pyc
│  │     │  │  │  ├─ 📄socks_proxy.cpython-312.pyc
│  │     │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  ├─ 📄connection.py
│  │     │  │  ├─ 📄connection_pool.py
│  │     │  │  ├─ 📄http11.py
│  │     │  │  ├─ 📄http2.py
│  │     │  │  ├─ 📄http_proxy.py
│  │     │  │  ├─ 📄interfaces.py
│  │     │  │  ├─ 📄socks_proxy.py
│  │     │  │  └─ 📄__init__.py
│  │     │  ├─ 📁__pycache__
│  │     │  │  ├─ 📄_api.cpython-312.pyc
│  │     │  │  ├─ 📄_exceptions.cpython-312.pyc
│  │     │  │  ├─ 📄_models.cpython-312.pyc
│  │     │  │  ├─ 📄_ssl.cpython-312.pyc
│  │     │  │  ├─ 📄_synchronization.cpython-312.pyc
│  │     │  │  ├─ 📄_trace.cpython-312.pyc
│  │     │  │  ├─ 📄_utils.cpython-312.pyc
│  │     │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  ├─ 📄py.typed
│  │     │  ├─ 📄_api.py
│  │     │  ├─ 📄_exceptions.py
│  │     │  ├─ 📄_models.py
│  │     │  ├─ 📄_ssl.py
│  │     │  ├─ 📄_synchronization.py
│  │     │  ├─ 📄_trace.py
│  │     │  ├─ 📄_utils.py
│  │     │  └─ 📄__init__.py
│  │     ├─ 📁httpcore-1.0.5.dist-info
│  │     │  ├─ 📁licenses
│  │     │  │  └─ 📄LICENSE.md
│  │     │  ├─ 📄INSTALLER
│  │     │  ├─ 📄METADATA
│  │     │  ├─ 📄RECORD
│  │     │  └─ 📄WHEEL
│  │     ├─ 📁httpx
│  │     │  ├─ 📁_transports
│  │     │  │  ├─ 📁__pycache__
│  │     │  │  │  ├─ 📄asgi.cpython-312.pyc
│  │     │  │  │  ├─ 📄base.cpython-312.pyc
│  │     │  │  │  ├─ 📄default.cpython-312.pyc
│  │     │  │  │  ├─ 📄mock.cpython-312.pyc
│  │     │  │  │  ├─ 📄wsgi.cpython-312.pyc
│  │     │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  ├─ 📄asgi.py
│  │     │  │  ├─ 📄base.py
│  │     │  │  ├─ 📄default.py
│  │     │  │  ├─ 📄mock.py
│  │     │  │  ├─ 📄wsgi.py
│  │     │  │  └─ 📄__init__.py
│  │     │  ├─ 📁__pycache__
│  │     │  │  ├─ 📄_api.cpython-312.pyc
│  │     │  │  ├─ 📄_auth.cpython-312.pyc
│  │     │  │  ├─ 📄_client.cpython-312.pyc
│  │     │  │  ├─ 📄_compat.cpython-312.pyc
│  │     │  │  ├─ 📄_config.cpython-312.pyc
│  │     │  │  ├─ 📄_content.cpython-312.pyc
│  │     │  │  ├─ 📄_decoders.cpython-312.pyc
│  │     │  │  ├─ 📄_exceptions.cpython-312.pyc
│  │     │  │  ├─ 📄_main.cpython-312.pyc
│  │     │  │  ├─ 📄_models.cpython-312.pyc
│  │     │  │  ├─ 📄_multipart.cpython-312.pyc
│  │     │  │  ├─ 📄_status_codes.cpython-312.pyc
│  │     │  │  ├─ 📄_types.cpython-312.pyc
│  │     │  │  ├─ 📄_urlparse.cpython-312.pyc
│  │     │  │  ├─ 📄_urls.cpython-312.pyc
│  │     │  │  ├─ 📄_utils.cpython-312.pyc
│  │     │  │  ├─ 📄__init__.cpython-312.pyc
│  │     │  │  └─ 📄__version__.cpython-312.pyc
│  │     │  ├─ 📄py.typed
│  │     │  ├─ 📄_api.py
│  │     │  ├─ 📄_auth.py
│  │     │  ├─ 📄_client.py
│  │     │  ├─ 📄_compat.py
│  │     │  ├─ 📄_config.py
│  │     │  ├─ 📄_content.py
│  │     │  ├─ 📄_decoders.py
│  │     │  ├─ 📄_exceptions.py
│  │     │  ├─ 📄_main.py
│  │     │  ├─ 📄_models.py
│  │     │  ├─ 📄_multipart.py
│  │     │  ├─ 📄_status_codes.py
│  │     │  ├─ 📄_types.py
│  │     │  ├─ 📄_urlparse.py
│  │     │  ├─ 📄_urls.py
│  │     │  ├─ 📄_utils.py
│  │     │  ├─ 📄__init__.py
│  │     │  └─ 📄__version__.py
│  │     ├─ 📁httpx-0.27.0.dist-info
│  │     │  ├─ 📁licenses
│  │     │  │  └─ 📄LICENSE.md
│  │     │  ├─ 📄entry_points.txt
│  │     │  ├─ 📄INSTALLER
│  │     │  ├─ 📄METADATA
│  │     │  ├─ 📄RECORD
│  │     │  └─ 📄WHEEL
│  │     ├─ 📁idna
│  │     │  ├─ 📁__pycache__
│  │     │  │  ├─ 📄codec.cpython-312.pyc
│  │     │  │  ├─ 📄compat.cpython-312.pyc
│  │     │  │  ├─ 📄core.cpython-312.pyc
│  │     │  │  ├─ 📄idnadata.cpython-312.pyc
│  │     │  │  ├─ 📄intranges.cpython-312.pyc
│  │     │  │  ├─ 📄package_data.cpython-312.pyc
│  │     │  │  ├─ 📄uts46data.cpython-312.pyc
│  │     │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  ├─ 📄codec.py
│  │     │  ├─ 📄compat.py
│  │     │  ├─ 📄core.py
│  │     │  ├─ 📄idnadata.py
│  │     │  ├─ 📄intranges.py
│  │     │  ├─ 📄package_data.py
│  │     │  ├─ 📄py.typed
│  │     │  ├─ 📄uts46data.py
│  │     │  └─ 📄__init__.py
│  │     ├─ 📁idna-3.7.dist-info
│  │     │  ├─ 📄INSTALLER
│  │     │  ├─ 📄LICENSE.md
│  │     │  ├─ 📄METADATA
│  │     │  ├─ 📄RECORD
│  │     │  └─ 📄WHEEL
│  │     ├─ 📁itsdangerous
│  │     │  ├─ 📁__pycache__
│  │     │  │  ├─ 📄encoding.cpython-312.pyc
│  │     │  │  ├─ 📄exc.cpython-312.pyc
│  │     │  │  ├─ 📄serializer.cpython-312.pyc
│  │     │  │  ├─ 📄signer.cpython-312.pyc
│  │     │  │  ├─ 📄timed.cpython-312.pyc
│  │     │  │  ├─ 📄url_safe.cpython-312.pyc
│  │     │  │  ├─ 📄_json.cpython-312.pyc
│  │     │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  ├─ 📄encoding.py
│  │     │  ├─ 📄exc.py
│  │     │  ├─ 📄py.typed
│  │     │  ├─ 📄serializer.py
│  │     │  ├─ 📄signer.py
│  │     │  ├─ 📄timed.py
│  │     │  ├─ 📄url_safe.py
│  │     │  ├─ 📄_json.py
│  │     │  └─ 📄__init__.py
│  │     ├─ 📁itsdangerous-2.2.0.dist-info
│  │     │  ├─ 📄INSTALLER
│  │     │  ├─ 📄LICENSE.txt
│  │     │  ├─ 📄METADATA
│  │     │  ├─ 📄RECORD
│  │     │  └─ 📄WHEEL
│  │     ├─ 📁jinja2
│  │     │  ├─ 📁__pycache__
│  │     │  │  ├─ 📄async_utils.cpython-312.pyc
│  │     │  │  ├─ 📄bccache.cpython-312.pyc
│  │     │  │  ├─ 📄compiler.cpython-312.pyc
│  │     │  │  ├─ 📄constants.cpython-312.pyc
│  │     │  │  ├─ 📄debug.cpython-312.pyc
│  │     │  │  ├─ 📄defaults.cpython-312.pyc
│  │     │  │  ├─ 📄environment.cpython-312.pyc
│  │     │  │  ├─ 📄exceptions.cpython-312.pyc
│  │     │  │  ├─ 📄ext.cpython-312.pyc
│  │     │  │  ├─ 📄filters.cpython-312.pyc
│  │     │  │  ├─ 📄idtracking.cpython-312.pyc
│  │     │  │  ├─ 📄lexer.cpython-312.pyc
│  │     │  │  ├─ 📄loaders.cpython-312.pyc
│  │     │  │  ├─ 📄meta.cpython-312.pyc
│  │     │  │  ├─ 📄nativetypes.cpython-312.pyc
│  │     │  │  ├─ 📄nodes.cpython-312.pyc
│  │     │  │  ├─ 📄optimizer.cpython-312.pyc
│  │     │  │  ├─ 📄parser.cpython-312.pyc
│  │     │  │  ├─ 📄runtime.cpython-312.pyc
│  │     │  │  ├─ 📄sandbox.cpython-312.pyc
│  │     │  │  ├─ 📄tests.cpython-312.pyc
│  │     │  │  ├─ 📄utils.cpython-312.pyc
│  │     │  │  ├─ 📄visitor.cpython-312.pyc
│  │     │  │  ├─ 📄_identifier.cpython-312.pyc
│  │     │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  ├─ 📄async_utils.py
│  │     │  ├─ 📄bccache.py
│  │     │  ├─ 📄compiler.py
│  │     │  ├─ 📄constants.py
│  │     │  ├─ 📄debug.py
│  │     │  ├─ 📄defaults.py
│  │     │  ├─ 📄environment.py
│  │     │  ├─ 📄exceptions.py
│  │     │  ├─ 📄ext.py
│  │     │  ├─ 📄filters.py
│  │     │  ├─ 📄idtracking.py
│  │     │  ├─ 📄lexer.py
│  │     │  ├─ 📄loaders.py
│  │     │  ├─ 📄meta.py
│  │     │  ├─ 📄nativetypes.py
│  │     │  ├─ 📄nodes.py
│  │     │  ├─ 📄optimizer.py
│  │     │  ├─ 📄parser.py
│  │     │  ├─ 📄py.typed
│  │     │  ├─ 📄runtime.py
│  │     │  ├─ 📄sandbox.py
│  │     │  ├─ 📄tests.py
│  │     │  ├─ 📄utils.py
│  │     │  ├─ 📄visitor.py
│  │     │  ├─ 📄_identifier.py
│  │     │  └─ 📄__init__.py
│  │     ├─ 📁jinja2-3.1.4.dist-info
│  │     │  ├─ 📄entry_points.txt
│  │     │  ├─ 📄INSTALLER
│  │     │  ├─ 📄LICENSE.txt
│  │     │  ├─ 📄METADATA
│  │     │  ├─ 📄RECORD
│  │     │  └─ 📄WHEEL
│  │     ├─ 📁markupsafe
│  │     │  ├─ 📁__pycache__
│  │     │  │  ├─ 📄_native.cpython-312.pyc
│  │     │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  ├─ 📄py.typed
│  │     │  ├─ 📄_native.py
│  │     │  ├─ 📄_speedups.c
│  │     │  ├─ 📄_speedups.cp312-win_amd64.pyd
│  │     │  ├─ 📄_speedups.pyi
│  │     │  └─ 📄__init__.py
│  │     ├─ 📁MarkupSafe-2.1.5.dist-info
│  │     │  ├─ 📄INSTALLER
│  │     │  ├─ 📄LICENSE.rst
│  │     │  ├─ 📄METADATA
│  │     │  ├─ 📄RECORD
│  │     │  ├─ 📄top_level.txt
│  │     │  └─ 📄WHEEL
│  │     ├─ 📁nodeenv-1.8.0.dist-info
│  │     │  ├─ 📄AUTHORS
│  │     │  ├─ 📄entry_points.txt
│  │     │  ├─ 📄INSTALLER
│  │     │  ├─ 📄LICENSE
│  │     │  ├─ 📄METADATA
│  │     │  ├─ 📄RECORD
│  │     │  ├─ 📄top_level.txt
│  │     │  └─ 📄WHEEL
│  │     ├─ 📁pip
│  │     │  ├─ 📁_internal
│  │     │  │  ├─ 📁cli
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄autocompletion.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄base_command.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄cmdoptions.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄command_context.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄main.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄main_parser.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄parser.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄progress_bars.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄req_command.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄spinners.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄status_codes.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄autocompletion.py
│  │     │  │  │  ├─ 📄base_command.py
│  │     │  │  │  ├─ 📄cmdoptions.py
│  │     │  │  │  ├─ 📄command_context.py
│  │     │  │  │  ├─ 📄main.py
│  │     │  │  │  ├─ 📄main_parser.py
│  │     │  │  │  ├─ 📄parser.py
│  │     │  │  │  ├─ 📄progress_bars.py
│  │     │  │  │  ├─ 📄req_command.py
│  │     │  │  │  ├─ 📄spinners.py
│  │     │  │  │  ├─ 📄status_codes.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁commands
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄freeze.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄install.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄uninstall.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄cache.py
│  │     │  │  │  ├─ 📄check.py
│  │     │  │  │  ├─ 📄completion.py
│  │     │  │  │  ├─ 📄configuration.py
│  │     │  │  │  ├─ 📄debug.py
│  │     │  │  │  ├─ 📄download.py
│  │     │  │  │  ├─ 📄freeze.py
│  │     │  │  │  ├─ 📄hash.py
│  │     │  │  │  ├─ 📄help.py
│  │     │  │  │  ├─ 📄index.py
│  │     │  │  │  ├─ 📄inspect.py
│  │     │  │  │  ├─ 📄install.py
│  │     │  │  │  ├─ 📄list.py
│  │     │  │  │  ├─ 📄search.py
│  │     │  │  │  ├─ 📄show.py
│  │     │  │  │  ├─ 📄uninstall.py
│  │     │  │  │  ├─ 📄wheel.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁distributions
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄base.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄installed.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄sdist.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄wheel.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄base.py
│  │     │  │  │  ├─ 📄installed.py
│  │     │  │  │  ├─ 📄sdist.py
│  │     │  │  │  ├─ 📄wheel.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁index
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄collector.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄package_finder.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄sources.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄collector.py
│  │     │  │  │  ├─ 📄package_finder.py
│  │     │  │  │  ├─ 📄sources.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁locations
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄base.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_sysconfig.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄base.py
│  │     │  │  │  ├─ 📄_distutils.py
│  │     │  │  │  ├─ 📄_sysconfig.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁metadata
│  │     │  │  │  ├─ 📁importlib
│  │     │  │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  │  ├─ 📄_compat.cpython-312.pyc
│  │     │  │  │  │  │  ├─ 📄_dists.cpython-312.pyc
│  │     │  │  │  │  │  ├─ 📄_envs.cpython-312.pyc
│  │     │  │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_compat.py
│  │     │  │  │  │  ├─ 📄_dists.py
│  │     │  │  │  │  ├─ 📄_envs.py
│  │     │  │  │  │  └─ 📄__init__.py
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄base.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄pkg_resources.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_json.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄base.py
│  │     │  │  │  ├─ 📄pkg_resources.py
│  │     │  │  │  ├─ 📄_json.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁models
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄candidate.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄direct_url.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄format_control.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄index.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄installation_report.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄link.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄scheme.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄search_scope.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄selection_prefs.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄target_python.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄wheel.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄candidate.py
│  │     │  │  │  ├─ 📄direct_url.py
│  │     │  │  │  ├─ 📄format_control.py
│  │     │  │  │  ├─ 📄index.py
│  │     │  │  │  ├─ 📄installation_report.py
│  │     │  │  │  ├─ 📄link.py
│  │     │  │  │  ├─ 📄scheme.py
│  │     │  │  │  ├─ 📄search_scope.py
│  │     │  │  │  ├─ 📄selection_prefs.py
│  │     │  │  │  ├─ 📄target_python.py
│  │     │  │  │  ├─ 📄wheel.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁network
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄auth.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄cache.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄download.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄lazy_wheel.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄session.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄utils.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄auth.py
│  │     │  │  │  ├─ 📄cache.py
│  │     │  │  │  ├─ 📄download.py
│  │     │  │  │  ├─ 📄lazy_wheel.py
│  │     │  │  │  ├─ 📄session.py
│  │     │  │  │  ├─ 📄utils.py
│  │     │  │  │  ├─ 📄xmlrpc.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁operations
│  │     │  │  │  ├─ 📁build
│  │     │  │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  │  ├─ 📄build_tracker.cpython-312.pyc
│  │     │  │  │  │  │  ├─ 📄metadata.cpython-312.pyc
│  │     │  │  │  │  │  ├─ 📄metadata_editable.cpython-312.pyc
│  │     │  │  │  │  │  ├─ 📄metadata_legacy.cpython-312.pyc
│  │     │  │  │  │  │  ├─ 📄wheel.cpython-312.pyc
│  │     │  │  │  │  │  ├─ 📄wheel_editable.cpython-312.pyc
│  │     │  │  │  │  │  ├─ 📄wheel_legacy.cpython-312.pyc
│  │     │  │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄build_tracker.py
│  │     │  │  │  │  ├─ 📄metadata.py
│  │     │  │  │  │  ├─ 📄metadata_editable.py
│  │     │  │  │  │  ├─ 📄metadata_legacy.py
│  │     │  │  │  │  ├─ 📄wheel.py
│  │     │  │  │  │  ├─ 📄wheel_editable.py
│  │     │  │  │  │  ├─ 📄wheel_legacy.py
│  │     │  │  │  │  └─ 📄__init__.py
│  │     │  │  │  ├─ 📁install
│  │     │  │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  │  ├─ 📄editable_legacy.cpython-312.pyc
│  │     │  │  │  │  │  ├─ 📄wheel.cpython-312.pyc
│  │     │  │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄editable_legacy.py
│  │     │  │  │  │  ├─ 📄wheel.py
│  │     │  │  │  │  └─ 📄__init__.py
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄check.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄freeze.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄prepare.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄check.py
│  │     │  │  │  ├─ 📄freeze.py
│  │     │  │  │  ├─ 📄prepare.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁req
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄constructors.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄req_file.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄req_install.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄req_set.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄req_uninstall.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄constructors.py
│  │     │  │  │  ├─ 📄req_file.py
│  │     │  │  │  ├─ 📄req_install.py
│  │     │  │  │  ├─ 📄req_set.py
│  │     │  │  │  ├─ 📄req_uninstall.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁resolution
│  │     │  │  │  ├─ 📁legacy
│  │     │  │  │  │  ├─ 📄resolver.py
│  │     │  │  │  │  └─ 📄__init__.py
│  │     │  │  │  ├─ 📁resolvelib
│  │     │  │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  │  ├─ 📄base.cpython-312.pyc
│  │     │  │  │  │  │  ├─ 📄candidates.cpython-312.pyc
│  │     │  │  │  │  │  ├─ 📄factory.cpython-312.pyc
│  │     │  │  │  │  │  ├─ 📄found_candidates.cpython-312.pyc
│  │     │  │  │  │  │  ├─ 📄provider.cpython-312.pyc
│  │     │  │  │  │  │  ├─ 📄reporter.cpython-312.pyc
│  │     │  │  │  │  │  ├─ 📄requirements.cpython-312.pyc
│  │     │  │  │  │  │  ├─ 📄resolver.cpython-312.pyc
│  │     │  │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄base.py
│  │     │  │  │  │  ├─ 📄candidates.py
│  │     │  │  │  │  ├─ 📄factory.py
│  │     │  │  │  │  ├─ 📄found_candidates.py
│  │     │  │  │  │  ├─ 📄provider.py
│  │     │  │  │  │  ├─ 📄reporter.py
│  │     │  │  │  │  ├─ 📄requirements.py
│  │     │  │  │  │  ├─ 📄resolver.py
│  │     │  │  │  │  └─ 📄__init__.py
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄base.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄base.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁utils
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄appdirs.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄compat.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄compatibility_tags.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄deprecation.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄direct_url_helpers.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄egg_link.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄encoding.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄entrypoints.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄filesystem.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄filetypes.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄glibc.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄hashes.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄logging.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄misc.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄models.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄packaging.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄setuptools_build.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄subprocess.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄temp_dir.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄unpacking.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄urls.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄virtualenv.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄wheel.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_jaraco_text.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_log.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄appdirs.py
│  │     │  │  │  ├─ 📄compat.py
│  │     │  │  │  ├─ 📄compatibility_tags.py
│  │     │  │  │  ├─ 📄datetime.py
│  │     │  │  │  ├─ 📄deprecation.py
│  │     │  │  │  ├─ 📄direct_url_helpers.py
│  │     │  │  │  ├─ 📄egg_link.py
│  │     │  │  │  ├─ 📄encoding.py
│  │     │  │  │  ├─ 📄entrypoints.py
│  │     │  │  │  ├─ 📄filesystem.py
│  │     │  │  │  ├─ 📄filetypes.py
│  │     │  │  │  ├─ 📄glibc.py
│  │     │  │  │  ├─ 📄hashes.py
│  │     │  │  │  ├─ 📄logging.py
│  │     │  │  │  ├─ 📄misc.py
│  │     │  │  │  ├─ 📄models.py
│  │     │  │  │  ├─ 📄packaging.py
│  │     │  │  │  ├─ 📄setuptools_build.py
│  │     │  │  │  ├─ 📄subprocess.py
│  │     │  │  │  ├─ 📄temp_dir.py
│  │     │  │  │  ├─ 📄unpacking.py
│  │     │  │  │  ├─ 📄urls.py
│  │     │  │  │  ├─ 📄virtualenv.py
│  │     │  │  │  ├─ 📄wheel.py
│  │     │  │  │  ├─ 📄_jaraco_text.py
│  │     │  │  │  ├─ 📄_log.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁vcs
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄bazaar.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄git.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄mercurial.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄subversion.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄versioncontrol.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄bazaar.py
│  │     │  │  │  ├─ 📄git.py
│  │     │  │  │  ├─ 📄mercurial.py
│  │     │  │  │  ├─ 📄subversion.py
│  │     │  │  │  ├─ 📄versioncontrol.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁__pycache__
│  │     │  │  │  ├─ 📄build_env.cpython-312.pyc
│  │     │  │  │  ├─ 📄cache.cpython-312.pyc
│  │     │  │  │  ├─ 📄configuration.cpython-312.pyc
│  │     │  │  │  ├─ 📄exceptions.cpython-312.pyc
│  │     │  │  │  ├─ 📄pyproject.cpython-312.pyc
│  │     │  │  │  ├─ 📄self_outdated_check.cpython-312.pyc
│  │     │  │  │  ├─ 📄wheel_builder.cpython-312.pyc
│  │     │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  ├─ 📄build_env.py
│  │     │  │  ├─ 📄cache.py
│  │     │  │  ├─ 📄configuration.py
│  │     │  │  ├─ 📄exceptions.py
│  │     │  │  ├─ 📄main.py
│  │     │  │  ├─ 📄pyproject.py
│  │     │  │  ├─ 📄self_outdated_check.py
│  │     │  │  ├─ 📄wheel_builder.py
│  │     │  │  └─ 📄__init__.py
│  │     │  ├─ 📁_vendor
│  │     │  │  ├─ 📁cachecontrol
│  │     │  │  │  ├─ 📁caches
│  │     │  │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  │  ├─ 📄file_cache.cpython-312.pyc
│  │     │  │  │  │  │  ├─ 📄redis_cache.cpython-312.pyc
│  │     │  │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄file_cache.py
│  │     │  │  │  │  ├─ 📄redis_cache.py
│  │     │  │  │  │  └─ 📄__init__.py
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄adapter.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄cache.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄controller.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄filewrapper.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄serialize.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄wrapper.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄adapter.py
│  │     │  │  │  ├─ 📄cache.py
│  │     │  │  │  ├─ 📄controller.py
│  │     │  │  │  ├─ 📄filewrapper.py
│  │     │  │  │  ├─ 📄heuristics.py
│  │     │  │  │  ├─ 📄py.typed
│  │     │  │  │  ├─ 📄serialize.py
│  │     │  │  │  ├─ 📄wrapper.py
│  │     │  │  │  ├─ 📄_cmd.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁certifi
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄core.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄cacert.pem
│  │     │  │  │  ├─ 📄core.py
│  │     │  │  │  ├─ 📄py.typed
│  │     │  │  │  ├─ 📄__init__.py
│  │     │  │  │  └─ 📄__main__.py
│  │     │  │  ├─ 📁chardet
│  │     │  │  │  ├─ 📁cli
│  │     │  │  │  │  ├─ 📄chardetect.py
│  │     │  │  │  │  └─ 📄__init__.py
│  │     │  │  │  ├─ 📁metadata
│  │     │  │  │  │  ├─ 📄languages.py
│  │     │  │  │  │  └─ 📄__init__.py
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄big5freq.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄big5prober.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄chardistribution.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄charsetgroupprober.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄charsetprober.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄codingstatemachine.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄codingstatemachinedict.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄cp949prober.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄enums.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄escprober.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄escsm.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄eucjpprober.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄euckrfreq.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄euckrprober.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄euctwfreq.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄euctwprober.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄gb2312freq.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄gb2312prober.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄hebrewprober.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄jisfreq.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄johabfreq.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄johabprober.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄jpcntx.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄langbulgarianmodel.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄langgreekmodel.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄langhebrewmodel.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄langrussianmodel.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄langthaimodel.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄langturkishmodel.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄latin1prober.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄macromanprober.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄mbcharsetprober.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄mbcsgroupprober.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄mbcssm.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄resultdict.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄sbcharsetprober.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄sbcsgroupprober.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄sjisprober.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄universaldetector.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄utf1632prober.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄utf8prober.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄version.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄big5freq.py
│  │     │  │  │  ├─ 📄big5prober.py
│  │     │  │  │  ├─ 📄chardistribution.py
│  │     │  │  │  ├─ 📄charsetgroupprober.py
│  │     │  │  │  ├─ 📄charsetprober.py
│  │     │  │  │  ├─ 📄codingstatemachine.py
│  │     │  │  │  ├─ 📄codingstatemachinedict.py
│  │     │  │  │  ├─ 📄cp949prober.py
│  │     │  │  │  ├─ 📄enums.py
│  │     │  │  │  ├─ 📄escprober.py
│  │     │  │  │  ├─ 📄escsm.py
│  │     │  │  │  ├─ 📄eucjpprober.py
│  │     │  │  │  ├─ 📄euckrfreq.py
│  │     │  │  │  ├─ 📄euckrprober.py
│  │     │  │  │  ├─ 📄euctwfreq.py
│  │     │  │  │  ├─ 📄euctwprober.py
│  │     │  │  │  ├─ 📄gb2312freq.py
│  │     │  │  │  ├─ 📄gb2312prober.py
│  │     │  │  │  ├─ 📄hebrewprober.py
│  │     │  │  │  ├─ 📄jisfreq.py
│  │     │  │  │  ├─ 📄johabfreq.py
│  │     │  │  │  ├─ 📄johabprober.py
│  │     │  │  │  ├─ 📄jpcntx.py
│  │     │  │  │  ├─ 📄langbulgarianmodel.py
│  │     │  │  │  ├─ 📄langgreekmodel.py
│  │     │  │  │  ├─ 📄langhebrewmodel.py
│  │     │  │  │  ├─ 📄langhungarianmodel.py
│  │     │  │  │  ├─ 📄langrussianmodel.py
│  │     │  │  │  ├─ 📄langthaimodel.py
│  │     │  │  │  ├─ 📄langturkishmodel.py
│  │     │  │  │  ├─ 📄latin1prober.py
│  │     │  │  │  ├─ 📄macromanprober.py
│  │     │  │  │  ├─ 📄mbcharsetprober.py
│  │     │  │  │  ├─ 📄mbcsgroupprober.py
│  │     │  │  │  ├─ 📄mbcssm.py
│  │     │  │  │  ├─ 📄py.typed
│  │     │  │  │  ├─ 📄resultdict.py
│  │     │  │  │  ├─ 📄sbcharsetprober.py
│  │     │  │  │  ├─ 📄sbcsgroupprober.py
│  │     │  │  │  ├─ 📄sjisprober.py
│  │     │  │  │  ├─ 📄universaldetector.py
│  │     │  │  │  ├─ 📄utf1632prober.py
│  │     │  │  │  ├─ 📄utf8prober.py
│  │     │  │  │  ├─ 📄version.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁colorama
│  │     │  │  │  ├─ 📁tests
│  │     │  │  │  │  ├─ 📄ansitowin32_test.py
│  │     │  │  │  │  ├─ 📄ansi_test.py
│  │     │  │  │  │  ├─ 📄initialise_test.py
│  │     │  │  │  │  ├─ 📄isatty_test.py
│  │     │  │  │  │  ├─ 📄utils.py
│  │     │  │  │  │  ├─ 📄winterm_test.py
│  │     │  │  │  │  └─ 📄__init__.py
│  │     │  │  │  ├─ 📄ansi.py
│  │     │  │  │  ├─ 📄ansitowin32.py
│  │     │  │  │  ├─ 📄initialise.py
│  │     │  │  │  ├─ 📄win32.py
│  │     │  │  │  ├─ 📄winterm.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁distlib
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄compat.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄resources.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄scripts.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄util.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄compat.py
│  │     │  │  │  ├─ 📄database.py
│  │     │  │  │  ├─ 📄index.py
│  │     │  │  │  ├─ 📄locators.py
│  │     │  │  │  ├─ 📄manifest.py
│  │     │  │  │  ├─ 📄markers.py
│  │     │  │  │  ├─ 📄metadata.py
│  │     │  │  │  ├─ 📄resources.py
│  │     │  │  │  ├─ 📄scripts.py
│  │     │  │  │  ├─ 📄t32.exe
│  │     │  │  │  ├─ 📄t64-arm.exe
│  │     │  │  │  ├─ 📄t64.exe
│  │     │  │  │  ├─ 📄util.py
│  │     │  │  │  ├─ 📄version.py
│  │     │  │  │  ├─ 📄w32.exe
│  │     │  │  │  ├─ 📄w64-arm.exe
│  │     │  │  │  ├─ 📄w64.exe
│  │     │  │  │  ├─ 📄wheel.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁distro
│  │     │  │  │  ├─ 📄distro.py
│  │     │  │  │  ├─ 📄py.typed
│  │     │  │  │  ├─ 📄__init__.py
│  │     │  │  │  └─ 📄__main__.py
│  │     │  │  ├─ 📁idna
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄core.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄idnadata.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄intranges.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄package_data.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄codec.py
│  │     │  │  │  ├─ 📄compat.py
│  │     │  │  │  ├─ 📄core.py
│  │     │  │  │  ├─ 📄idnadata.py
│  │     │  │  │  ├─ 📄intranges.py
│  │     │  │  │  ├─ 📄package_data.py
│  │     │  │  │  ├─ 📄py.typed
│  │     │  │  │  ├─ 📄uts46data.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁msgpack
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄exceptions.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄ext.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄fallback.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄exceptions.py
│  │     │  │  │  ├─ 📄ext.py
│  │     │  │  │  ├─ 📄fallback.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁packaging
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄markers.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄requirements.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄specifiers.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄tags.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄utils.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄version.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_manylinux.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_musllinux.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_structures.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄__about__.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄markers.py
│  │     │  │  │  ├─ 📄py.typed
│  │     │  │  │  ├─ 📄requirements.py
│  │     │  │  │  ├─ 📄specifiers.py
│  │     │  │  │  ├─ 📄tags.py
│  │     │  │  │  ├─ 📄utils.py
│  │     │  │  │  ├─ 📄version.py
│  │     │  │  │  ├─ 📄_manylinux.py
│  │     │  │  │  ├─ 📄_musllinux.py
│  │     │  │  │  ├─ 📄_structures.py
│  │     │  │  │  ├─ 📄__about__.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁pkg_resources
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁platformdirs
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄api.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄version.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄windows.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄android.py
│  │     │  │  │  ├─ 📄api.py
│  │     │  │  │  ├─ 📄macos.py
│  │     │  │  │  ├─ 📄py.typed
│  │     │  │  │  ├─ 📄unix.py
│  │     │  │  │  ├─ 📄version.py
│  │     │  │  │  ├─ 📄windows.py
│  │     │  │  │  ├─ 📄__init__.py
│  │     │  │  │  └─ 📄__main__.py
│  │     │  │  ├─ 📁pygments
│  │     │  │  │  ├─ 📁filters
│  │     │  │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.py
│  │     │  │  │  ├─ 📁formatters
│  │     │  │  │  │  ├─ 📄bbcode.py
│  │     │  │  │  │  ├─ 📄groff.py
│  │     │  │  │  │  ├─ 📄html.py
│  │     │  │  │  │  ├─ 📄img.py
│  │     │  │  │  │  ├─ 📄irc.py
│  │     │  │  │  │  ├─ 📄latex.py
│  │     │  │  │  │  ├─ 📄other.py
│  │     │  │  │  │  ├─ 📄pangomarkup.py
│  │     │  │  │  │  ├─ 📄rtf.py
│  │     │  │  │  │  ├─ 📄svg.py
│  │     │  │  │  │  ├─ 📄terminal.py
│  │     │  │  │  │  ├─ 📄terminal256.py
│  │     │  │  │  │  ├─ 📄_mapping.py
│  │     │  │  │  │  └─ 📄__init__.py
│  │     │  │  │  ├─ 📁lexers
│  │     │  │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  │  ├─ 📄_mapping.cpython-312.pyc
│  │     │  │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄python.py
│  │     │  │  │  │  ├─ 📄_mapping.py
│  │     │  │  │  │  └─ 📄__init__.py
│  │     │  │  │  ├─ 📁styles
│  │     │  │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.py
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄filter.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄lexer.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄modeline.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄plugin.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄regexopt.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄style.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄token.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄util.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄cmdline.py
│  │     │  │  │  ├─ 📄console.py
│  │     │  │  │  ├─ 📄filter.py
│  │     │  │  │  ├─ 📄formatter.py
│  │     │  │  │  ├─ 📄lexer.py
│  │     │  │  │  ├─ 📄modeline.py
│  │     │  │  │  ├─ 📄plugin.py
│  │     │  │  │  ├─ 📄regexopt.py
│  │     │  │  │  ├─ 📄scanner.py
│  │     │  │  │  ├─ 📄sphinxext.py
│  │     │  │  │  ├─ 📄style.py
│  │     │  │  │  ├─ 📄token.py
│  │     │  │  │  ├─ 📄unistring.py
│  │     │  │  │  ├─ 📄util.py
│  │     │  │  │  ├─ 📄__init__.py
│  │     │  │  │  └─ 📄__main__.py
│  │     │  │  ├─ 📁pyparsing
│  │     │  │  │  ├─ 📁diagram
│  │     │  │  │  │  └─ 📄__init__.py
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄actions.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄common.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄core.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄exceptions.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄helpers.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄results.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄testing.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄unicode.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄util.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄actions.py
│  │     │  │  │  ├─ 📄common.py
│  │     │  │  │  ├─ 📄core.py
│  │     │  │  │  ├─ 📄exceptions.py
│  │     │  │  │  ├─ 📄helpers.py
│  │     │  │  │  ├─ 📄py.typed
│  │     │  │  │  ├─ 📄results.py
│  │     │  │  │  ├─ 📄testing.py
│  │     │  │  │  ├─ 📄unicode.py
│  │     │  │  │  ├─ 📄util.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁pyproject_hooks
│  │     │  │  │  ├─ 📁_in_process
│  │     │  │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_in_process.py
│  │     │  │  │  │  └─ 📄__init__.py
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄_impl.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄_compat.py
│  │     │  │  │  ├─ 📄_impl.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁requests
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄adapters.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄api.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄auth.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄certs.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄compat.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄cookies.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄exceptions.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄hooks.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄models.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄packages.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄sessions.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄status_codes.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄structures.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄utils.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_internal_utils.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄__init__.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__version__.cpython-312.pyc
│  │     │  │  │  ├─ 📄adapters.py
│  │     │  │  │  ├─ 📄api.py
│  │     │  │  │  ├─ 📄auth.py
│  │     │  │  │  ├─ 📄certs.py
│  │     │  │  │  ├─ 📄compat.py
│  │     │  │  │  ├─ 📄cookies.py
│  │     │  │  │  ├─ 📄exceptions.py
│  │     │  │  │  ├─ 📄help.py
│  │     │  │  │  ├─ 📄hooks.py
│  │     │  │  │  ├─ 📄models.py
│  │     │  │  │  ├─ 📄packages.py
│  │     │  │  │  ├─ 📄sessions.py
│  │     │  │  │  ├─ 📄status_codes.py
│  │     │  │  │  ├─ 📄structures.py
│  │     │  │  │  ├─ 📄utils.py
│  │     │  │  │  ├─ 📄_internal_utils.py
│  │     │  │  │  ├─ 📄__init__.py
│  │     │  │  │  └─ 📄__version__.py
│  │     │  │  ├─ 📁resolvelib
│  │     │  │  │  ├─ 📁compat
│  │     │  │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  │  ├─ 📄collections_abc.cpython-312.pyc
│  │     │  │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄collections_abc.py
│  │     │  │  │  │  └─ 📄__init__.py
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄providers.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄reporters.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄resolvers.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄structs.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄providers.py
│  │     │  │  │  ├─ 📄py.typed
│  │     │  │  │  ├─ 📄reporters.py
│  │     │  │  │  ├─ 📄resolvers.py
│  │     │  │  │  ├─ 📄structs.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁rich
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄abc.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄align.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄ansi.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄box.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄cells.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄color.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄color_triplet.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄columns.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄console.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄constrain.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄containers.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄control.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄default_styles.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄emoji.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄errors.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄filesize.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄file_proxy.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄highlighter.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄jupyter.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄live.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄live_render.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄logging.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄markup.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄measure.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄padding.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄pager.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄palette.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄panel.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄pretty.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄progress.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄progress_bar.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄protocol.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄region.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄repr.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄scope.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄screen.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄segment.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄spinner.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄style.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄styled.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄syntax.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄table.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄terminal_theme.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄text.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄theme.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄themes.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄traceback.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_cell_widths.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_emoji_codes.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_emoji_replace.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_export_format.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_extension.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_fileno.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_log_render.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_loop.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_null_file.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_palettes.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_pick.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_ratio.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_spinners.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_win32_console.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_windows.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_wrap.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄abc.py
│  │     │  │  │  ├─ 📄align.py
│  │     │  │  │  ├─ 📄ansi.py
│  │     │  │  │  ├─ 📄bar.py
│  │     │  │  │  ├─ 📄box.py
│  │     │  │  │  ├─ 📄cells.py
│  │     │  │  │  ├─ 📄color.py
│  │     │  │  │  ├─ 📄color_triplet.py
│  │     │  │  │  ├─ 📄columns.py
│  │     │  │  │  ├─ 📄console.py
│  │     │  │  │  ├─ 📄constrain.py
│  │     │  │  │  ├─ 📄containers.py
│  │     │  │  │  ├─ 📄control.py
│  │     │  │  │  ├─ 📄default_styles.py
│  │     │  │  │  ├─ 📄diagnose.py
│  │     │  │  │  ├─ 📄emoji.py
│  │     │  │  │  ├─ 📄errors.py
│  │     │  │  │  ├─ 📄filesize.py
│  │     │  │  │  ├─ 📄file_proxy.py
│  │     │  │  │  ├─ 📄highlighter.py
│  │     │  │  │  ├─ 📄json.py
│  │     │  │  │  ├─ 📄jupyter.py
│  │     │  │  │  ├─ 📄layout.py
│  │     │  │  │  ├─ 📄live.py
│  │     │  │  │  ├─ 📄live_render.py
│  │     │  │  │  ├─ 📄logging.py
│  │     │  │  │  ├─ 📄markup.py
│  │     │  │  │  ├─ 📄measure.py
│  │     │  │  │  ├─ 📄padding.py
│  │     │  │  │  ├─ 📄pager.py
│  │     │  │  │  ├─ 📄palette.py
│  │     │  │  │  ├─ 📄panel.py
│  │     │  │  │  ├─ 📄pretty.py
│  │     │  │  │  ├─ 📄progress.py
│  │     │  │  │  ├─ 📄progress_bar.py
│  │     │  │  │  ├─ 📄prompt.py
│  │     │  │  │  ├─ 📄protocol.py
│  │     │  │  │  ├─ 📄py.typed
│  │     │  │  │  ├─ 📄region.py
│  │     │  │  │  ├─ 📄repr.py
│  │     │  │  │  ├─ 📄rule.py
│  │     │  │  │  ├─ 📄scope.py
│  │     │  │  │  ├─ 📄screen.py
│  │     │  │  │  ├─ 📄segment.py
│  │     │  │  │  ├─ 📄spinner.py
│  │     │  │  │  ├─ 📄status.py
│  │     │  │  │  ├─ 📄style.py
│  │     │  │  │  ├─ 📄styled.py
│  │     │  │  │  ├─ 📄syntax.py
│  │     │  │  │  ├─ 📄table.py
│  │     │  │  │  ├─ 📄terminal_theme.py
│  │     │  │  │  ├─ 📄text.py
│  │     │  │  │  ├─ 📄theme.py
│  │     │  │  │  ├─ 📄themes.py
│  │     │  │  │  ├─ 📄traceback.py
│  │     │  │  │  ├─ 📄tree.py
│  │     │  │  │  ├─ 📄_cell_widths.py
│  │     │  │  │  ├─ 📄_emoji_codes.py
│  │     │  │  │  ├─ 📄_emoji_replace.py
│  │     │  │  │  ├─ 📄_export_format.py
│  │     │  │  │  ├─ 📄_extension.py
│  │     │  │  │  ├─ 📄_fileno.py
│  │     │  │  │  ├─ 📄_inspect.py
│  │     │  │  │  ├─ 📄_log_render.py
│  │     │  │  │  ├─ 📄_loop.py
│  │     │  │  │  ├─ 📄_null_file.py
│  │     │  │  │  ├─ 📄_palettes.py
│  │     │  │  │  ├─ 📄_pick.py
│  │     │  │  │  ├─ 📄_ratio.py
│  │     │  │  │  ├─ 📄_spinners.py
│  │     │  │  │  ├─ 📄_stack.py
│  │     │  │  │  ├─ 📄_timer.py
│  │     │  │  │  ├─ 📄_win32_console.py
│  │     │  │  │  ├─ 📄_windows.py
│  │     │  │  │  ├─ 📄_windows_renderer.py
│  │     │  │  │  ├─ 📄_wrap.py
│  │     │  │  │  ├─ 📄__init__.py
│  │     │  │  │  └─ 📄__main__.py
│  │     │  │  ├─ 📁tenacity
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄after.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄before.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄before_sleep.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄nap.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄retry.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄stop.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄wait.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_asyncio.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_utils.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄after.py
│  │     │  │  │  ├─ 📄before.py
│  │     │  │  │  ├─ 📄before_sleep.py
│  │     │  │  │  ├─ 📄nap.py
│  │     │  │  │  ├─ 📄py.typed
│  │     │  │  │  ├─ 📄retry.py
│  │     │  │  │  ├─ 📄stop.py
│  │     │  │  │  ├─ 📄tornadoweb.py
│  │     │  │  │  ├─ 📄wait.py
│  │     │  │  │  ├─ 📄_asyncio.py
│  │     │  │  │  ├─ 📄_utils.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁tomli
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄_parser.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_re.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_types.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄py.typed
│  │     │  │  │  ├─ 📄_parser.py
│  │     │  │  │  ├─ 📄_re.py
│  │     │  │  │  ├─ 📄_types.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁truststore
│  │     │  │  │  ├─ 📄py.typed
│  │     │  │  │  ├─ 📄_api.py
│  │     │  │  │  ├─ 📄_macos.py
│  │     │  │  │  ├─ 📄_openssl.py
│  │     │  │  │  ├─ 📄_ssl_constants.py
│  │     │  │  │  ├─ 📄_windows.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁urllib3
│  │     │  │  │  ├─ 📁contrib
│  │     │  │  │  │  ├─ 📁_securetransport
│  │     │  │  │  │  │  ├─ 📄bindings.py
│  │     │  │  │  │  │  ├─ 📄low_level.py
│  │     │  │  │  │  │  └─ 📄__init__.py
│  │     │  │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  │  ├─ 📄socks.cpython-312.pyc
│  │     │  │  │  │  │  ├─ 📄_appengine_environ.cpython-312.pyc
│  │     │  │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄appengine.py
│  │     │  │  │  │  ├─ 📄ntlmpool.py
│  │     │  │  │  │  ├─ 📄pyopenssl.py
│  │     │  │  │  │  ├─ 📄securetransport.py
│  │     │  │  │  │  ├─ 📄socks.py
│  │     │  │  │  │  ├─ 📄_appengine_environ.py
│  │     │  │  │  │  └─ 📄__init__.py
│  │     │  │  │  ├─ 📁packages
│  │     │  │  │  │  ├─ 📁backports
│  │     │  │  │  │  │  ├─ 📄makefile.py
│  │     │  │  │  │  │  ├─ 📄weakref_finalize.py
│  │     │  │  │  │  │  └─ 📄__init__.py
│  │     │  │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  │  ├─ 📄six.cpython-312.pyc
│  │     │  │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄six.py
│  │     │  │  │  │  └─ 📄__init__.py
│  │     │  │  │  ├─ 📁util
│  │     │  │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  │  ├─ 📄connection.cpython-312.pyc
│  │     │  │  │  │  │  ├─ 📄proxy.cpython-312.pyc
│  │     │  │  │  │  │  ├─ 📄queue.cpython-312.pyc
│  │     │  │  │  │  │  ├─ 📄request.cpython-312.pyc
│  │     │  │  │  │  │  ├─ 📄response.cpython-312.pyc
│  │     │  │  │  │  │  ├─ 📄retry.cpython-312.pyc
│  │     │  │  │  │  │  ├─ 📄ssltransport.cpython-312.pyc
│  │     │  │  │  │  │  ├─ 📄ssl_.cpython-312.pyc
│  │     │  │  │  │  │  ├─ 📄ssl_match_hostname.cpython-312.pyc
│  │     │  │  │  │  │  ├─ 📄timeout.cpython-312.pyc
│  │     │  │  │  │  │  ├─ 📄url.cpython-312.pyc
│  │     │  │  │  │  │  ├─ 📄wait.cpython-312.pyc
│  │     │  │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄connection.py
│  │     │  │  │  │  ├─ 📄proxy.py
│  │     │  │  │  │  ├─ 📄queue.py
│  │     │  │  │  │  ├─ 📄request.py
│  │     │  │  │  │  ├─ 📄response.py
│  │     │  │  │  │  ├─ 📄retry.py
│  │     │  │  │  │  ├─ 📄ssltransport.py
│  │     │  │  │  │  ├─ 📄ssl_.py
│  │     │  │  │  │  ├─ 📄ssl_match_hostname.py
│  │     │  │  │  │  ├─ 📄timeout.py
│  │     │  │  │  │  ├─ 📄url.py
│  │     │  │  │  │  ├─ 📄wait.py
│  │     │  │  │  │  └─ 📄__init__.py
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄connection.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄connectionpool.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄exceptions.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄fields.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄filepost.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄poolmanager.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄request.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄response.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_collections.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_version.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄connection.py
│  │     │  │  │  ├─ 📄connectionpool.py
│  │     │  │  │  ├─ 📄exceptions.py
│  │     │  │  │  ├─ 📄fields.py
│  │     │  │  │  ├─ 📄filepost.py
│  │     │  │  │  ├─ 📄poolmanager.py
│  │     │  │  │  ├─ 📄request.py
│  │     │  │  │  ├─ 📄response.py
│  │     │  │  │  ├─ 📄_collections.py
│  │     │  │  │  ├─ 📄_version.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁webencodings
│  │     │  │  │  ├─ 📄labels.py
│  │     │  │  │  ├─ 📄mklabels.py
│  │     │  │  │  ├─ 📄tests.py
│  │     │  │  │  ├─ 📄x_user_defined.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁__pycache__
│  │     │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  ├─ 📄six.py
│  │     │  │  ├─ 📄typing_extensions.py
│  │     │  │  ├─ 📄vendor.txt
│  │     │  │  └─ 📄__init__.py
│  │     │  ├─ 📁__pycache__
│  │     │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  ├─ 📄py.typed
│  │     │  ├─ 📄__init__.py
│  │     │  ├─ 📄__main__.py
│  │     │  └─ 📄__pip-runner__.py
│  │     ├─ 📁pip-24.0.dist-info
│  │     │  ├─ 📄AUTHORS.txt
│  │     │  ├─ 📄entry_points.txt
│  │     │  ├─ 📄INSTALLER
│  │     │  ├─ 📄LICENSE.txt
│  │     │  ├─ 📄METADATA
│  │     │  ├─ 📄RECORD
│  │     │  ├─ 📄top_level.txt
│  │     │  └─ 📄WHEEL
│  │     ├─ 📁pkg_resources
│  │     │  ├─ 📁extern
│  │     │  │  ├─ 📁__pycache__
│  │     │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  └─ 📄__init__.py
│  │     │  ├─ 📁_vendor
│  │     │  │  ├─ 📁backports
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄tarfile.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄tarfile.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁importlib_resources
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄abc.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄readers.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄simple.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_adapters.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_common.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_compat.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_itertools.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_legacy.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄abc.py
│  │     │  │  │  ├─ 📄py.typed
│  │     │  │  │  ├─ 📄readers.py
│  │     │  │  │  ├─ 📄simple.py
│  │     │  │  │  ├─ 📄_adapters.py
│  │     │  │  │  ├─ 📄_common.py
│  │     │  │  │  ├─ 📄_compat.py
│  │     │  │  │  ├─ 📄_itertools.py
│  │     │  │  │  ├─ 📄_legacy.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁jaraco
│  │     │  │  │  ├─ 📁functools
│  │     │  │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄py.typed
│  │     │  │  │  │  ├─ 📄__init__.py
│  │     │  │  │  │  └─ 📄__init__.pyi
│  │     │  │  │  ├─ 📁text
│  │     │  │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.py
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄context.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄context.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁more_itertools
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄more.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄recipes.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄more.py
│  │     │  │  │  ├─ 📄more.pyi
│  │     │  │  │  ├─ 📄py.typed
│  │     │  │  │  ├─ 📄recipes.py
│  │     │  │  │  ├─ 📄recipes.pyi
│  │     │  │  │  ├─ 📄__init__.py
│  │     │  │  │  └─ 📄__init__.pyi
│  │     │  │  ├─ 📁packaging
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄markers.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄metadata.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄requirements.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄specifiers.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄tags.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄utils.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄version.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_elffile.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_manylinux.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_musllinux.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_parser.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_structures.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_tokenizer.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄markers.py
│  │     │  │  │  ├─ 📄metadata.py
│  │     │  │  │  ├─ 📄py.typed
│  │     │  │  │  ├─ 📄requirements.py
│  │     │  │  │  ├─ 📄specifiers.py
│  │     │  │  │  ├─ 📄tags.py
│  │     │  │  │  ├─ 📄utils.py
│  │     │  │  │  ├─ 📄version.py
│  │     │  │  │  ├─ 📄_elffile.py
│  │     │  │  │  ├─ 📄_manylinux.py
│  │     │  │  │  ├─ 📄_musllinux.py
│  │     │  │  │  ├─ 📄_parser.py
│  │     │  │  │  ├─ 📄_structures.py
│  │     │  │  │  ├─ 📄_tokenizer.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁platformdirs
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄android.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄api.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄macos.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄unix.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄version.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄windows.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄__init__.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__main__.cpython-312.pyc
│  │     │  │  │  ├─ 📄android.py
│  │     │  │  │  ├─ 📄api.py
│  │     │  │  │  ├─ 📄macos.py
│  │     │  │  │  ├─ 📄py.typed
│  │     │  │  │  ├─ 📄unix.py
│  │     │  │  │  ├─ 📄version.py
│  │     │  │  │  ├─ 📄windows.py
│  │     │  │  │  ├─ 📄__init__.py
│  │     │  │  │  └─ 📄__main__.py
│  │     │  │  ├─ 📁__pycache__
│  │     │  │  │  ├─ 📄typing_extensions.cpython-312.pyc
│  │     │  │  │  ├─ 📄zipp.cpython-312.pyc
│  │     │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  ├─ 📄typing_extensions.py
│  │     │  │  ├─ 📄zipp.py
│  │     │  │  └─ 📄__init__.py
│  │     │  ├─ 📁__pycache__
│  │     │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  └─ 📄__init__.py
│  │     ├─ 📁pydantic
│  │     │  ├─ 📁deprecated
│  │     │  │  ├─ 📁__pycache__
│  │     │  │  │  ├─ 📄class_validators.cpython-312.pyc
│  │     │  │  │  ├─ 📄config.cpython-312.pyc
│  │     │  │  │  ├─ 📄copy_internals.cpython-312.pyc
│  │     │  │  │  ├─ 📄decorator.cpython-312.pyc
│  │     │  │  │  ├─ 📄json.cpython-312.pyc
│  │     │  │  │  ├─ 📄parse.cpython-312.pyc
│  │     │  │  │  ├─ 📄tools.cpython-312.pyc
│  │     │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  ├─ 📄class_validators.py
│  │     │  │  ├─ 📄config.py
│  │     │  │  ├─ 📄copy_internals.py
│  │     │  │  ├─ 📄decorator.py
│  │     │  │  ├─ 📄json.py
│  │     │  │  ├─ 📄parse.py
│  │     │  │  ├─ 📄tools.py
│  │     │  │  └─ 📄__init__.py
│  │     │  ├─ 📁plugin
│  │     │  │  ├─ 📁__pycache__
│  │     │  │  │  ├─ 📄_loader.cpython-312.pyc
│  │     │  │  │  ├─ 📄_schema_validator.cpython-312.pyc
│  │     │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  ├─ 📄_loader.py
│  │     │  │  ├─ 📄_schema_validator.py
│  │     │  │  └─ 📄__init__.py
│  │     │  ├─ 📁v1
│  │     │  │  ├─ 📁__pycache__
│  │     │  │  │  ├─ 📄annotated_types.cpython-312.pyc
│  │     │  │  │  ├─ 📄class_validators.cpython-312.pyc
│  │     │  │  │  ├─ 📄color.cpython-312.pyc
│  │     │  │  │  ├─ 📄config.cpython-312.pyc
│  │     │  │  │  ├─ 📄dataclasses.cpython-312.pyc
│  │     │  │  │  ├─ 📄datetime_parse.cpython-312.pyc
│  │     │  │  │  ├─ 📄decorator.cpython-312.pyc
│  │     │  │  │  ├─ 📄env_settings.cpython-312.pyc
│  │     │  │  │  ├─ 📄errors.cpython-312.pyc
│  │     │  │  │  ├─ 📄error_wrappers.cpython-312.pyc
│  │     │  │  │  ├─ 📄fields.cpython-312.pyc
│  │     │  │  │  ├─ 📄generics.cpython-312.pyc
│  │     │  │  │  ├─ 📄json.cpython-312.pyc
│  │     │  │  │  ├─ 📄main.cpython-312.pyc
│  │     │  │  │  ├─ 📄mypy.cpython-312.pyc
│  │     │  │  │  ├─ 📄networks.cpython-312.pyc
│  │     │  │  │  ├─ 📄parse.cpython-312.pyc
│  │     │  │  │  ├─ 📄schema.cpython-312.pyc
│  │     │  │  │  ├─ 📄tools.cpython-312.pyc
│  │     │  │  │  ├─ 📄types.cpython-312.pyc
│  │     │  │  │  ├─ 📄typing.cpython-312.pyc
│  │     │  │  │  ├─ 📄utils.cpython-312.pyc
│  │     │  │  │  ├─ 📄v1.cpython-312.pyc
│  │     │  │  │  ├─ 📄validators.cpython-312.pyc
│  │     │  │  │  ├─ 📄version.cpython-312.pyc
│  │     │  │  │  ├─ 📄_hypothesis_plugin.cpython-312.pyc
│  │     │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  ├─ 📄annotated_types.py
│  │     │  │  ├─ 📄class_validators.py
│  │     │  │  ├─ 📄color.py
│  │     │  │  ├─ 📄config.py
│  │     │  │  ├─ 📄dataclasses.py
│  │     │  │  ├─ 📄datetime_parse.py
│  │     │  │  ├─ 📄decorator.py
│  │     │  │  ├─ 📄env_settings.py
│  │     │  │  ├─ 📄errors.py
│  │     │  │  ├─ 📄error_wrappers.py
│  │     │  │  ├─ 📄fields.py
│  │     │  │  ├─ 📄generics.py
│  │     │  │  ├─ 📄json.py
│  │     │  │  ├─ 📄main.py
│  │     │  │  ├─ 📄mypy.py
│  │     │  │  ├─ 📄networks.py
│  │     │  │  ├─ 📄parse.py
│  │     │  │  ├─ 📄py.typed
│  │     │  │  ├─ 📄schema.py
│  │     │  │  ├─ 📄tools.py
│  │     │  │  ├─ 📄types.py
│  │     │  │  ├─ 📄typing.py
│  │     │  │  ├─ 📄utils.py
│  │     │  │  ├─ 📄v1.py
│  │     │  │  ├─ 📄validators.py
│  │     │  │  ├─ 📄version.py
│  │     │  │  ├─ 📄_hypothesis_plugin.py
│  │     │  │  └─ 📄__init__.py
│  │     │  ├─ 📁_internal
│  │     │  │  ├─ 📁__pycache__
│  │     │  │  │  ├─ 📄_config.cpython-312.pyc
│  │     │  │  │  ├─ 📄_core_metadata.cpython-312.pyc
│  │     │  │  │  ├─ 📄_core_utils.cpython-312.pyc
│  │     │  │  │  ├─ 📄_dataclasses.cpython-312.pyc
│  │     │  │  │  ├─ 📄_decorators.cpython-312.pyc
│  │     │  │  │  ├─ 📄_decorators_v1.cpython-312.pyc
│  │     │  │  │  ├─ 📄_discriminated_union.cpython-312.pyc
│  │     │  │  │  ├─ 📄_docs_extraction.cpython-312.pyc
│  │     │  │  │  ├─ 📄_fields.cpython-312.pyc
│  │     │  │  │  ├─ 📄_forward_ref.cpython-312.pyc
│  │     │  │  │  ├─ 📄_generate_schema.cpython-312.pyc
│  │     │  │  │  ├─ 📄_generics.cpython-312.pyc
│  │     │  │  │  ├─ 📄_git.cpython-312.pyc
│  │     │  │  │  ├─ 📄_internal_dataclass.cpython-312.pyc
│  │     │  │  │  ├─ 📄_known_annotated_metadata.cpython-312.pyc
│  │     │  │  │  ├─ 📄_mock_val_ser.cpython-312.pyc
│  │     │  │  │  ├─ 📄_model_construction.cpython-312.pyc
│  │     │  │  │  ├─ 📄_repr.cpython-312.pyc
│  │     │  │  │  ├─ 📄_schema_generation_shared.cpython-312.pyc
│  │     │  │  │  ├─ 📄_signature.cpython-312.pyc
│  │     │  │  │  ├─ 📄_std_types_schema.cpython-312.pyc
│  │     │  │  │  ├─ 📄_typing_extra.cpython-312.pyc
│  │     │  │  │  ├─ 📄_utils.cpython-312.pyc
│  │     │  │  │  ├─ 📄_validate_call.cpython-312.pyc
│  │     │  │  │  ├─ 📄_validators.cpython-312.pyc
│  │     │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  ├─ 📄_config.py
│  │     │  │  ├─ 📄_core_metadata.py
│  │     │  │  ├─ 📄_core_utils.py
│  │     │  │  ├─ 📄_dataclasses.py
│  │     │  │  ├─ 📄_decorators.py
│  │     │  │  ├─ 📄_decorators_v1.py
│  │     │  │  ├─ 📄_discriminated_union.py
│  │     │  │  ├─ 📄_docs_extraction.py
│  │     │  │  ├─ 📄_fields.py
│  │     │  │  ├─ 📄_forward_ref.py
│  │     │  │  ├─ 📄_generate_schema.py
│  │     │  │  ├─ 📄_generics.py
│  │     │  │  ├─ 📄_git.py
│  │     │  │  ├─ 📄_internal_dataclass.py
│  │     │  │  ├─ 📄_known_annotated_metadata.py
│  │     │  │  ├─ 📄_mock_val_ser.py
│  │     │  │  ├─ 📄_model_construction.py
│  │     │  │  ├─ 📄_repr.py
│  │     │  │  ├─ 📄_schema_generation_shared.py
│  │     │  │  ├─ 📄_signature.py
│  │     │  │  ├─ 📄_std_types_schema.py
│  │     │  │  ├─ 📄_typing_extra.py
│  │     │  │  ├─ 📄_utils.py
│  │     │  │  ├─ 📄_validate_call.py
│  │     │  │  ├─ 📄_validators.py
│  │     │  │  └─ 📄__init__.py
│  │     │  ├─ 📁__pycache__
│  │     │  │  ├─ 📄aliases.cpython-312.pyc
│  │     │  │  ├─ 📄alias_generators.cpython-312.pyc
│  │     │  │  ├─ 📄annotated_handlers.cpython-312.pyc
│  │     │  │  ├─ 📄class_validators.cpython-312.pyc
│  │     │  │  ├─ 📄color.cpython-312.pyc
│  │     │  │  ├─ 📄config.cpython-312.pyc
│  │     │  │  ├─ 📄dataclasses.cpython-312.pyc
│  │     │  │  ├─ 📄datetime_parse.cpython-312.pyc
│  │     │  │  ├─ 📄decorator.cpython-312.pyc
│  │     │  │  ├─ 📄env_settings.cpython-312.pyc
│  │     │  │  ├─ 📄errors.cpython-312.pyc
│  │     │  │  ├─ 📄error_wrappers.cpython-312.pyc
│  │     │  │  ├─ 📄fields.cpython-312.pyc
│  │     │  │  ├─ 📄functional_serializers.cpython-312.pyc
│  │     │  │  ├─ 📄functional_validators.cpython-312.pyc
│  │     │  │  ├─ 📄generics.cpython-312.pyc
│  │     │  │  ├─ 📄json.cpython-312.pyc
│  │     │  │  ├─ 📄json_schema.cpython-312.pyc
│  │     │  │  ├─ 📄main.cpython-312.pyc
│  │     │  │  ├─ 📄mypy.cpython-312.pyc
│  │     │  │  ├─ 📄networks.cpython-312.pyc
│  │     │  │  ├─ 📄parse.cpython-312.pyc
│  │     │  │  ├─ 📄root_model.cpython-312.pyc
│  │     │  │  ├─ 📄schema.cpython-312.pyc
│  │     │  │  ├─ 📄tools.cpython-312.pyc
│  │     │  │  ├─ 📄types.cpython-312.pyc
│  │     │  │  ├─ 📄type_adapter.cpython-312.pyc
│  │     │  │  ├─ 📄typing.cpython-312.pyc
│  │     │  │  ├─ 📄utils.cpython-312.pyc
│  │     │  │  ├─ 📄validate_call_decorator.cpython-312.pyc
│  │     │  │  ├─ 📄validators.cpython-312.pyc
│  │     │  │  ├─ 📄version.cpython-312.pyc
│  │     │  │  ├─ 📄warnings.cpython-312.pyc
│  │     │  │  ├─ 📄_migration.cpython-312.pyc
│  │     │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  ├─ 📄aliases.py
│  │     │  ├─ 📄alias_generators.py
│  │     │  ├─ 📄annotated_handlers.py
│  │     │  ├─ 📄class_validators.py
│  │     │  ├─ 📄color.py
│  │     │  ├─ 📄config.py
│  │     │  ├─ 📄dataclasses.py
│  │     │  ├─ 📄datetime_parse.py
│  │     │  ├─ 📄decorator.py
│  │     │  ├─ 📄env_settings.py
│  │     │  ├─ 📄errors.py
│  │     │  ├─ 📄error_wrappers.py
│  │     │  ├─ 📄fields.py
│  │     │  ├─ 📄functional_serializers.py
│  │     │  ├─ 📄functional_validators.py
│  │     │  ├─ 📄generics.py
│  │     │  ├─ 📄json.py
│  │     │  ├─ 📄json_schema.py
│  │     │  ├─ 📄main.py
│  │     │  ├─ 📄mypy.py
│  │     │  ├─ 📄networks.py
│  │     │  ├─ 📄parse.py
│  │     │  ├─ 📄py.typed
│  │     │  ├─ 📄root_model.py
│  │     │  ├─ 📄schema.py
│  │     │  ├─ 📄tools.py
│  │     │  ├─ 📄types.py
│  │     │  ├─ 📄type_adapter.py
│  │     │  ├─ 📄typing.py
│  │     │  ├─ 📄utils.py
│  │     │  ├─ 📄validate_call_decorator.py
│  │     │  ├─ 📄validators.py
│  │     │  ├─ 📄version.py
│  │     │  ├─ 📄warnings.py
│  │     │  ├─ 📄_migration.py
│  │     │  └─ 📄__init__.py
│  │     ├─ 📁pydantic-2.7.1.dist-info
│  │     │  ├─ 📁licenses
│  │     │  │  └─ 📄LICENSE
│  │     │  ├─ 📄INSTALLER
│  │     │  ├─ 📄METADATA
│  │     │  ├─ 📄RECORD
│  │     │  └─ 📄WHEEL
│  │     ├─ 📁pydantic_core
│  │     │  ├─ 📁__pycache__
│  │     │  │  ├─ 📄core_schema.cpython-312.pyc
│  │     │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  ├─ 📄core_schema.py
│  │     │  ├─ 📄py.typed
│  │     │  ├─ 📄_pydantic_core.cp312-win_amd64.pyd
│  │     │  ├─ 📄_pydantic_core.pyi
│  │     │  └─ 📄__init__.py
│  │     ├─ 📁pydantic_core-2.18.2.dist-info
│  │     │  ├─ 📁license_files
│  │     │  │  └─ 📄LICENSE
│  │     │  ├─ 📄INSTALLER
│  │     │  ├─ 📄METADATA
│  │     │  ├─ 📄RECORD
│  │     │  └─ 📄WHEEL
│  │     ├─ 📁pymysql
│  │     │  ├─ 📁constants
│  │     │  │  ├─ 📁__pycache__
│  │     │  │  │  ├─ 📄CLIENT.cpython-312.pyc
│  │     │  │  │  ├─ 📄COMMAND.cpython-312.pyc
│  │     │  │  │  ├─ 📄CR.cpython-312.pyc
│  │     │  │  │  ├─ 📄ER.cpython-312.pyc
│  │     │  │  │  ├─ 📄FIELD_TYPE.cpython-312.pyc
│  │     │  │  │  ├─ 📄FLAG.cpython-312.pyc
│  │     │  │  │  ├─ 📄SERVER_STATUS.cpython-312.pyc
│  │     │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  ├─ 📄CLIENT.py
│  │     │  │  ├─ 📄COMMAND.py
│  │     │  │  ├─ 📄CR.py
│  │     │  │  ├─ 📄ER.py
│  │     │  │  ├─ 📄FIELD_TYPE.py
│  │     │  │  ├─ 📄FLAG.py
│  │     │  │  ├─ 📄SERVER_STATUS.py
│  │     │  │  └─ 📄__init__.py
│  │     │  ├─ 📁__pycache__
│  │     │  │  ├─ 📄charset.cpython-312.pyc
│  │     │  │  ├─ 📄connections.cpython-312.pyc
│  │     │  │  ├─ 📄converters.cpython-312.pyc
│  │     │  │  ├─ 📄cursors.cpython-312.pyc
│  │     │  │  ├─ 📄err.cpython-312.pyc
│  │     │  │  ├─ 📄optionfile.cpython-312.pyc
│  │     │  │  ├─ 📄protocol.cpython-312.pyc
│  │     │  │  ├─ 📄times.cpython-312.pyc
│  │     │  │  ├─ 📄_auth.cpython-312.pyc
│  │     │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  ├─ 📄charset.py
│  │     │  ├─ 📄connections.py
│  │     │  ├─ 📄converters.py
│  │     │  ├─ 📄cursors.py
│  │     │  ├─ 📄err.py
│  │     │  ├─ 📄optionfile.py
│  │     │  ├─ 📄protocol.py
│  │     │  ├─ 📄times.py
│  │     │  ├─ 📄_auth.py
│  │     │  └─ 📄__init__.py
│  │     ├─ 📁PyMySQL-1.1.0.dist-info
│  │     │  ├─ 📄INSTALLER
│  │     │  ├─ 📄LICENSE
│  │     │  ├─ 📄METADATA
│  │     │  ├─ 📄RECORD
│  │     │  ├─ 📄REQUESTED
│  │     │  ├─ 📄top_level.txt
│  │     │  └─ 📄WHEEL
│  │     ├─ 📁python_decouple-3.8.dist-info
│  │     │  ├─ 📄INSTALLER
│  │     │  ├─ 📄LICENSE
│  │     │  ├─ 📄METADATA
│  │     │  ├─ 📄RECORD
│  │     │  ├─ 📄REQUESTED
│  │     │  ├─ 📄top_level.txt
│  │     │  └─ 📄WHEEL
│  │     ├─ 📁python_dotenv-1.0.1.dist-info
│  │     │  ├─ 📄entry_points.txt
│  │     │  ├─ 📄INSTALLER
│  │     │  ├─ 📄LICENSE
│  │     │  ├─ 📄METADATA
│  │     │  ├─ 📄RECORD
│  │     │  ├─ 📄top_level.txt
│  │     │  └─ 📄WHEEL
│  │     ├─ 📁setuptools
│  │     │  ├─ 📁command
│  │     │  │  ├─ 📁__pycache__
│  │     │  │  │  ├─ 📄alias.cpython-312.pyc
│  │     │  │  │  ├─ 📄bdist_egg.cpython-312.pyc
│  │     │  │  │  ├─ 📄bdist_rpm.cpython-312.pyc
│  │     │  │  │  ├─ 📄build.cpython-312.pyc
│  │     │  │  │  ├─ 📄build_clib.cpython-312.pyc
│  │     │  │  │  ├─ 📄build_ext.cpython-312.pyc
│  │     │  │  │  ├─ 📄build_py.cpython-312.pyc
│  │     │  │  │  ├─ 📄develop.cpython-312.pyc
│  │     │  │  │  ├─ 📄dist_info.cpython-312.pyc
│  │     │  │  │  ├─ 📄easy_install.cpython-312.pyc
│  │     │  │  │  ├─ 📄editable_wheel.cpython-312.pyc
│  │     │  │  │  ├─ 📄egg_info.cpython-312.pyc
│  │     │  │  │  ├─ 📄install.cpython-312.pyc
│  │     │  │  │  ├─ 📄install_egg_info.cpython-312.pyc
│  │     │  │  │  ├─ 📄install_lib.cpython-312.pyc
│  │     │  │  │  ├─ 📄install_scripts.cpython-312.pyc
│  │     │  │  │  ├─ 📄register.cpython-312.pyc
│  │     │  │  │  ├─ 📄rotate.cpython-312.pyc
│  │     │  │  │  ├─ 📄saveopts.cpython-312.pyc
│  │     │  │  │  ├─ 📄sdist.cpython-312.pyc
│  │     │  │  │  ├─ 📄setopt.cpython-312.pyc
│  │     │  │  │  ├─ 📄test.cpython-312.pyc
│  │     │  │  │  ├─ 📄upload.cpython-312.pyc
│  │     │  │  │  ├─ 📄upload_docs.cpython-312.pyc
│  │     │  │  │  ├─ 📄_requirestxt.cpython-312.pyc
│  │     │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  ├─ 📄alias.py
│  │     │  │  ├─ 📄bdist_egg.py
│  │     │  │  ├─ 📄bdist_rpm.py
│  │     │  │  ├─ 📄build.py
│  │     │  │  ├─ 📄build_clib.py
│  │     │  │  ├─ 📄build_ext.py
│  │     │  │  ├─ 📄build_py.py
│  │     │  │  ├─ 📄develop.py
│  │     │  │  ├─ 📄dist_info.py
│  │     │  │  ├─ 📄easy_install.py
│  │     │  │  ├─ 📄editable_wheel.py
│  │     │  │  ├─ 📄egg_info.py
│  │     │  │  ├─ 📄install.py
│  │     │  │  ├─ 📄install_egg_info.py
│  │     │  │  ├─ 📄install_lib.py
│  │     │  │  ├─ 📄install_scripts.py
│  │     │  │  ├─ 📄launcher manifest.xml
│  │     │  │  ├─ 📄register.py
│  │     │  │  ├─ 📄rotate.py
│  │     │  │  ├─ 📄saveopts.py
│  │     │  │  ├─ 📄sdist.py
│  │     │  │  ├─ 📄setopt.py
│  │     │  │  ├─ 📄test.py
│  │     │  │  ├─ 📄upload.py
│  │     │  │  ├─ 📄upload_docs.py
│  │     │  │  ├─ 📄_requirestxt.py
│  │     │  │  └─ 📄__init__.py
│  │     │  ├─ 📁compat
│  │     │  │  ├─ 📁__pycache__
│  │     │  │  │  ├─ 📄py310.cpython-312.pyc
│  │     │  │  │  ├─ 📄py311.cpython-312.pyc
│  │     │  │  │  ├─ 📄py39.cpython-312.pyc
│  │     │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  ├─ 📄py310.py
│  │     │  │  ├─ 📄py311.py
│  │     │  │  ├─ 📄py39.py
│  │     │  │  └─ 📄__init__.py
│  │     │  ├─ 📁config
│  │     │  │  ├─ 📁_validate_pyproject
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄error_reporting.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄extra_validations.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄fastjsonschema_exceptions.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄fastjsonschema_validations.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄formats.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄error_reporting.py
│  │     │  │  │  ├─ 📄extra_validations.py
│  │     │  │  │  ├─ 📄fastjsonschema_exceptions.py
│  │     │  │  │  ├─ 📄fastjsonschema_validations.py
│  │     │  │  │  ├─ 📄formats.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁__pycache__
│  │     │  │  │  ├─ 📄expand.cpython-312.pyc
│  │     │  │  │  ├─ 📄pyprojecttoml.cpython-312.pyc
│  │     │  │  │  ├─ 📄setupcfg.cpython-312.pyc
│  │     │  │  │  ├─ 📄_apply_pyprojecttoml.cpython-312.pyc
│  │     │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  ├─ 📄expand.py
│  │     │  │  ├─ 📄pyprojecttoml.py
│  │     │  │  ├─ 📄setupcfg.py
│  │     │  │  ├─ 📄_apply_pyprojecttoml.py
│  │     │  │  └─ 📄__init__.py
│  │     │  ├─ 📁extern
│  │     │  │  ├─ 📁__pycache__
│  │     │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  └─ 📄__init__.py
│  │     │  ├─ 📁_distutils
│  │     │  │  ├─ 📁command
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄bdist.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄bdist_dumb.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄bdist_rpm.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄build.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄build_clib.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄build_ext.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄build_py.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄build_scripts.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄check.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄clean.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄config.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄install.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄install_data.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄install_egg_info.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄install_headers.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄install_lib.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄install_scripts.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄register.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄sdist.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄upload.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_framework_compat.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄bdist.py
│  │     │  │  │  ├─ 📄bdist_dumb.py
│  │     │  │  │  ├─ 📄bdist_rpm.py
│  │     │  │  │  ├─ 📄build.py
│  │     │  │  │  ├─ 📄build_clib.py
│  │     │  │  │  ├─ 📄build_ext.py
│  │     │  │  │  ├─ 📄build_py.py
│  │     │  │  │  ├─ 📄build_scripts.py
│  │     │  │  │  ├─ 📄check.py
│  │     │  │  │  ├─ 📄clean.py
│  │     │  │  │  ├─ 📄config.py
│  │     │  │  │  ├─ 📄install.py
│  │     │  │  │  ├─ 📄install_data.py
│  │     │  │  │  ├─ 📄install_egg_info.py
│  │     │  │  │  ├─ 📄install_headers.py
│  │     │  │  │  ├─ 📄install_lib.py
│  │     │  │  │  ├─ 📄install_scripts.py
│  │     │  │  │  ├─ 📄register.py
│  │     │  │  │  ├─ 📄sdist.py
│  │     │  │  │  ├─ 📄upload.py
│  │     │  │  │  ├─ 📄_framework_compat.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁compat
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄py38.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄py38.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁__pycache__
│  │     │  │  │  ├─ 📄archive_util.cpython-312.pyc
│  │     │  │  │  ├─ 📄bcppcompiler.cpython-312.pyc
│  │     │  │  │  ├─ 📄ccompiler.cpython-312.pyc
│  │     │  │  │  ├─ 📄cmd.cpython-312.pyc
│  │     │  │  │  ├─ 📄config.cpython-312.pyc
│  │     │  │  │  ├─ 📄core.cpython-312.pyc
│  │     │  │  │  ├─ 📄cygwinccompiler.cpython-312.pyc
│  │     │  │  │  ├─ 📄debug.cpython-312.pyc
│  │     │  │  │  ├─ 📄dep_util.cpython-312.pyc
│  │     │  │  │  ├─ 📄dir_util.cpython-312.pyc
│  │     │  │  │  ├─ 📄dist.cpython-312.pyc
│  │     │  │  │  ├─ 📄errors.cpython-312.pyc
│  │     │  │  │  ├─ 📄extension.cpython-312.pyc
│  │     │  │  │  ├─ 📄fancy_getopt.cpython-312.pyc
│  │     │  │  │  ├─ 📄filelist.cpython-312.pyc
│  │     │  │  │  ├─ 📄file_util.cpython-312.pyc
│  │     │  │  │  ├─ 📄log.cpython-312.pyc
│  │     │  │  │  ├─ 📄msvc9compiler.cpython-312.pyc
│  │     │  │  │  ├─ 📄msvccompiler.cpython-312.pyc
│  │     │  │  │  ├─ 📄py38compat.cpython-312.pyc
│  │     │  │  │  ├─ 📄py39compat.cpython-312.pyc
│  │     │  │  │  ├─ 📄spawn.cpython-312.pyc
│  │     │  │  │  ├─ 📄sysconfig.cpython-312.pyc
│  │     │  │  │  ├─ 📄text_file.cpython-312.pyc
│  │     │  │  │  ├─ 📄unixccompiler.cpython-312.pyc
│  │     │  │  │  ├─ 📄util.cpython-312.pyc
│  │     │  │  │  ├─ 📄version.cpython-312.pyc
│  │     │  │  │  ├─ 📄versionpredicate.cpython-312.pyc
│  │     │  │  │  ├─ 📄zosccompiler.cpython-312.pyc
│  │     │  │  │  ├─ 📄_collections.cpython-312.pyc
│  │     │  │  │  ├─ 📄_functools.cpython-312.pyc
│  │     │  │  │  ├─ 📄_itertools.cpython-312.pyc
│  │     │  │  │  ├─ 📄_log.cpython-312.pyc
│  │     │  │  │  ├─ 📄_macos_compat.cpython-312.pyc
│  │     │  │  │  ├─ 📄_modified.cpython-312.pyc
│  │     │  │  │  ├─ 📄_msvccompiler.cpython-312.pyc
│  │     │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  ├─ 📄archive_util.py
│  │     │  │  ├─ 📄bcppcompiler.py
│  │     │  │  ├─ 📄ccompiler.py
│  │     │  │  ├─ 📄cmd.py
│  │     │  │  ├─ 📄config.py
│  │     │  │  ├─ 📄core.py
│  │     │  │  ├─ 📄cygwinccompiler.py
│  │     │  │  ├─ 📄debug.py
│  │     │  │  ├─ 📄dep_util.py
│  │     │  │  ├─ 📄dir_util.py
│  │     │  │  ├─ 📄dist.py
│  │     │  │  ├─ 📄errors.py
│  │     │  │  ├─ 📄extension.py
│  │     │  │  ├─ 📄fancy_getopt.py
│  │     │  │  ├─ 📄filelist.py
│  │     │  │  ├─ 📄file_util.py
│  │     │  │  ├─ 📄log.py
│  │     │  │  ├─ 📄msvc9compiler.py
│  │     │  │  ├─ 📄msvccompiler.py
│  │     │  │  ├─ 📄py38compat.py
│  │     │  │  ├─ 📄py39compat.py
│  │     │  │  ├─ 📄spawn.py
│  │     │  │  ├─ 📄sysconfig.py
│  │     │  │  ├─ 📄text_file.py
│  │     │  │  ├─ 📄unixccompiler.py
│  │     │  │  ├─ 📄util.py
│  │     │  │  ├─ 📄version.py
│  │     │  │  ├─ 📄versionpredicate.py
│  │     │  │  ├─ 📄zosccompiler.py
│  │     │  │  ├─ 📄_collections.py
│  │     │  │  ├─ 📄_functools.py
│  │     │  │  ├─ 📄_itertools.py
│  │     │  │  ├─ 📄_log.py
│  │     │  │  ├─ 📄_macos_compat.py
│  │     │  │  ├─ 📄_modified.py
│  │     │  │  ├─ 📄_msvccompiler.py
│  │     │  │  └─ 📄__init__.py
│  │     │  ├─ 📁_vendor
│  │     │  │  ├─ 📁backports
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄tarfile.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄tarfile.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁importlib_metadata
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄_adapters.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_collections.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_compat.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_functools.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_itertools.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_meta.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_py39compat.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_text.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄py.typed
│  │     │  │  │  ├─ 📄_adapters.py
│  │     │  │  │  ├─ 📄_collections.py
│  │     │  │  │  ├─ 📄_compat.py
│  │     │  │  │  ├─ 📄_functools.py
│  │     │  │  │  ├─ 📄_itertools.py
│  │     │  │  │  ├─ 📄_meta.py
│  │     │  │  │  ├─ 📄_py39compat.py
│  │     │  │  │  ├─ 📄_text.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁importlib_resources
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄abc.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄readers.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄simple.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_adapters.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_common.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_compat.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_itertools.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_legacy.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄abc.py
│  │     │  │  │  ├─ 📄py.typed
│  │     │  │  │  ├─ 📄readers.py
│  │     │  │  │  ├─ 📄simple.py
│  │     │  │  │  ├─ 📄_adapters.py
│  │     │  │  │  ├─ 📄_common.py
│  │     │  │  │  ├─ 📄_compat.py
│  │     │  │  │  ├─ 📄_itertools.py
│  │     │  │  │  ├─ 📄_legacy.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁jaraco
│  │     │  │  │  ├─ 📁functools
│  │     │  │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄py.typed
│  │     │  │  │  │  ├─ 📄__init__.py
│  │     │  │  │  │  └─ 📄__init__.pyi
│  │     │  │  │  ├─ 📁text
│  │     │  │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.py
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄context.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄context.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁more_itertools
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄more.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄recipes.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄more.py
│  │     │  │  │  ├─ 📄more.pyi
│  │     │  │  │  ├─ 📄py.typed
│  │     │  │  │  ├─ 📄recipes.py
│  │     │  │  │  ├─ 📄recipes.pyi
│  │     │  │  │  ├─ 📄__init__.py
│  │     │  │  │  └─ 📄__init__.pyi
│  │     │  │  ├─ 📁packaging
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄markers.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄metadata.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄requirements.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄specifiers.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄tags.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄utils.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄version.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_elffile.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_manylinux.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_musllinux.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_parser.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_structures.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_tokenizer.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄markers.py
│  │     │  │  │  ├─ 📄metadata.py
│  │     │  │  │  ├─ 📄py.typed
│  │     │  │  │  ├─ 📄requirements.py
│  │     │  │  │  ├─ 📄specifiers.py
│  │     │  │  │  ├─ 📄tags.py
│  │     │  │  │  ├─ 📄utils.py
│  │     │  │  │  ├─ 📄version.py
│  │     │  │  │  ├─ 📄_elffile.py
│  │     │  │  │  ├─ 📄_manylinux.py
│  │     │  │  │  ├─ 📄_musllinux.py
│  │     │  │  │  ├─ 📄_parser.py
│  │     │  │  │  ├─ 📄_structures.py
│  │     │  │  │  ├─ 📄_tokenizer.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁tomli
│  │     │  │  │  ├─ 📁__pycache__
│  │     │  │  │  │  ├─ 📄_parser.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_re.cpython-312.pyc
│  │     │  │  │  │  ├─ 📄_types.cpython-312.pyc
│  │     │  │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  │  ├─ 📄py.typed
│  │     │  │  │  ├─ 📄_parser.py
│  │     │  │  │  ├─ 📄_re.py
│  │     │  │  │  ├─ 📄_types.py
│  │     │  │  │  └─ 📄__init__.py
│  │     │  │  ├─ 📁__pycache__
│  │     │  │  │  ├─ 📄ordered_set.cpython-312.pyc
│  │     │  │  │  ├─ 📄typing_extensions.cpython-312.pyc
│  │     │  │  │  ├─ 📄zipp.cpython-312.pyc
│  │     │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  ├─ 📄ordered_set.py
│  │     │  │  ├─ 📄typing_extensions.py
│  │     │  │  ├─ 📄zipp.py
│  │     │  │  └─ 📄__init__.py
│  │     │  ├─ 📁__pycache__
│  │     │  │  ├─ 📄archive_util.cpython-312.pyc
│  │     │  │  ├─ 📄build_meta.cpython-312.pyc
│  │     │  │  ├─ 📄depends.cpython-312.pyc
│  │     │  │  ├─ 📄dep_util.cpython-312.pyc
│  │     │  │  ├─ 📄discovery.cpython-312.pyc
│  │     │  │  ├─ 📄dist.cpython-312.pyc
│  │     │  │  ├─ 📄errors.cpython-312.pyc
│  │     │  │  ├─ 📄extension.cpython-312.pyc
│  │     │  │  ├─ 📄glob.cpython-312.pyc
│  │     │  │  ├─ 📄installer.cpython-312.pyc
│  │     │  │  ├─ 📄launch.cpython-312.pyc
│  │     │  │  ├─ 📄logging.cpython-312.pyc
│  │     │  │  ├─ 📄modified.cpython-312.pyc
│  │     │  │  ├─ 📄monkey.cpython-312.pyc
│  │     │  │  ├─ 📄msvc.cpython-312.pyc
│  │     │  │  ├─ 📄namespaces.cpython-312.pyc
│  │     │  │  ├─ 📄package_index.cpython-312.pyc
│  │     │  │  ├─ 📄sandbox.cpython-312.pyc
│  │     │  │  ├─ 📄unicode_utils.cpython-312.pyc
│  │     │  │  ├─ 📄version.cpython-312.pyc
│  │     │  │  ├─ 📄warnings.cpython-312.pyc
│  │     │  │  ├─ 📄wheel.cpython-312.pyc
│  │     │  │  ├─ 📄windows_support.cpython-312.pyc
│  │     │  │  ├─ 📄_core_metadata.cpython-312.pyc
│  │     │  │  ├─ 📄_entry_points.cpython-312.pyc
│  │     │  │  ├─ 📄_imp.cpython-312.pyc
│  │     │  │  ├─ 📄_importlib.cpython-312.pyc
│  │     │  │  ├─ 📄_itertools.cpython-312.pyc
│  │     │  │  ├─ 📄_normalization.cpython-312.pyc
│  │     │  │  ├─ 📄_path.cpython-312.pyc
│  │     │  │  ├─ 📄_reqs.cpython-312.pyc
│  │     │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  ├─ 📄archive_util.py
│  │     │  ├─ 📄build_meta.py
│  │     │  ├─ 📄cli-32.exe
│  │     │  ├─ 📄cli-64.exe
│  │     │  ├─ 📄cli-arm64.exe
│  │     │  ├─ 📄cli.exe
│  │     │  ├─ 📄depends.py
│  │     │  ├─ 📄dep_util.py
│  │     │  ├─ 📄discovery.py
│  │     │  ├─ 📄dist.py
│  │     │  ├─ 📄errors.py
│  │     │  ├─ 📄extension.py
│  │     │  ├─ 📄glob.py
│  │     │  ├─ 📄gui-32.exe
│  │     │  ├─ 📄gui-64.exe
│  │     │  ├─ 📄gui-arm64.exe
│  │     │  ├─ 📄gui.exe
│  │     │  ├─ 📄installer.py
│  │     │  ├─ 📄launch.py
│  │     │  ├─ 📄logging.py
│  │     │  ├─ 📄modified.py
│  │     │  ├─ 📄monkey.py
│  │     │  ├─ 📄msvc.py
│  │     │  ├─ 📄namespaces.py
│  │     │  ├─ 📄package_index.py
│  │     │  ├─ 📄sandbox.py
│  │     │  ├─ 📄script (dev).tmpl
│  │     │  ├─ 📄script.tmpl
│  │     │  ├─ 📄unicode_utils.py
│  │     │  ├─ 📄version.py
│  │     │  ├─ 📄warnings.py
│  │     │  ├─ 📄wheel.py
│  │     │  ├─ 📄windows_support.py
│  │     │  ├─ 📄_core_metadata.py
│  │     │  ├─ 📄_entry_points.py
│  │     │  ├─ 📄_imp.py
│  │     │  ├─ 📄_importlib.py
│  │     │  ├─ 📄_itertools.py
│  │     │  ├─ 📄_normalization.py
│  │     │  ├─ 📄_path.py
│  │     │  ├─ 📄_reqs.py
│  │     │  └─ 📄__init__.py
│  │     ├─ 📁setuptools-69.5.1.dist-info
│  │     │  ├─ 📄entry_points.txt
│  │     │  ├─ 📄INSTALLER
│  │     │  ├─ 📄LICENSE
│  │     │  ├─ 📄METADATA
│  │     │  ├─ 📄RECORD
│  │     │  ├─ 📄top_level.txt
│  │     │  └─ 📄WHEEL
│  │     ├─ 📁sniffio
│  │     │  ├─ 📁_tests
│  │     │  │  ├─ 📁__pycache__
│  │     │  │  │  ├─ 📄test_sniffio.cpython-312.pyc
│  │     │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  ├─ 📄test_sniffio.py
│  │     │  │  └─ 📄__init__.py
│  │     │  ├─ 📁__pycache__
│  │     │  │  ├─ 📄_impl.cpython-312.pyc
│  │     │  │  ├─ 📄_version.cpython-312.pyc
│  │     │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  ├─ 📄py.typed
│  │     │  ├─ 📄_impl.py
│  │     │  ├─ 📄_version.py
│  │     │  └─ 📄__init__.py
│  │     ├─ 📁sniffio-1.3.1.dist-info
│  │     │  ├─ 📄INSTALLER
│  │     │  ├─ 📄LICENSE
│  │     │  ├─ 📄LICENSE.APACHE2
│  │     │  ├─ 📄LICENSE.MIT
│  │     │  ├─ 📄METADATA
│  │     │  ├─ 📄RECORD
│  │     │  ├─ 📄top_level.txt
│  │     │  └─ 📄WHEEL
│  │     ├─ 📁tomlkit
│  │     │  ├─ 📁__pycache__
│  │     │  │  ├─ 📄api.cpython-312.pyc
│  │     │  │  ├─ 📄container.cpython-312.pyc
│  │     │  │  ├─ 📄exceptions.cpython-312.pyc
│  │     │  │  ├─ 📄items.cpython-312.pyc
│  │     │  │  ├─ 📄parser.cpython-312.pyc
│  │     │  │  ├─ 📄source.cpython-312.pyc
│  │     │  │  ├─ 📄toml_char.cpython-312.pyc
│  │     │  │  ├─ 📄toml_document.cpython-312.pyc
│  │     │  │  ├─ 📄toml_file.cpython-312.pyc
│  │     │  │  ├─ 📄_compat.cpython-312.pyc
│  │     │  │  ├─ 📄_types.cpython-312.pyc
│  │     │  │  ├─ 📄_utils.cpython-312.pyc
│  │     │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  ├─ 📄api.py
│  │     │  ├─ 📄container.py
│  │     │  ├─ 📄exceptions.py
│  │     │  ├─ 📄items.py
│  │     │  ├─ 📄parser.py
│  │     │  ├─ 📄py.typed
│  │     │  ├─ 📄source.py
│  │     │  ├─ 📄toml_char.py
│  │     │  ├─ 📄toml_document.py
│  │     │  ├─ 📄toml_file.py
│  │     │  ├─ 📄_compat.py
│  │     │  ├─ 📄_types.py
│  │     │  ├─ 📄_utils.py
│  │     │  └─ 📄__init__.py
│  │     ├─ 📁tomlkit-0.12.5.dist-info
│  │     │  ├─ 📄INSTALLER
│  │     │  ├─ 📄LICENSE
│  │     │  ├─ 📄METADATA
│  │     │  ├─ 📄RECORD
│  │     │  └─ 📄WHEEL
│  │     ├─ 📁typing_extensions-4.11.0.dist-info
│  │     │  ├─ 📄INSTALLER
│  │     │  ├─ 📄LICENSE
│  │     │  ├─ 📄METADATA
│  │     │  ├─ 📄RECORD
│  │     │  └─ 📄WHEEL
│  │     ├─ 📁werkzeug
│  │     │  ├─ 📁datastructures
│  │     │  │  ├─ 📁__pycache__
│  │     │  │  │  ├─ 📄accept.cpython-312.pyc
│  │     │  │  │  ├─ 📄auth.cpython-312.pyc
│  │     │  │  │  ├─ 📄cache_control.cpython-312.pyc
│  │     │  │  │  ├─ 📄csp.cpython-312.pyc
│  │     │  │  │  ├─ 📄etag.cpython-312.pyc
│  │     │  │  │  ├─ 📄file_storage.cpython-312.pyc
│  │     │  │  │  ├─ 📄headers.cpython-312.pyc
│  │     │  │  │  ├─ 📄mixins.cpython-312.pyc
│  │     │  │  │  ├─ 📄range.cpython-312.pyc
│  │     │  │  │  ├─ 📄structures.cpython-312.pyc
│  │     │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  ├─ 📄accept.py
│  │     │  │  ├─ 📄accept.pyi
│  │     │  │  ├─ 📄auth.py
│  │     │  │  ├─ 📄cache_control.py
│  │     │  │  ├─ 📄cache_control.pyi
│  │     │  │  ├─ 📄csp.py
│  │     │  │  ├─ 📄csp.pyi
│  │     │  │  ├─ 📄etag.py
│  │     │  │  ├─ 📄etag.pyi
│  │     │  │  ├─ 📄file_storage.py
│  │     │  │  ├─ 📄file_storage.pyi
│  │     │  │  ├─ 📄headers.py
│  │     │  │  ├─ 📄headers.pyi
│  │     │  │  ├─ 📄mixins.py
│  │     │  │  ├─ 📄mixins.pyi
│  │     │  │  ├─ 📄range.py
│  │     │  │  ├─ 📄range.pyi
│  │     │  │  ├─ 📄structures.py
│  │     │  │  ├─ 📄structures.pyi
│  │     │  │  └─ 📄__init__.py
│  │     │  ├─ 📁debug
│  │     │  │  ├─ 📁shared
│  │     │  │  │  ├─ 📄console.png
│  │     │  │  │  ├─ 📄debugger.js
│  │     │  │  │  ├─ 📄ICON_LICENSE.md
│  │     │  │  │  ├─ 📄less.png
│  │     │  │  │  ├─ 📄more.png
│  │     │  │  │  └─ 📄style.css
│  │     │  │  ├─ 📁__pycache__
│  │     │  │  │  ├─ 📄console.cpython-312.pyc
│  │     │  │  │  ├─ 📄repr.cpython-312.pyc
│  │     │  │  │  ├─ 📄tbtools.cpython-312.pyc
│  │     │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  ├─ 📄console.py
│  │     │  │  ├─ 📄repr.py
│  │     │  │  ├─ 📄tbtools.py
│  │     │  │  └─ 📄__init__.py
│  │     │  ├─ 📁middleware
│  │     │  │  ├─ 📁__pycache__
│  │     │  │  │  ├─ 📄dispatcher.cpython-312.pyc
│  │     │  │  │  ├─ 📄http_proxy.cpython-312.pyc
│  │     │  │  │  ├─ 📄lint.cpython-312.pyc
│  │     │  │  │  ├─ 📄profiler.cpython-312.pyc
│  │     │  │  │  ├─ 📄proxy_fix.cpython-312.pyc
│  │     │  │  │  ├─ 📄shared_data.cpython-312.pyc
│  │     │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  ├─ 📄dispatcher.py
│  │     │  │  ├─ 📄http_proxy.py
│  │     │  │  ├─ 📄lint.py
│  │     │  │  ├─ 📄profiler.py
│  │     │  │  ├─ 📄proxy_fix.py
│  │     │  │  ├─ 📄shared_data.py
│  │     │  │  └─ 📄__init__.py
│  │     │  ├─ 📁routing
│  │     │  │  ├─ 📁__pycache__
│  │     │  │  │  ├─ 📄converters.cpython-312.pyc
│  │     │  │  │  ├─ 📄exceptions.cpython-312.pyc
│  │     │  │  │  ├─ 📄map.cpython-312.pyc
│  │     │  │  │  ├─ 📄matcher.cpython-312.pyc
│  │     │  │  │  ├─ 📄rules.cpython-312.pyc
│  │     │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  ├─ 📄converters.py
│  │     │  │  ├─ 📄exceptions.py
│  │     │  │  ├─ 📄map.py
│  │     │  │  ├─ 📄matcher.py
│  │     │  │  ├─ 📄rules.py
│  │     │  │  └─ 📄__init__.py
│  │     │  ├─ 📁sansio
│  │     │  │  ├─ 📁__pycache__
│  │     │  │  │  ├─ 📄http.cpython-312.pyc
│  │     │  │  │  ├─ 📄multipart.cpython-312.pyc
│  │     │  │  │  ├─ 📄request.cpython-312.pyc
│  │     │  │  │  ├─ 📄response.cpython-312.pyc
│  │     │  │  │  ├─ 📄utils.cpython-312.pyc
│  │     │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  ├─ 📄http.py
│  │     │  │  ├─ 📄multipart.py
│  │     │  │  ├─ 📄request.py
│  │     │  │  ├─ 📄response.py
│  │     │  │  ├─ 📄utils.py
│  │     │  │  └─ 📄__init__.py
│  │     │  ├─ 📁wrappers
│  │     │  │  ├─ 📁__pycache__
│  │     │  │  │  ├─ 📄request.cpython-312.pyc
│  │     │  │  │  ├─ 📄response.cpython-312.pyc
│  │     │  │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  │  ├─ 📄request.py
│  │     │  │  ├─ 📄response.py
│  │     │  │  └─ 📄__init__.py
│  │     │  ├─ 📁__pycache__
│  │     │  │  ├─ 📄exceptions.cpython-312.pyc
│  │     │  │  ├─ 📄formparser.cpython-312.pyc
│  │     │  │  ├─ 📄http.cpython-312.pyc
│  │     │  │  ├─ 📄local.cpython-312.pyc
│  │     │  │  ├─ 📄security.cpython-312.pyc
│  │     │  │  ├─ 📄serving.cpython-312.pyc
│  │     │  │  ├─ 📄test.cpython-312.pyc
│  │     │  │  ├─ 📄testapp.cpython-312.pyc
│  │     │  │  ├─ 📄urls.cpython-312.pyc
│  │     │  │  ├─ 📄user_agent.cpython-312.pyc
│  │     │  │  ├─ 📄utils.cpython-312.pyc
│  │     │  │  ├─ 📄wsgi.cpython-312.pyc
│  │     │  │  ├─ 📄_internal.cpython-312.pyc
│  │     │  │  ├─ 📄_reloader.cpython-312.pyc
│  │     │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  ├─ 📄exceptions.py
│  │     │  ├─ 📄formparser.py
│  │     │  ├─ 📄http.py
│  │     │  ├─ 📄local.py
│  │     │  ├─ 📄py.typed
│  │     │  ├─ 📄security.py
│  │     │  ├─ 📄serving.py
│  │     │  ├─ 📄test.py
│  │     │  ├─ 📄testapp.py
│  │     │  ├─ 📄urls.py
│  │     │  ├─ 📄user_agent.py
│  │     │  ├─ 📄utils.py
│  │     │  ├─ 📄wsgi.py
│  │     │  ├─ 📄_internal.py
│  │     │  ├─ 📄_reloader.py
│  │     │  └─ 📄__init__.py
│  │     ├─ 📁werkzeug-3.0.3.dist-info
│  │     │  ├─ 📄INSTALLER
│  │     │  ├─ 📄LICENSE.txt
│  │     │  ├─ 📄METADATA
│  │     │  ├─ 📄RECORD
│  │     │  └─ 📄WHEEL
│  │     ├─ 📁_distutils_hack
│  │     │  ├─ 📁__pycache__
│  │     │  │  ├─ 📄override.cpython-312.pyc
│  │     │  │  └─ 📄__init__.cpython-312.pyc
│  │     │  ├─ 📄override.py
│  │     │  └─ 📄__init__.py
│  │     ├─ 📁__pycache__
│  │     │  ├─ 📄decouple.cpython-312.pyc
│  │     │  ├─ 📄nodeenv.cpython-312.pyc
│  │     │  ├─ 📄typing_extensions.cpython-312.pyc
│  │     │  └─ 📄_virtualenv.cpython-312.pyc
│  │     ├─ 📄decouple.py
│  │     ├─ 📄distutils-precedence.pth
│  │     ├─ 📄nodeenv.py
│  │     ├─ 📄pip-24.0.virtualenv
│  │     ├─ 📄typing_extensions.py
│  │     ├─ 📄_virtualenv.pth
│  │     └─ 📄_virtualenv.py
│  ├─ 📁Scripts
│  │  ├─ 📄activate
│  │  ├─ 📄activate.bat
│  │  ├─ 📄activate.fish
│  │  ├─ 📄activate.nu
│  │  ├─ 📄activate.ps1
│  │  ├─ 📄activate_this.py
│  │  ├─ 📄deactivate.bat
│  │  ├─ 📄dotenv.exe
│  │  ├─ 📄flask.exe
│  │  ├─ 📄httpx.exe
│  │  ├─ 📄nodeenv.exe
│  │  ├─ 📄pip-3.12.exe
│  │  ├─ 📄pip.exe
│  │  ├─ 📄pip3.12.exe
│  │  ├─ 📄pip3.exe
│  │  ├─ 📄pydoc.bat
│  │  ├─ 📄python.exe
│  │  └─ 📄pythonw.exe
│  ├─ 📄.gitignore
│  └─ 📄pyvenv.cfg
├─ 📄.env
├─ 📄Dockerfile
├─ 📄README.md
└─ 📄requirements.txt
```