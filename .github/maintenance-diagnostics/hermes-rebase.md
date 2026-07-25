status=validation_failed
head_branch=fork-maintenance/hermes-resolve-run
head_sha=2527d090808e0393e160e475275665672826607f
original_head=e4a71418352300209e6cdc6b32bcfb61ae330972
upstream_head=199f55805876965fadea0f7a7ef29ae9128602ec
candidate_head=44659e19823466b1e61e162fa3f99d4c57014a2d
custom_count=10
merge_count=0
dropped_absorbed_commit=786c3c253e10ff51c6c8b269960e07433a9ac874
failed_step=ruff
failed_rc=2
failed_log_tail:
error: Failed to spawn: `ruff`
  Caused by: No such file or directory (os error 2)
custom_stack:
- e68ccb44e11374d461f439a8f74613d40418c395 fix(desktop): route read-aloud speak through the active chat profile
- 542fbb1a219c23f603098695898b6ea8ae05bc39 fix(gateway): harden voice and audio delivery
- 80485a0f6fba8bf6ff1e9da28c6af8ef328d8d9c fix(honcho): persist async writes with retry fallback
- 136a27c71785c3fd94feeeace53d72e58d05c7ed fix(qqbot): bound reply-context message cache
- c71aaea8587f398f34e4119dc1ea692689cf1e06 fix(dashboard): allow configured loopback proxy hosts
- 56687a5e29c6fea0fec1a0082b2e55a39d29286d fix(dashboard): bridge requested profile's .env when computing connected platforms
- 8b4dc5dd9bda1b2e0b987191b33f0938fe9cfe08 fix(tts): handle MiniMax CN and Opus output
- d30352b36b27d96fcbb7c8d3ade588660215725b fix(dashboard): scope /api/audio/speak to requested profile
- f2f246487c1af7b09737d42769323d6e5b4ebd4b feat(models): add glm-5.2 to alibaba + alibaba-coding-plan
- 44659e19823466b1e61e162fa3f99d4c57014a2d fix(models): restore qwen3.7-max to alibaba-coding-plan
git_cherry:
+ e68ccb44e11374d461f439a8f74613d40418c395
+ 542fbb1a219c23f603098695898b6ea8ae05bc39
+ 80485a0f6fba8bf6ff1e9da28c6af8ef328d8d9c
+ 136a27c71785c3fd94feeeace53d72e58d05c7ed
+ c71aaea8587f398f34e4119dc1ea692689cf1e06
+ 56687a5e29c6fea0fec1a0082b2e55a39d29286d
+ 8b4dc5dd9bda1b2e0b987191b33f0938fe9cfe08
+ d30352b36b27d96fcbb7c8d3ade588660215725b
+ f2f246487c1af7b09737d42769323d6e5b4ebd4b
+ 44659e19823466b1e61e162fa3f99d4c57014a2d
