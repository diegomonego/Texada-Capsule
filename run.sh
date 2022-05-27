# if no arguments are provided, return usage function

function usage() {
    cat <<USAGE

    Usage: bash $0 --property

    Options:
        -g | --globally | 'G(x) -> "x" is always true

        -x | --globally | 'X(x) -> "x" is true on the event after the first one

        -f | --globally | 'F(x) -> "x" is eventually true

        --always-followed file.txt| 'G(x -> X y)' -> "x" is always followed by "y"

        --always-eventualy-followed file.txt| 'G( x -> XF y)' -> "x" is eventually followed by "y"
USAGE
    exit 1
}

if [ $# -eq 0 ]; then
   usage # run usage function
    exit 1
fi



for arg in "$1"; do
    case $arg in
    -g | --globally)
        ./texada -l -f 'G(x)'  --log-file $2
        echo "-----"
        shift # Remove --skip-verification from `$@`
        ;;
    -x | --next)
        ./texada -l -f 'X(x)'  --log-file $2
        echo "-----"
        shift # Remove --skip-verification from `$@`
        ;;
    -f | --finally)
        ./texada -l -f 'F(x)'  --log-file $2
        echo "-----"
        shift # Remove --skip-verification from `$@`
        ;;
    --always-followed)
        ./texada -l -f 'G(x -> X y)'  --log-file $2
        echo "-----"
        shift # Remove --skip-verification from `$@`
        ;;
    --always-eventualy-followed)
        ./texada -l -f 'G(x -> XF y)'  --log-file $2
        echo "-----"
        shift # Remove --skip-verification from `$@`
        ;;
    -t | --tag)
        TAG=$2
        shift # Remove argument (-t) name from `$@`
        shift # Remove argument value (latest) from `$@`
        ;;
    -h | --help)
        usage # run usage function on help
        ;;
    *)
        usage # run usage function if wrong argument provided
        ;;
    esac
done











