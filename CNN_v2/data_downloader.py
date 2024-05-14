# First install dependencies
# pip install googledrivedownloader

# Import module - dependency
from google_drive_downloader import GoogleDriveDownloader as gdd

# Download rozsevy
gdd.download_file_from_google_drive(file_id='1ynp1YRdo17EVcZTEf2357nPQx2rEV86U',
                                    dest_path='./RozsAgloSP4-2018-vystup.xlsm',
                                    overwrite=True,
                                    showsize=True)

# Download 30 min data
gdd.download_file_from_google_drive(file_id='1FE_7szFPV9E1S1JMFcYwW9o-OGoBJgAS',
                                    dest_path='./PI_DataLink_Aglo_digital twins-5min-SP4-2018-30minute.xlsm',
                                    overwrite=True,
                                    showsize=True)

# Download 15 min data
gdd.download_file_from_google_drive(file_id='1UWf1QpzjWwn_MP5hLk4QLJZYctx3uHva',
                                    dest_path='./PI_DataLink_Aglo_digital twins-5min-SP4-2018-15minute.xlsm',
                                    overwrite=True,
                                    showsize=True)

# Download 5 min data
gdd.download_file_from_google_drive(file_id='14b8iMW_miItZtBRLUGZFP0oRfp71XmsZ',
                                    dest_path='./PI_DataLink_Aglo_digital twins-5min-SP4-2018.xlsm',
                                    overwrite=True,
                                    showsize=True)

