# Move this project to Codex Cloud
Prepared November 6, 2026. This is a new Cloud continuation, not an in-place migration of the original chat.

## 1. Put these files in a private GitHub repository (one-time desktop setup)
1. Download wet-okole-cloud-transfer.zip and unzip it. Open the wet-okole-design folder.
2. Sign in at https://github.com and choose + > New repository. Name it wet-okole-design, choose Private, select Add a README, and create it.
3. In the repository's Code tab, choose Add file > Upload files. Drag the CONTENTS of the extracted wet-okole-design folder into the upload area: assets, current, scripts, AGENTS.md, PROJECT_BRIEF.md, requirements.txt, README.md, both prompt text files, and MANIFEST.json. Replace the starter README if asked. The optional .gitignore may be hidden in Finder; it is not needed for setup.
4. Commit the uploaded files to main. Upload the extracted files, not just the ZIP. Check that AGENTS.md and the assets/current/scripts folders appear at repository root. If your browser will not upload folders, create/upload one folder at a time using GitHub's interface, or use GitHub Desktop to publish this extracted folder privately.
5. Keep the separate wet-okole-full-local-archive.zip as historical backup. Do NOT upload it for routine setup; it contains obsolete files and Mac-specific scripts. This curated package contains the necessary current assets and portable renderer.

## 2. Create and publish the Cloud environment
1. On desktop or web, start a NEW Codex task. Choose Work in > Cloud > Select environment > Create environment. Alternative: Settings > Codex Cloud > Environments > Create environment.
2. Connect GitHub if prompted and allow access to your private wet-okole-design repository. Select that repository.
3. Select Get started. Paste the contents of CLOUD_SETUP_PROMPT.txt into the environment-setup conversation.
4. Let setup install dependencies and run verification/rendering. No API key is needed. Package-manager network access may be needed during installation; rendering itself is offline.
5. Review the setup report. Resolve errors, save, then select Publish. Wait for Environment published. Saving a draft is not publishing.
6. Select Start a new task in that published environment. Paste START_HERE_PROMPT.txt. Confirm the two images match the delivered files.

## 3. Continue from iPhone
1. Open the ChatGPT app signed into the SAME account and workspace.
2. Open Codex and select Cloud (not your Mac), then the published wet-okole-design environment/task.
3. Open the continuation chat and send your next request. Cloud runs independently of your Mac. Mobile controls may differ with account rollout; if Cloud is missing, check the account/workspace and availability rather than selecting a connected Mac as a substitute.

## 4. Preserve future work
Cloud task files are not a permanent backup by themselves. After an accepted revision, ask Codex to save the new images and updated project notes in the repository, commit them, and push the branch/open a pull request. Review and merge the result on GitHub. Preserve original assets and use new filenames for revisions. A published environment is the reusable starting setup; each task has its own working files.

## Included checks
python3 -m pip install -r requirements.txt
python3 scripts/verify_package.py
python3 scripts/render_board.py

The renderer writes rendered/cloud-board-smoke-test.png; it never overwrites current/ or assets/. Authoritative final files are already supplied. Font/layout rendering is avoided by reusing the prepared board.

## Official references
- Cloud setup: https://learn.chatgpt.com/docs/environments/cloud-environments
- Execution modes/local files: https://learn.chatgpt.com/docs/environments/modes
- iPhone: https://learn.chatgpt.com/docs/mobile

This package does not upload anything, create a GitHub repository, publish an environment, or copy the full original chat history automatically.
