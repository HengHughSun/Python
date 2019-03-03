#!/bin/bash
if [ -f $1 ]; then
	echo "This file is exist"
	exit 10
else 		
	touch "$1" 
fi
cat >> "$1" << EOF
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : `date +%H:%M:%S/%D`
# Author  : Hugh Sun
# File    : $1
# Software: $1
EOF
