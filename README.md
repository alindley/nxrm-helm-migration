# nxrm-helm-migration
This script was developed to help with the migration of hosted helm repository content from one Nexus Repository instance to another.

## Requirements
Python3 

## Execution
Modify the variables which relate to your source and target Nexus Repository instances at the top of the script.
Run the script from a directory which has adequate storage for all of the helm packages you plan to download.

## Disclaimer
This script provides an example of how to migrate helm components due to the lack of a [Export](https://help.sonatype.com/repomanager3/nexus-repository-administration/tasks/repository-export) and [Import](https://help.sonatype.com/repomanager3/nexus-repository-administration/tasks/repository-import) task.
It should be tested thoroughly before use on any production Nexus Repository instance.
This script is not supported by Sonatype and is provided as-is with MIT licence.
