status=success
head_branch=fork-maintenance/hermes-resolve-run
head_sha=46dee4db6e0a0db884a3132f2e66130b9d7cb553
original_head=e4a71418352300209e6cdc6b32bcfb61ae330972
upstream_head=199f55805876965fadea0f7a7ef29ae9128602ec
candidate_head=189ff34a85662650241daed7a010d61de2a9d58a
custom_count=11
merge_count=0
absorbed_production_commit=786c3c253e10ff51c6c8b269960e07433a9ac874
replacement_test_commit=test(dashboard): adapt profile-env status stubs to scoped reads
custom_stack:
- cf28db0ab8d44abf283b9a3714968fc639005a5e fix(desktop): route read-aloud speak through the active chat profile
- f2b7b0600210b7eb14a49ab3566e1ed6d7996031 fix(gateway): harden voice and audio delivery
- 3214cce097fb8e2748cf6bc9b5f4238f464a5348 fix(honcho): persist async writes with retry fallback
- db7c930e235b7b8fe27467df66268e30c01c76a0 fix(qqbot): bound reply-context message cache
- f2f8d1eb71a5c23fccefd89dbee1f95daeea9115 fix(dashboard): allow configured loopback proxy hosts
- e1e151f50de357db2c6ed961a0acf1e252fb42cb fix(dashboard): bridge requested profile's .env when computing connected platforms
- f31b2bf24ba2323251838b4fb15c4c20354b7f20 fix(tts): handle MiniMax CN and Opus output
- 60b8d1d6f54d9d18d97cada4c9f0cffd4a39f24d fix(dashboard): scope /api/audio/speak to requested profile
- d7162b10b865589c593ea9958ac4a79fa2f98a01 feat(models): add glm-5.2 to alibaba + alibaba-coding-plan
- 27e6c50d81fde9b09b12dea34ad0555a770711ba fix(models): restore qwen3.7-max to alibaba-coding-plan
- 189ff34a85662650241daed7a010d61de2a9d58a test(dashboard): adapt profile-env status stubs to scoped reads
git_cherry:
+ cf28db0ab8d44abf283b9a3714968fc639005a5e
+ f2b7b0600210b7eb14a49ab3566e1ed6d7996031
+ 3214cce097fb8e2748cf6bc9b5f4238f464a5348
+ db7c930e235b7b8fe27467df66268e30c01c76a0
+ f2f8d1eb71a5c23fccefd89dbee1f95daeea9115
+ e1e151f50de357db2c6ed961a0acf1e252fb42cb
+ f31b2bf24ba2323251838b4fb15c4c20354b7f20
+ 60b8d1d6f54d9d18d97cada4c9f0cffd4a39f24d
+ d7162b10b865589c593ea9958ac4a79fa2f98a01
+ 27e6c50d81fde9b09b12dea34ad0555a770711ba
+ 189ff34a85662650241daed7a010d61de2a9d58a
validation=ruff+targeted_pytest+desktop_typecheck+desktop_build passed
