#!/bin/bash

eval "$(direnv hook bash)"

#echo $@
invoke -e -r $TRAEFIK_HOME/src/tasks "$@"
