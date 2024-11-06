$exclude = @("venv", "desafio_4.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "desafio_4.zip" -Force