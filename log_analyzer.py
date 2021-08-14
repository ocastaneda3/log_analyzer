import sys      # version 3.8.5
import re       # version 2.2.1
import gzip     

import argparse

import collections

# Python  3.9.2

# This class is used to parse auth.log files to collect information about attempted logins to an SSH session
#   1. parse: parse log file with regular expression for failed 
#   2. print_counts: prints table of counter passed into it
#   3. print_summary: check if counters contain data then call print_counts to display data
class log_stats():
    def __init__( self, filename, topn = 5, full = False, clean = False, debug = False ):
        self.filename = filename
        self.topn = topn

        self.cnt_ip_addr = collections.Counter()
        self.cnt_user = collections.Counter()
        self.cnt_port = collections.Counter()

        # Regular expression to pull 'Failed' password attempts
        self.re = re.compile( r'(?P<date>[A-Z][a-z]{2}\s*\d{1,2}).+' +                              # Date
                                '(?P<timestamp>(\d{2}:\d{2}:\d{2})).+Failed password for\s*' +      # Timestamp
                                '(?P<user>(?:\w{1,15})).+from\s*' +                                 # User
                                '(?P<ip>(?:\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})).+port\s*' +         # Source IP
                                '(?P<port>(?:\d{1,5}))'                                             # Port
                            )

        self.full = full
        self.clean = clean
        self.debug = debug

    # function - parse_file
    #   - Parse though log file provided and match entries to regular expression.
    #   - Pull matched data and store into counters.
    #   - Debuging is avaliable if set True to view data as it's processed
    #
    def parse_file( self ):
        _log = None
        _file = None

        for x in self.filename:
            # Try to read log file compressed and not
            try:
                _file = gzip.open( x, 'r') if '.gz' in x else open(x, 'r' )
                _log = _file.read()

            # Print exception if failed
            except Exception as e:
                print( e )

            # Finally close file when read
            finally:
                if _file is not None: _file.close()

            # Decode compressed byte array to string
            if isinstance( _log, bytes ):
                _log = _log.decode( 'UTF-8' )

            for _line in _log.split('\n'):
                m = self.re.match( _line )      # Match line to regular expression

                if not m: continue              # If regular expression not matched skip line

                self.cnt_ip_addr.update( [m.group( 'ip' )] )        # Store ip into counter
                if not self.full:
                    self.cnt_user.update( [m.group('user')] )       # Store username into counter
                    self.cnt_port.update( [m.group('port' )] )      # Store port into counter

                # Debug avaliable if set True
                if self.debug:
                    print( 'date/timestamp: %s %s, user: %s, ip: %s, port %s' % ( m.group('date'), m.group('timestamp'), m.group('user'), m.group('ip'), m.group('port' ) ) )
            pass

    # function - print_counts
    #   - Print table of counter passed in.
    def print_counts(self, cdict, title ):
        print( 60 * '-' )
        print( ' << Top #%2d %s >>' % (self.topn, title ) )
        print( 60 * '-' )

        for i, t in enumerate( cdict.most_common( self.topn ) ):
            if 'IP Addresses' in title:
                print( '%2s) %25s: %8d' %( i + 1, t[0][:40], t[1] ) )
            else:
                print( '%2s) %25s: %8d' %( i + 1, t[0], t[1] ) )

        print( 60 * '-' )
        pass

    # function - print_summary
    #   - Call print_counts on counters that have data to be printed
    def print_summary( self ):
        if self.cnt_ip_addr:
            self.print_counts( self.cnt_ip_addr, 'IP Addresses' )
        if self.cnt_user:
            self.print_counts( self.cnt_user, 'Users' )
        if self.cnt_port:
            self.print_counts( self.cnt_port, 'Ports' )
        pass

    def print_ip_list( self ):
        for _blank, _t in enumerate( self.cnt_ip_addr.most_common( ) ):
            if self.clean:
                print( '%s' %( _t[0][:40] ) )
            else:
                print( '%-15s %8d' %( _t[0][:40], _t[1] ) )
        pass

# ------------------------
#           Main
# ------------------------
if __name__ == '__main__':
    # Setup command line argument parsing.
    parser = argparse.ArgumentParser(prog = 'sudo log_analysis.py', description='Simple tool to pull Failed Password attempts from SSH AUTH Logs')

    parser.add_argument('filename', nargs='+', help='input file name')
    parser.add_argument('-n', metavar='N', default=5, type=int, help='print top N')
    parser.add_argument('-f','--full',  action='store_true', help='print full ip list w/ number of occurences')
    parser.add_argument('-c','--clean', action='store_true', help='print clean list and to be used with [-f] to')
    parser.add_argument('-d','--debug', action='store_true', help='enable debugging')

    parser.print_usage = parser.print_help
    
    # Parse command line arguments.
    args = parser.parse_args( )

    # Check if [--full] flag is set when [--clean] flag is set
    if args.clean and not args.full :
        sys.stderr.write( 'error: missing [-f][--full] flag\n\n' )
        parser.print_help()

    # Create log_stat object
    log_obj = log_stats( args.filename, args.n, args.full, args.clean, args.debug )

    # Parse files
    log_obj.parse_file()

    # Print default output or full list
    if args.full:
        log_obj.print_ip_list()
    else:
        log_obj.print_summary()

    sys.exit( )