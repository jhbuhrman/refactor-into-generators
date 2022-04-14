# call bash explicitly on this script

## shellcheck disable=SC2154
#trap 'set -x; _ecode=$?; trap "" ERR; echo -E "*** error code ${_ecode}"; (exit ${_ecode})' ERR

set -e

source="${1?}"
target="${2?}"

ASCIIDOC="npx asciidoctor-revealjs"
ASCIIDOC_FLAGS=

MV=mv
CAT=cat
RM="rm -f"

asciidoc_err="${TMPDIR}/asciidoc.$$.stderr"
exitcode=0
echo -E ${ASCIIDOC} ${ASCIIDOC_FLAGS} -o "${target}.tmp" "${source}" >&2
${ASCIIDOC} ${ASCIIDOC_FLAGS} -o "${target}.tmp" "${source}" 2>"${asciidoc_err}" || exitcode=$?
${CAT} "${asciidoc_err}" >&2
[ -s "${asciidoc_err}" -a ${exitcode} -eq 0 ] && exitcode=2
${RM} "${asciidoc_err}"
[ ${exitcode} -eq 0 ] && ${MV} "${target}.tmp" "${target}" || ${RM} "${target}.tmp" "${target}"
[ ${exitcode} -eq 0 ] || echo -E "*** error code ${exitcode}" >&2
(exit ${exitcode})
