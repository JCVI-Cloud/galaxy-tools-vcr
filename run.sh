#!/bin/sh

export DRMAA_LIBRARY_PATH=/opt/sge/lib/lx24-amd64/libdrmaa.so.1.0
cd `dirname $0`

python -ES ./scripts/check_python.py
[ $? -ne 0 ] && exit 1

SAMPLES="
    community_wsgi.ini.sample
    datatypes_conf.xml.sample
    external_service_types_conf.xml.sample
    migrated_tools_conf.xml.sample
    reports_wsgi.ini.sample
    shed_tool_conf.xml.sample
    tool_conf.xml.sample
    tool_data_table_conf.xml.sample
    tool_sheds_conf.xml.sample
    openid_conf.xml.sample
    universe_wsgi.ini.sample
    tool-data/shared/ucsc/builds.txt.sample
    tool-data/shared/igv/igv_build_sites.txt.sample
    tool-data/shared/rviewer/rviewer_build_sites.txt.sample
    tool-data/*.sample
    static/welcome.html.sample
"

# Create any missing config/location files
for sample in $SAMPLES; do
    file=`echo $sample | sed -e 's/\.sample$//'`
    if [ ! -f "$file" -a -f "$sample" ]; then
        echo "Initializing $file from `basename $sample`"
        cp $sample $file
    fi
done

# explicitly attempt to fetch eggs before running
FETCH_EGGS=1
for arg in "$@"; do
    [ "$arg" = "--stop-daemon" ] && FETCH_EGGS=0; break
done
if [ $FETCH_EGGS -eq 1 ]; then
    python -ES ./scripts/check_eggs.py -q
    if [ $? -ne 0 ]; then
        echo "Some eggs are out of date, attempting to fetch..."
        python -ES ./scripts/fetch_eggs.py
        if [ $? -eq 0 ]; then
            echo "Fetch successful."
        else
            echo "Fetch failed."
            exit 1
        fi
    fi
fi

if [ -n "$GALAXY_RUN_ALL" ]; then
    servers=`sed -n 's/^\[server:\(.*\)\]/\1/  p' universe_wsgi.ini | xargs echo`
    daemon=`echo "$@" | grep -q daemon`
    if [ $? -ne 0 ]; then
        echo 'ERROR: $GALAXY_RUN_ALL cannot be used without the `--daemon` or `--stop-daemon` arguments to run.sh'
        exit 1
    fi
    for server in $servers; do
        echo "Handling $server with log file $server.log..."
        python -ES ./scripts/paster.py serve universe_wsgi.ini --server-name=$server --pid-file=$server.pid --log-file=$server.log $@
    done
else
    python -ES ./scripts/paster.py serve universe_wsgi.ini $@
fi
