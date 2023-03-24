import { TestBed } from '@angular/core/testing';

import { StartModeratingService } from './start-moderating.service';

describe('StartModeratingService', () => {
  let service: StartModeratingService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(StartModeratingService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
