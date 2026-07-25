status=validation_failed
head_branch=fork-maintenance/hermes-resolve-run
head_sha=bd6fff514cbeb2665160c3e0ee7430cf6445133c
original_head=e4a71418352300209e6cdc6b32bcfb61ae330972
upstream_head=199f55805876965fadea0f7a7ef29ae9128602ec
candidate_head=1262149f37b203058e8c91386d2686539e29112c
custom_count=10
merge_count=0
dropped_absorbed_commit=786c3c253e10ff51c6c8b269960e07433a9ac874
failed_step=pytest
failed_rc=1
failed_log_tail:
/usr/lib/python3.12/contextlib.py:158: in __exit__
    self.gen.throw(value)
.venv/lib/python3.12/site-packages/starlette/_utils.py:87: in collapse_excgroups
    raise exc
.venv/lib/python3.12/site-packages/starlette/middleware/base.py:193: in __call__
    response = await self.dispatch_func(request, call_next)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
hermes_cli/web_server.py:652: in _token_auth_seam
    return await token_auth_middleware(request, call_next)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
hermes_cli/dashboard_auth/token_auth.py:164: in token_auth_middleware
    return await call_next(request)
           ^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.12/site-packages/starlette/middleware/base.py:168: in call_next
    raise app_exc from app_exc.__cause__ or app_exc.__context__
.venv/lib/python3.12/site-packages/starlette/middleware/base.py:144: in coro
    await self.app(scope, receive_or_disconnect, send_no_error)
.venv/lib/python3.12/site-packages/starlette/middleware/base.py:191: in __call__
    with recv_stream, send_stream, collapse_excgroups():
/usr/lib/python3.12/contextlib.py:158: in __exit__
    self.gen.throw(value)
.venv/lib/python3.12/site-packages/starlette/_utils.py:87: in collapse_excgroups
    raise exc
.venv/lib/python3.12/site-packages/starlette/middleware/base.py:193: in __call__
    response = await self.dispatch_func(request, call_next)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
hermes_cli/web_server.py:638: in auth_middleware
    return await call_next(request)
           ^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.12/site-packages/starlette/middleware/base.py:168: in call_next
    raise app_exc from app_exc.__cause__ or app_exc.__context__
.venv/lib/python3.12/site-packages/starlette/middleware/base.py:144: in coro
    await self.app(scope, receive_or_disconnect, send_no_error)
.venv/lib/python3.12/site-packages/starlette/middleware/base.py:191: in __call__
    with recv_stream, send_stream, collapse_excgroups():
/usr/lib/python3.12/contextlib.py:158: in __exit__
    self.gen.throw(value)
.venv/lib/python3.12/site-packages/starlette/_utils.py:87: in collapse_excgroups
    raise exc
.venv/lib/python3.12/site-packages/starlette/middleware/base.py:193: in __call__
    response = await self.dispatch_func(request, call_next)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
hermes_cli/web_server.py:614: in _dashboard_auth_gate
    return await gated_auth_middleware(request, call_next)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
hermes_cli/dashboard_auth/middleware.py:333: in gated_auth_middleware
    return await call_next(request)
           ^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.12/site-packages/starlette/middleware/base.py:168: in call_next
    raise app_exc from app_exc.__cause__ or app_exc.__context__
.venv/lib/python3.12/site-packages/starlette/middleware/base.py:144: in coro
    await self.app(scope, receive_or_disconnect, send_no_error)
.venv/lib/python3.12/site-packages/starlette/middleware/base.py:191: in __call__
    with recv_stream, send_stream, collapse_excgroups():
/usr/lib/python3.12/contextlib.py:158: in __exit__
    self.gen.throw(value)
.venv/lib/python3.12/site-packages/starlette/_utils.py:87: in collapse_excgroups
    raise exc
.venv/lib/python3.12/site-packages/starlette/middleware/base.py:193: in __call__
    response = await self.dispatch_func(request, call_next)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
hermes_cli/web_server.py:599: in _plugin_api_runtime_gate
    return await call_next(request)
           ^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.12/site-packages/starlette/middleware/base.py:168: in call_next
    raise app_exc from app_exc.__cause__ or app_exc.__context__
.venv/lib/python3.12/site-packages/starlette/middleware/base.py:144: in coro
    await self.app(scope, receive_or_disconnect, send_no_error)
.venv/lib/python3.12/site-packages/starlette/middleware/base.py:191: in __call__
    with recv_stream, send_stream, collapse_excgroups():
/usr/lib/python3.12/contextlib.py:158: in __exit__
    self.gen.throw(value)
.venv/lib/python3.12/site-packages/starlette/_utils.py:87: in collapse_excgroups
    raise exc
.venv/lib/python3.12/site-packages/starlette/middleware/base.py:193: in __call__
    response = await self.dispatch_func(request, call_next)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
hermes_cli/web_server.py:532: in host_header_middleware
    return await call_next(request)
           ^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.12/site-packages/starlette/middleware/base.py:168: in call_next
    raise app_exc from app_exc.__cause__ or app_exc.__context__
.venv/lib/python3.12/site-packages/starlette/middleware/base.py:144: in coro
    await self.app(scope, receive_or_disconnect, send_no_error)
.venv/lib/python3.12/site-packages/starlette/middleware/cors.py:88: in __call__
    await self.app(scope, receive, send)
.venv/lib/python3.12/site-packages/starlette/middleware/exceptions.py:63: in __call__
    await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
.venv/lib/python3.12/site-packages/starlette/_exception_handler.py:53: in wrapped_app
    raise exc
.venv/lib/python3.12/site-packages/starlette/_exception_handler.py:42: in wrapped_app
    await app(scope, receive, sender)
.venv/lib/python3.12/site-packages/fastapi/middleware/asyncexitstack.py:18: in __call__
    await self.app(scope, receive, send)
.venv/lib/python3.12/site-packages/starlette/routing.py:660: in __call__
    await self.middleware_stack(scope, receive, send)
.venv/lib/python3.12/site-packages/starlette/routing.py:680: in app
    await route.handle(scope, receive, send)
.venv/lib/python3.12/site-packages/starlette/routing.py:276: in handle
    await self.app(scope, receive, send)
.venv/lib/python3.12/site-packages/fastapi/routing.py:119: in app
    await wrap_app_handling_exceptions(app, request)(scope, receive, send)
.venv/lib/python3.12/site-packages/starlette/_exception_handler.py:53: in wrapped_app
    raise exc
.venv/lib/python3.12/site-packages/starlette/_exception_handler.py:42: in wrapped_app
    await app(scope, receive, sender)
.venv/lib/python3.12/site-packages/fastapi/routing.py:105: in app
    response = await f(request)
               ^^^^^^^^^^^^^^^^
.venv/lib/python3.12/site-packages/fastapi/routing.py:431: in app
    raw_response = await run_endpoint_function(
.venv/lib/python3.12/site-packages/fastapi/routing.py:313: in run_endpoint_function
    return await dependant.call(**values)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

profile = 'worker_beta'

    @app.get("/api/status")
    async def get_status(profile: Optional[str] = None):
        status_scope = None
        requested_profile = (profile or "").strip()
        # Plain /api/status stays the machine-level public liveness probe. The
        # dashboard adds ?profile= when its management switcher targets another
        # profile, so its gateway badge reflects the selected profile.
        #
        # Use the config-only (contextvar) scope, NOT _profile_scope: this handler
        # awaits the remote-health probe, and _profile_scope swaps process-global
        # skills-module attributes that a concurrent request would cross-restore
        # across that await. Status only resolves get_hermes_home() at call time
        # (config/env/gateway state), which the task-local contextvar covers.
        profile_dir: Optional[Path] = None
        if requested_profile and requested_profile.lower() != "current":
            profile_dir = _resolve_profile_dir(requested_profile)
            status_scope = _config_profile_scope(requested_profile)
            status_scope.__enter__()
    
        try:
            current_ver, latest_ver = check_config_version()
            # --- Gateway liveness detection ---
            # Try local PID check first (same-host).  If that fails and a remote
            # GATEWAY_HEALTH_URL is configured, probe the gateway over HTTP so the
            # dashboard works when the gateway runs in a separate container.
            #
            # When ?profile=<name> was given, scope PID and state reads to that
            # profile's directory — gateway identity files (PID, lock, runtime
            # status) are written to the per-profile home, not the process-level
            # HERMES_HOME (see issue #69143). Plain /api/status keeps the exact
            # zero-arg call so its behavior (and cache signature) is unchanged.
            gateway_pid = (
>               get_running_pid_cached(pid_path=profile_dir / "gateway.pid")
                if profile_dir
                else get_running_pid_cached()
            )
E           TypeError: TestProfileScopedGateway.test_status_connected_platforms_bridge_profile_env.<locals>.<lambda>() got an unexpected keyword argument 'pid_path'

hermes_cli/web_server.py:3093: TypeError
=========================== short test summary info ============================
FAILED tests/hermes_cli/test_web_server_profile_unification.py::TestProfileScopedGateway::test_status_connected_platforms_bridge_profile_env - TypeError: TestProfileScopedGateway.test_status_connected_platforms_bridge_profile_env.<locals>.<lambda>() got an unexpected keyword argument 'pid_path'
1 failed, 94 passed in 9.79s
custom_stack:
- 7eddf42eeb04a130a653faee6d3e879881052a27 fix(desktop): route read-aloud speak through the active chat profile
- abdd336c2b4518e49e26878b91753b90d34bb28b fix(gateway): harden voice and audio delivery
- 406ada0ac766997a092ac2e44c6f8932253e9bef fix(honcho): persist async writes with retry fallback
- 6ff31405cc8a665fdfcb9e37f2741d2d46514225 fix(qqbot): bound reply-context message cache
- 1091015e3a30ae1bc917e60aa791756085f5c02f fix(dashboard): allow configured loopback proxy hosts
- c139a815b84c6cce292b029346131b48b7530926 fix(dashboard): bridge requested profile's .env when computing connected platforms
- 0fe5695e0d619771e1fe3f01514c32942dd1a2a0 fix(tts): handle MiniMax CN and Opus output
- de4b4ac20166ea4e96e1e74cdb759f747d0ff086 fix(dashboard): scope /api/audio/speak to requested profile
- cfee31ca86000e626b4a59361b02f21efbd68490 feat(models): add glm-5.2 to alibaba + alibaba-coding-plan
- 1262149f37b203058e8c91386d2686539e29112c fix(models): restore qwen3.7-max to alibaba-coding-plan
git_cherry:
+ 7eddf42eeb04a130a653faee6d3e879881052a27
+ abdd336c2b4518e49e26878b91753b90d34bb28b
+ 406ada0ac766997a092ac2e44c6f8932253e9bef
+ 6ff31405cc8a665fdfcb9e37f2741d2d46514225
+ 1091015e3a30ae1bc917e60aa791756085f5c02f
+ c139a815b84c6cce292b029346131b48b7530926
+ 0fe5695e0d619771e1fe3f01514c32942dd1a2a0
+ de4b4ac20166ea4e96e1e74cdb759f747d0ff086
+ cfee31ca86000e626b4a59361b02f21efbd68490
+ 1262149f37b203058e8c91386d2686539e29112c
