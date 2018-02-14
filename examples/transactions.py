import os
import logging

from invoca import Invoca

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

api = Invoca(
    oauth_token=os.environ['INVOCA_OAUTH_TOKEN'],
    network_name=os.environ['INVOCA_NETWORK_NAME'],
    network_id=os.environ['INVOCA_NETWORK_ID']
)

logger.debug('Calling Invoca.transactions()...')
transactions = api.transactions(filters={
    'limit': 50,
    'from': '2017-01-01',
    'include_columns': ('advertiser_id_from_network,advertiser_name,'
                        'advertiser_payin_localized,affiliate_id_from_network,'
                        'affiliate_name,affiliate_payout_localized,'
                        'city,destination_phone_number,keypresses,'
                        'connect_duration,duration,ivr_duration,'
                        'recording,region,repeat_calling_phone_number,'
                        'transaction_id,hangup_cause,transfer_from_type,'
                        'start_time_utc,corrected_at,corrects_transaction_id,'
                        'advertiser_campaign_name,calling_phone_number')
})
logger.debug('Received Transactions: {}'.format(transactions))
