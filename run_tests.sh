
RETURN_CODE=0

echo
echo "Running linting and checks:"
echo

echo "Pylama..." \
&& pylama . \
\
&& echo \
&& echo "black check..." \
&& black --check . \
\
&& echo \
&& echo "Check text files..." \
&& ./check_line_lengths.sh \
\
|| RETURN_CODE=1

exit $RETURN_CODE
