$exclude = @("venv", "desafio_3.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "desafio_3.zip" -Force